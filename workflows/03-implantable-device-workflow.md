# Implantable Device Recall Workflow

## Overview

Implantable device recalls represent the most complex recall scenario because they require:
1. Patient identification and tracking
2. Clinical decision-making (explant vs. monitor)
3. Surgeon and patient communication
4. Long-term follow-up

This workflow applies to: joint replacements, pacemakers/ICDs, stents, surgical mesh, breast implants, spinal hardware, cochlear implants, and similar devices.

## Critical Distinction: Device in Patient vs. Device in Inventory

```mermaid
flowchart TD
    A[IMPLANTABLE DEVICE<br/>RECALL RECEIVED] --> B[Review Recall Notice]
    B --> C{Device Location?}
    C -->|In Inventory| D[DEVICES IN INVENTORY]
    C -->|In Patients| E[DEVICES IN PATIENTS]

    D --> D1[Standard recall process:<br/>quarantine and return]
    E --> E1[Complex clinical<br/>workflow required<br/>See below]

    style D fill:#90EE90
    style E fill:#FFB6C1
    style D1 fill:#98FB98
    style E1 fill:#FFC0CB
```

## Complete Implantable Device Recall Workflow

### Sequence Diagram: End-to-End Process

```mermaid
sequenceDiagram
    autonumber
    participant RC as Recall Coordinator
    participant SYS as Data Systems
    participant TEAM as Clinical Review Team
    participant SURG as Surgeon
    participant PT as Patient

    rect rgb(240, 248, 255)
        Note over RC,SYS: PHASE 1: PATIENT IDENTIFICATION
        RC->>SYS: Search implant registry
        RC->>SYS: Search surgical logs
        RC->>SYS: Search EHR procedure notes
        RC->>SYS: Search billing/charge records
        RC->>SYS: Search manufacturer tracking DB
        RC->>SYS: Search UDI/barcode scan records
        SYS-->>RC: Match lot/serial numbers to patients
        RC->>RC: Generate affected patient list
    end

    rect rgb(255, 250, 205)
        Note over RC,TEAM: PHASE 2: CLINICAL REVIEW
        RC->>TEAM: Present affected patient list
        TEAM->>TEAM: Multidisciplinary review
        TEAM->>TEAM: Review manufacturer recommendations
        alt High Risk
            TEAM->>TEAM: Recommend EXPLANT
        else Moderate Risk
            TEAM->>TEAM: Recommend ENHANCED MONITORING
        else Low Risk
            TEAM->>TEAM: Recommend ROUTINE FOLLOW-UP
        end
        TEAM->>RC: Patient-specific action plans
    end

    rect rgb(240, 255, 240)
        Note over RC,SURG: PHASE 3: SURGEON NOTIFICATION
        RC->>SURG: Send recall details + patient list
        RC->>SURG: Provide communication templates
        SURG-->>RC: Acknowledge receipt
        SURG->>SURG: Accept responsibility for patient notification
    end

    rect rgb(255, 240, 245)
        Note over SURG,PT: PHASE 4: PATIENT NOTIFICATION
        alt Class I / Urgent
            SURG->>PT: Phone call (same day)
        else Class II / Standard
            SURG->>PT: Phone call preferred, letter backup
        else Class III / Low Risk
            SURG->>PT: Letter or portal message
        end
        SURG->>PT: Explain issue, recommendations, next steps
        PT-->>SURG: Response/acknowledgment
        SURG->>PT: Schedule follow-up if needed
    end

    rect rgb(248, 240, 255)
        Note over SURG,PT: PHASE 5: CLINICAL FOLLOW-UP
        alt Explant Pathway
            SURG->>PT: Schedule surgery
            SURG->>PT: Pre-op workup
            SURG->>PT: Explant & revision
        else Enhanced Monitoring
            SURG->>PT: Increased visit frequency
            SURG->>PT: Additional imaging
        else Routine Monitoring
            SURG->>PT: Standard follow-up schedule
        end
    end

    rect rgb(255, 245, 238)
        Note over RC,SURG: PHASE 6: DOCUMENTATION & TRACKING
        SURG->>RC: Report patient status
        RC->>RC: Track completion per patient
        RC->>RC: Report to manufacturer
    end
```

