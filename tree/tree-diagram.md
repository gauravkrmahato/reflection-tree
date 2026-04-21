# The Tree — Visual Map

I kept going back and forth on whether to include this diagram, because the JSON file is already the source of truth. But when I tried to explain my own tree to a friend verbally, I realized a picture saves a lot of words. So — here.

```mermaid
flowchart TD
    START([START: evening check-in])
    START --> A1_OPEN

    A1_OPEN{{Weather of today?}}
    A1_OPEN -->|Clear skies| A1_Q_AGENCY_HIGH
    A1_OPEN -->|Partly cloudy| A1_Q_AGENCY_MIXED
    A1_OPEN -->|Storms| A1_Q_AGENCY_LOW
    A1_OPEN -->|Fog| A1_Q_AGENCY_LOW

    A1_Q_AGENCY_HIGH{{What made the good part good?}}
    A1_Q_AGENCY_MIXED{{When it stumbled — first instinct?}}
    A1_Q_AGENCY_LOW{{When it got hard — where did attention go?}}

    A1_Q_AGENCY_HIGH -->|Prepared / Adapted| A1_R_INTERNAL
    A1_Q_AGENCY_HIGH -->|Team / Luck| A1_R_EXTERNAL
    A1_Q_AGENCY_MIXED -->|Self-check / Try again| A1_R_INTERNAL
    A1_Q_AGENCY_MIXED -->|Frustrated / Wait| A1_R_EXTERNAL
    A1_Q_AGENCY_LOW -->|Found small control| A1_R_INTERNAL
    A1_Q_AGENCY_LOW -->|Blame / Stuck / Alone| A1_R_EXTERNAL

    A1_R_INTERNAL[/Reflection: you had your hands on the wheel/]
    A1_R_EXTERNAL[/Reflection: find the small call that was yours/]

    A1_R_INTERNAL --> A1_D_BRIDGE
    A1_R_EXTERNAL --> A1_D_BRIDGE

    A1_D_BRIDGE{Decision: which way did Axis 1 go?}
    A1_D_BRIDGE -->|internal ≥ external| BRIDGE_1_TO_2_STRONG
    A1_D_BRIDGE -->|else| BRIDGE_1_TO_2_SOFT

    BRIDGE_1_TO_2_STRONG[Bridge: now — what you gave]
    BRIDGE_1_TO_2_SOFT[Bridge: now — what flowed out of you]
    BRIDGE_1_TO_2_STRONG --> A2_OPEN
    BRIDGE_1_TO_2_SOFT --> A2_OPEN

    A2_OPEN{{Pick one real interaction from today}}
    A2_OPEN -->|Helped / Extra effort| A2_Q_CONTRIB_DEEP
    A2_OPEN -->|Felt under-credited / Others slacked| A2_Q_ENTITLE_DEEP
    A2_OPEN -->|Just surviving| A2_Q_NEUTRAL_DEEP

    A2_Q_CONTRIB_DEEP{{What was underneath the giving?}}
    A2_Q_ENTITLE_DEEP{{What's the shape of that feeling?}}
    A2_Q_NEUTRAL_DEEP{{Any small giving still slip through?}}

    A2_Q_CONTRIB_DEEP --> A2_R_CONTRIBUTION
    A2_Q_CONTRIB_DEEP --> A2_R_MIXED
    A2_Q_ENTITLE_DEEP --> A2_R_ENTITLEMENT
    A2_Q_ENTITLE_DEEP --> A2_R_MIXED
    A2_Q_ENTITLE_DEEP --> A2_R_CONTRIBUTION
    A2_Q_NEUTRAL_DEEP --> A2_R_CONTRIBUTION
    A2_Q_NEUTRAL_DEEP --> A2_R_MIXED

    A2_R_CONTRIBUTION[/Reflection: quiet engine of good teams/]
    A2_R_ENTITLEMENT[/Reflection: under-seen is real — what's the measure?/]
    A2_R_MIXED[/Reflection: most days are tangled/]

    A2_R_CONTRIBUTION --> A2_D_BRIDGE
    A2_R_ENTITLEMENT --> A2_D_BRIDGE
    A2_R_MIXED --> A2_D_BRIDGE

    A2_D_BRIDGE{Decision: which way did Axis 2 go?}
    A2_D_BRIDGE -->|contribution > entitlement| BRIDGE_2_TO_3_STRONG
    A2_D_BRIDGE -->|else| BRIDGE_2_TO_3_SOFT

    BRIDGE_2_TO_3_STRONG[Bridge: zoom out — who else was there?]
    BRIDGE_2_TO_3_SOFT[Bridge: others had weather too]
    BRIDGE_2_TO_3_STRONG --> A3_OPEN
    BRIDGE_2_TO_3_SOFT --> A3_OPEN

    A3_OPEN{{Hardest moment — who's in the picture?}}
    A3_OPEN -->|Just me / Me + 1| A3_Q_WIDEN
    A3_OPEN -->|Team / User| A3_Q_DEEPEN

    A3_Q_WIDEN{{Pull back — whose day did yours touch?}}
    A3_Q_DEEPEN{{From their side — what was today?}}

    A3_Q_WIDEN --> A3_R_WIDENED
    A3_Q_WIDEN --> A3_R_STILL_SELF
    A3_Q_DEEPEN --> A3_R_DEEPENED
    A3_Q_DEEPEN --> A3_R_WIDENED

    A3_R_DEEPENED[/Reflection: not alone in the carrying/]
    A3_R_WIDENED[/Reflection: small work ripples/]
    A3_R_STILL_SELF[/Reflection: ask tomorrow — who is this for?/]

    A3_R_DEEPENED --> SUMMARY
    A3_R_WIDENED --> SUMMARY
    A3_R_STILL_SELF --> SUMMARY

    SUMMARY[[SUMMARY: three frames + one closing thought]]
    SUMMARY --> END
    END([END: rest well])

    classDef question fill:#e3f2fd,stroke:#1976d2,color:#000
    classDef reflection fill:#fff3e0,stroke:#f57c00,color:#000
    classDef bridge fill:#f3e5f5,stroke:#7b1fa2,color:#000
    classDef decision fill:#ffebee,stroke:#c62828,color:#000

    class A1_OPEN,A1_Q_AGENCY_HIGH,A1_Q_AGENCY_MIXED,A1_Q_AGENCY_LOW,A2_OPEN,A2_Q_CONTRIB_DEEP,A2_Q_ENTITLE_DEEP,A2_Q_NEUTRAL_DEEP,A3_OPEN,A3_Q_WIDEN,A3_Q_DEEPEN question
    class A1_R_INTERNAL,A1_R_EXTERNAL,A2_R_CONTRIBUTION,A2_R_ENTITLEMENT,A2_R_MIXED,A3_R_DEEPENED,A3_R_WIDENED,A3_R_STILL_SELF reflection
    class BRIDGE_1_TO_2_STRONG,BRIDGE_1_TO_2_SOFT,BRIDGE_2_TO_3_STRONG,BRIDGE_2_TO_3_SOFT bridge
    class A1_D_BRIDGE,A2_D_BRIDGE decision
```

## How to read this

- **Blue diamonds** = questions (person picks one)
- **Orange** = reflections (person reads, presses continue)
- **Purple** = bridges (short transitions between axes)
- **Red diamonds** = decisions (invisible to the person — just routing based on their earlier picks)
- **Rounded** = start / end

## The three axes, again

| # | Axis | The spectrum | Section |
|---|---|---|---|
| 1 | Locus | Victim ↔ Victor | `A1_*` |
| 2 | Orientation | Entitlement ↔ Contribution | `A2_*` |
| 3 | Radius | Self-centric ↔ Altrocentric | `A3_*` |
