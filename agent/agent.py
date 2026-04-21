import json
import argparse
import os
import sys


# ---------------------------------------------------------------
# Loading & validation
# ---------------------------------------------------------------

def load_tree(path):
    """Load the tree JSON and sanity-check it. Fail loudly, not silently."""
    if not os.path.exists(path):
        sys.exit(f"Couldn't find the tree file at: {path}")

    with open(path, "r", encoding="utf-8") as f:
        tree = json.load(f)

    # Minimum things we need to exist
    for key in ("startNode", "nodes"):
        if key not in tree:
            sys.exit(f"Tree file is missing required key: '{key}'")

    # Every node needs an id and a type, or we can't walk it
    for node in tree["nodes"]:
        if "id" not in node or "type" not in node:
            sys.exit(f"A node is missing id or type: {node}")

    return tree


def index_by_id(tree):
    """Turn the list of nodes into a dict {id -> node} for fast lookup."""
    return {n["id"]: n for n in tree["nodes"]}


# ---------------------------------------------------------------
# Session state
# ---------------------------------------------------------------

def fresh_state():
    """What a brand-new session looks like."""
    return {
        "answers": {},   # node_id -> label the person picked
        "signals": {},   # e.g. "axis1:internal" -> count
        "path": [],      # every node visited, in order (for audit)
    }


def add_signal(state, signal):
    """Bump the counter for a signal like 'axis1:internal'."""
    if not signal:
        return
    state["signals"][signal] = state["signals"].get(signal, 0) + 1


def axis_tally(state, axis):
    """Get {pole: count} for one axis, e.g. axis1 -> {'internal': 2, 'external': 1}."""
    out = {}
    for key, val in state["signals"].items():
        if key.startswith(f"{axis}:"):
            pole = key.split(":", 1)[1]
            out[pole] = val
    return out


def axis_dominant(state, axis, fallback="balanced"):
    """Which pole of this axis did the person lean toward? Ties -> balanced."""
    tally = axis_tally(state, axis)
    if not tally:
        return fallback
    # Sort highest-count first
    ranked = sorted(tally.items(), key=lambda kv: kv[1], reverse=True)
    # If the top two are tied, it's actually balanced
    if len(ranked) >= 2 and ranked[0][1] == ranked[1][1]:
        return fallback
    return ranked[0][0]


# ---------------------------------------------------------------
# Evaluating decision conditions — the safe way, no eval()
# ---------------------------------------------------------------
#
# A condition looks like: "axis1.internal >= axis1.external"
# Or simpler:             "axis2.contribution > axis2.entitlement"
#
# I split on the operator, look up each side as a signal count,
# and compare. That's it.
# ---------------------------------------------------------------

def evaluate_condition(expr, state):
    # Check longer operators first (>= before >) so we don't mis-split
    for op in (">=", "<=", "==", "!=", ">", "<"):
        if op in expr:
            left_raw, right_raw = [s.strip() for s in expr.split(op, 1)]
            left = resolve_operand(left_raw, state)
            right = resolve_operand(right_raw, state)
            return compare(left, right, op)
    raise ValueError(f"Don't know how to evaluate condition: {expr}")


def resolve_operand(token, state):
    """
    Turn a token into a number.
      '5'                  -> 5
      'axis1.internal'     -> however many internal signals we've seen
      anything else        -> 0 (safe default)
    """
    if token.isdigit():
        return int(token)
    if "." in token:
        axis, pole = token.split(".", 1)
        return state["signals"].get(f"{axis}:{pole}", 0)
    return 0


def compare(a, b, op):
    return {
        ">=": a >= b, "<=": a <= b,
        ">": a > b,   "<": a < b,
        "==": a == b, "!=": a != b,
    }[op]


def route_decision(node, state):
    """Walk the conditions list top-to-bottom, return the next node id."""
    for cond in node.get("conditions", []):
        if cond.get("else"):
            return cond["next"]
        if "if" in cond and evaluate_condition(cond["if"], state):
            return cond["next"]
    raise ValueError(f"No matching condition at decision node {node['id']}")


# ---------------------------------------------------------------
# Text interpolation — replacing {placeholders}
# ---------------------------------------------------------------