### Flowchart: Patient Identification & Clinical Decision

```mermaid
flowchart TD
    subgraph Phase1["PHASE 1: PATIENT IDENTIFICATION"]
        A[Recall Notice Received] --> B[Search Data Sources]
        B --> B1[Implant Registry]
        B --> B2[Surgical Logs]
        B --> B3[EHR Procedure Notes]
        B --> B4[Billing/Charge Records]
        B --> B5[Manufacturer Tracking DB]
        B --> B6[UDI/Barcode Scan Records]

        B1 --> C[Match lot/serial numbers<br/>to patient records]
        B2 --> C
        B3 --> C
        B4 --> C
        B5 --> C
        B6 --> C

        C --> D[Generate Affected Patient List]
        D --> D1[Patient name & MRN]
        D --> D2[Contact info]
        D --> D3[Implant date]
        D --> D4[Implanting surgeon]
        D --> D5[Device details]
    end

    subgraph Phase2["PHASE 2: CLINICAL REVIEW"]
        D1 --> E[Multidisciplinary Clinical Review]
        D2 --> E
        D3 --> E
        D4 --> E
        D5 --> E

        E --> F[Review Manufacturer Recommendations]
        F --> G{Clinical Decision?}

        G -->|High risk of failure<br/>Imminent harm| H1[EXPLANT RECOMMENDED]
        G -->|Moderate risk<br/>Balance risk/benefit| H2[ENHANCED MONITORING]
        G -->|Low risk<br/>Labeling issue only| H3[ROUTINE FOLLOW-UP]

        H1 --> I[Develop Patient-Specific<br/>Action Plans]
        H2 --> I
        H3 --> I
    end

    style H1 fill:#ff6b6b,color:#fff
    style H2 fill:#ffd93d,color:#000
    style H3 fill:#6bcb77,color:#fff
```

### Flowchart: Patient Notification & Follow-up

```mermaid
flowchart TD
    subgraph Phase3["PHASE 3: SURGEON NOTIFICATION"]
        A[Patient-Specific Action Plans] --> B[Notify Implanting Surgeons]
        B --> B1[Recall details & classification]
        B --> B2[List of their affected patients]
        B --> B3[Manufacturer recommendations]
        B --> B4[Institution's clinical guidance]
        B --> B5[Patient communication templates]

        B1 --> C[Surgeon Acknowledges Receipt]
        B2 --> C
        B3 --> C
        B4 --> C
        B5 --> C
    end

    subgraph Phase4["PHASE 4: PATIENT NOTIFICATION"]
        C --> D{Recall Class?}

        D -->|Class I / Urgent| E1[Phone call - same day<br/>Document all attempts]
        D -->|Class II / Standard| E2[Phone call preferred<br/>Letter backup<br/>1-2 week timeline]
        D -->|Class III / Low Risk| E3[Letter or portal message<br/>Next scheduled visit]

        E1 --> F[Patient Communication Content]
        E2 --> F
        E3 --> F

        F --> F1[Clear explanation - no jargon]
        F --> F2[Why they're being contacted]
        F --> F3[What recall means for them]
        F --> F4[Recommended action]
        F --> F5[Symptoms to watch for]
        F --> F6[How to contact care team]

        F1 --> G[Schedule Follow-up<br/>Appointment if Needed]
        F2 --> G
        F3 --> G
        F4 --> G
        F5 --> G
        F6 --> G
    end

    subgraph Phase5["PHASE 5: CLINICAL FOLLOW-UP"]
        G --> H{Follow-up Pathway?}

        H -->|Explant| I1[EXPLANT PATHWAY]
        H -->|Enhanced| I2[ENHANCED MONITORING]
        H -->|Routine| I3[ROUTINE MONITORING]

        I1 --> I1a[Schedule surgery]
        I1 --> I1b[Pre-op workup]
        I1 --> I1c[Explant & revision]
        I1 --> I1d[Send device to mfr]

        I2 --> I2a[Increased visit frequency]
        I2 --> I2b[Additional imaging]
        I2 --> I2c[Remote monitoring if available]

        I3 --> I3a[Standard follow-up schedule]
        I3 --> I3b[Document in chart]
    end

    subgraph Phase6["PHASE 6: DOCUMENTATION & TRACKING"]
        I1d --> J[Track Completion Status]
        I2c --> J
        I3b --> J

        J --> J1[Notified]
        J --> J2[Appointment scheduled]
        J --> J3[Seen by provider]
        J --> J4[Action completed]
        J --> J5[Closed]

        J1 --> K[Report to Manufacturer]
        J2 --> K
        J3 --> K
        J4 --> K
        J5 --> K
    end

    style E1 fill:#ff6b6b,color:#fff
    style E2 fill:#ffd93d,color:#000
    style E3 fill:#6bcb77,color:#fff
    style I1 fill:#ff6b6b,color:#fff
    style I2 fill:#ffd93d,color:#000
    style I3 fill:#6bcb77,color:#fff
```

## Explant vs. Monitor Decision Framework

| Factor | Favors Explant | Favors Monitor |
|--------|---------------|----------------|
| **Device failure risk** | High/imminent | Low/theoretical |
| **Failure consequences** | Severe/life-threatening | Manageable |
| **Surgical risk** | Low | High (age, comorbidities) |
| **Device criticality** | Replaceable function | Life-sustaining |
| **Alternative available** | Yes | No/limited options |
| **Patient preference** | Prefers removal | Prefers to keep |
| **Time in body** | Recent | Long-standing, stable |

## Patient Unreachable Protocol

```mermaid
flowchart TD
    A[Attempt 1: Phone call<br/>to primary number] --> B{Successful?}
    B -->|Yes| Z[Patient Notified]
    B -->|No| C[Attempt 2: Phone call<br/>to secondary number]

    C --> D{Successful?}
    D -->|Yes| Z
    D -->|No| E[Attempt 3: Certified letter<br/>to address on file]

    E --> F{Successful?}
    F -->|Yes| Z
    F -->|No| G[Attempt 4: Emergency<br/>contact outreach]

    G --> H{Successful?}
    H -->|Yes| Z
    H -->|No| I[Attempt 5: Portal message<br/>if patient has access]

    I --> J{Successful?}
    J -->|Yes| Z
    J -->|No| K[Document all attempts]

    K --> L[Continue periodic outreach]
    L --> M[Flag in system for notification<br/>at next encounter]

    style Z fill:#90EE90
    style K fill:#FFB6C1
    style M fill:#FFD700
```

## Special Considerations by Device Type

### Cardiac Implants (Pacemakers, ICDs)
- Remote monitoring capability may allow early detection
- Device interrogation can provide data on function
- Manufacturer may provide firmware update option
- Consider temporary external monitoring during decision

### Orthopedic Implants (Hips, Knees, Spine)
- Imaging may be needed to assess device position/wear
- Pain/symptoms may indicate early failure
- Revision surgery is major undertaking
- Metal ion testing may be relevant

### Vascular Devices (Stents, Filters)
- May be high-risk to remove
- Monitoring for complications (thrombosis, migration)
- Anticoagulation considerations

## Challenges Specific to Implant Recalls

| Challenge | Impact | Mitigation |
|-----------|--------|-----------|
| **Incomplete tracking data** | Can't identify all patients | Improve UDI capture at implant |
| **Outdated contact info** | Can't reach patients | Verify at each visit |
| **Patient moved/transferred care** | Physician no longer managing | Coordination with new providers |
| **Deceased patients** | Still appear on lists | Death registry cross-reference |
| **Patient anxiety** | Psychological distress | Provide support resources |
| **Medicolegal concerns** | Liability exposure | Risk management involvement |

## Sources

- [ASPS: FDA Recalls - What Happens and What Should You Do](https://www.plasticsurgery.org/news/articles/fda-recalls-what-happens-when-there-is-a-recall-and-what-should-you-do)
- [AAOS Information Statement: Implant Device Recalls](https://www.aaos.org/globalassets/about/bylaws-library/information-statements/1019-implant-device-recalls1.pdf)
- [InVita: Match Medical Device Recall Notifications to Affected Patients](https://www.invitahealth.com/match-medical-device-recall-notifications-to-affected-patients/)
- [MedTech Dive: Anatomy of a Medical Device Recall](https://www.medtechdive.com/news/medical-device-recall-process-fda-philips-medtronic/608205/)