def interpolate(text, state, tree):
    """
    Replace placeholders in a text field. Supported:
        {axis1.dominant}, {axis2.dominant}, {axis3.dominant}
        {NODE_ID.answer}
        {closing_prompt}
    """
    out = text

    # Axis dominants — turn 'internal' into 'toward agency' etc.
    for axis in ("axis1", "axis2", "axis3"):
        placeholder = "{" + f"{axis}.dominant" + "}"
        if placeholder in out:
            dom = axis_dominant(state, axis)
            out = out.replace(placeholder, humanize(axis, dom))

    # Insert earlier answers back into the text if asked
    for node_id, answer in state["answers"].items():
        placeholder = "{" + f"{node_id}.answer" + "}"
        if placeholder in out:
            out = out.replace(placeholder, answer)

    # The summary uses {closing_prompt} — pick the right one
    if "{closing_prompt}" in out:
        out = out.replace("{closing_prompt}", pick_closing(state, tree))

    return out


def humanize(axis, pole):
    """Internal labels -> words a tired person actually wants to read."""
    mapping = {
        "axis1": {"internal": "toward agency", "external": "toward circumstance", "balanced": "evenly"},
        "axis2": {"contribution": "toward giving", "entitlement": "toward keeping score", "balanced": "evenly"},
        "axis3": {"self": "inward", "other": "outward", "balanced": "evenly"},
    }
    return mapping.get(axis, {}).get(pole, pole)


def pick_closing(state, tree):
    """Compose the right closing prompt based on the three dominants."""
    a1 = axis_dominant(state, "axis1", "external")
    a2 = axis_dominant(state, "axis2", "entitlement")
    a3 = axis_dominant(state, "axis3", "self")
    key = f"{a1}_{a2}_{a3}"
    # Fallback is intentionally humble — the tree might not have this combo
    return tree.get("closingPrompts", {}).get(
        key,
        "Tomorrow's another draft. Keep writing."
    )


# ---------------------------------------------------------------
# Rendering to the terminal
# ---------------------------------------------------------------

def show(node, state, tree):
    """Print a node's text, interpolated, with a simple divider."""
    text = interpolate(node.get("text", ""), state, tree)
    print("\n" + "-" * 62)
    print(text)
    print("-" * 62)


def ask(options):
    """Ask the person to pick one option. Keep asking until they do."""
    for i, opt in enumerate(options, 1):
        print(f"  {i}) {opt['label']}")
    while True:
        raw = input("\nYour pick: ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return int(raw) - 1
        print(f"Pick a number from 1 to {len(options)}.")


# ---------------------------------------------------------------
# The main walk
# ---------------------------------------------------------------

def walk(tree):
    """Walk from startNode to the first end node. Returns final state."""
    nodes = index_by_id(tree)
    state = fresh_state()
    current = tree["startNode"]

    while current:
        if current not in nodes:
            sys.exit(f"Broken link — node '{current}' doesn't exist.")

        node = nodes[current]
        state["path"].append(current)
        kind = node["type"]

        # Decisions are invisible — just route and continue
        if kind == "decision":
            current = route_decision(node, state)
            continue

        show(node, state, tree)

        if kind == "question":
            idx = ask(node["options"])
            chosen = node["options"][idx]
            state["answers"][node["id"]] = chosen["label"]
            add_signal(state, chosen.get("signal"))
            current = chosen["next"]

        elif kind in ("start", "bridge", "reflection", "summary"):
            input("\n[press Enter to continue]")
            current = node.get("next")

        elif kind == "end":
            print()
            break

        else:
            sys.exit(f"Don't know how to handle node type '{kind}' (at {node['id']})")

    return state


# ---------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Daily Reflection Agent")
    parser.add_argument(
        "--tree",
        default=os.path.join(os.path.dirname(__file__), "..", "tree", "reflection-tree.json"),
        help="Path to reflection-tree.json",
    )
    args = parser.parse_args()

    tree = load_tree(args.tree)
    state = walk(tree)

    # Audit trail — so anyone reviewing can see exactly which nodes fired
    print("\n(audit — nodes visited this session:)")
    print(" -> ".join(state["path"]))


if __name__ == "__main__":
    main()
