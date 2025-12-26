# Surgical Instrument Recall Workflow

## Overview

Surgical instrument recalls occupy a middle ground between implantable devices and capital equipment:
- They may require patient identification if used during procedures
- They are reusable, requiring inventory tracking across departments
- Sterile processing/central sterile plays a critical role
- Turnaround is often faster than imaging equipment recalls

This workflow applies to: surgical instruments, robotic surgical systems, reusable scopes, surgical power tools, electrosurgical devices, and similar equipment.

## Surgical Instrument Categories

| Category | Examples | Tracking Complexity |
|----------|----------|-------------------|
| **Reusable Instruments** | Forceps, retractors, scissors | Low (inventory) |
| **Power Equipment** | Drills, saws, powered instruments | Medium (serial tracked) |
| **Robotic Systems** | da Vinci, Mako, etc. | High (case logs) |
| **Scopes/Cameras** | Laparoscopes, arthroscopes | Medium (serial + reprocessing) |
| **Electrosurgical** | Generators, handpieces | Medium (serial tracked) |
| **Single-Use Instruments** | Disposable trocars, staplers | Low (lot tracking) |

## Workflow Diagram

### Sequence Diagram: Surgical Instrument Recall Response

```mermaid
sequenceDiagram
    autonumber
    participant SRC as Notification Source
    participant RC as Recall Coordinator
    participant SPD as Sterile Processing
    participant OR as OR/Surgical Services
    participant MFR as Manufacturer

    rect rgb(255, 245, 238)
        Note over SRC,RC: NOTIFICATION RECEIPT
        SRC->>RC: Manufacturer / Alert Service / Service Rep
        RC->>SPD: Notify Sterile Processing
        RC->>OR: Notify Surgical Services
    end

    rect rgb(240, 248, 255)
        Note over RC,SPD: INSTRUMENT IDENTIFICATION
        RC->>SPD: Search Central Sterile Processing
        RC->>OR: Search Operating Rooms
        RC->>OR: Search Procedure Areas, Clinics, ED
        RC->>RC: Match model/serial/lot numbers to recall
        alt Affected Instruments Found
            RC->>SPD: Proceed to quarantine
        else Not Affected
            RC->>RC: Document & Close
        end
    end

    rect rgb(255, 250, 205)
        Note over SPD,OR: IMMEDIATE QUARANTINE
        SPD->>SPD: Pull from sterile storage & trays
        OR->>OR: Retrieve from OR back tables
        SPD->>SPD: Apply "RECALLED - DO NOT USE" label
        SPD->>SPD: Update tracking system
        SPD->>OR: Notify OR/Surgical Leadership
    end

    rect rgb(240, 255, 240)
        Note over RC: PATIENT IMPACT ASSESSMENT
        RC->>RC: Was instrument used on patients?
        RC->>RC: Assess risk: retained material, infection, harm
        alt Patient Impact Possible
            RC->>OR: Cross-reference surgical logs
            RC->>RC: Generate affected patient list
            Note over RC: Follow implantable device<br/>workflow for notifications
        else No Patient Impact
            RC->>RC: Skip to corrective action
        end
    end

    rect rgb(255, 240, 245)
        Note over RC,MFR: CORRECTIVE ACTION
        alt Return to Manufacturer
            RC->>MFR: Obtain RMA & ship
        else On-Site Repair
            MFR->>SPD: Service tech visits
        else Destroy/Discard
            SPD->>SPD: Follow biohazard protocol
        end
        SPD->>SPD: Update tray contents/pick lists
        RC->>MFR: Source replacement instruments
    end

    rect rgb(248, 240, 255)
        Note over SPD: STERILE PROCESSING ACTIONS
        SPD->>SPD: Review all tray contents
        SPD->>SPD: Update count sheets
        SPD->>OR: Communicate temporary shortages
        SPD->>SPD: Ensure no reintroduction
    end

    rect rgb(255, 248, 240)
        Note over RC: DOCUMENTATION & CLOSURE
        RC->>RC: Complete all documentation
        RC->>MFR: Respond to manufacturer
        RC->>RC: Close recall in tracking system
    end
```

### Flowchart: Surgical Instrument Recall Decision Tree

```mermaid
flowchart TD
    subgraph Receipt["1. NOTIFICATION RECEIPT"]
        A1[Manufacturer Letter/Email] --> B[Recall Coordinator<br/>+ Surgical Services<br/>+ Sterile Processing]
        A2[Third-party Alert Service] --> B
        A3[Service Rep Notification] --> B
    end

    subgraph Identification["2. INSTRUMENT IDENTIFICATION"]
        B --> C[Search Multiple Locations]
        C --> C1[Central Sterile Processing]
        C --> C2[Operating Rooms]
        C --> C3[Procedure Areas - Endo, Cath]
        C --> C4[Clinic/Office Procedure Rooms]
        C --> C5[Emergency Department]
        C --> C6[Supply Inventory]

        C1 --> D[Check Against Recall]
        C2 --> D
        C3 --> D
        C4 --> D
        C5 --> D
        C6 --> D

        D --> D1[Model numbers]
        D --> D2[Serial numbers]
        D --> D3[Lot numbers]
        D --> D4[Manufacturing date ranges]
        D --> D5[Instrument tray contents]

        D1 --> E{Affected<br/>Instruments?}
        D2 --> E
        D3 --> E
        D4 --> E
        D5 --> E

        E -->|No| F[Document & Close]
        E -->|Yes| G[Proceed to Quarantine]
    end

    subgraph Quarantine["3. IMMEDIATE QUARANTINE"]
        G --> H[Remove from Circulation]
        H --> H1[Pull from sterile storage]
        H --> H2[Remove from instrument trays]
        H --> H3[Retrieve from OR back tables]
        H --> H4[Check loaner/consignment]

        H1 --> I[Segregate and Label]
        H2 --> I
        H3 --> I
        H4 --> I

        I --> I1[Designated quarantine area]
        I --> I2[RECALLED - DO NOT USE label]
        I --> I3[Maintain chain of custody]

        I1 --> J[Prevent Reintroduction]
        I2 --> J
        I3 --> J

        J --> J1[Update tracking system]
        J --> J2[Alert sterile processing]
        J --> J3[Block in inventory system]

        J1 --> K[Notify OR/Surgical Leadership]
        J2 --> K
        J3 --> K
    end

    subgraph Assessment["4. PATIENT IMPACT ASSESSMENT"]
        K --> L{Was instrument<br/>used on patients?}

        L --> L1[Nature of defect?]
        L --> L2[Could patients be harmed?]
        L --> L3[Retained fragment risk?]
        L --> L4[Infection transmission risk?]

        L1 --> M{Patient Impact<br/>Possible?}
        L2 --> M
        L3 --> M
        L4 --> M

        M -->|Yes| N1[PATIENT IMPACT POSSIBLE]
        M -->|No| N2[NO PATIENT IMPACT]

        N1 --> O[Proceed to Patient Identification]
        N2 --> P[Skip to Corrective Action]
    end

    subgraph PatientID["5. PATIENT IDENTIFICATION"]
        O --> Q[Cross-Reference Data Sources]
        Q --> Q1[Surgical Case Logs]
        Q --> Q2[Instrument Tracking System]
        Q --> Q3[Preference Cards]
        Q --> Q4[OR Schedule Records]
        Q --> Q5[Affected Date Range]

        Q1 --> R[Generate Affected Patient List]
        Q2 --> R
        Q3 --> R
        Q4 --> R
        Q5 --> R

        R --> S[Follow Implantable Device<br/>Workflow for Patient Notification<br/>See 03-implantable-device-workflow.md]
        S --> P
    end

    subgraph Corrective["6. CORRECTIVE ACTION"]
        P --> T{Action Type?}
        T -->|Return| U1[RETURN TO MANUFACTURER]
        T -->|Repair| U2[ON-SITE REPAIR]
        T -->|Destroy| U3[DESTROY/DISCARD]

        U1 --> U1a[Obtain RMA #]
        U1 --> U1b[Package per instructions]
        U1 --> U1c[Ship and track]

        U2 --> U2a[Service tech visits]
        U2 --> U2b[Replace component]
        U2 --> U2c[Re-validate]

        U3 --> U3a[Follow biohazard protocol]
        U3 --> U3b[Document destruction]
        U3 --> U3c[Obtain certification]

        U1c --> V[Update Tray Contents/Pick Lists]
        U2c --> V
        U3c --> V

        V --> W[Source Replacement Instruments]
    end

    subgraph SPD["7. STERILE PROCESSING ACTIONS"]
        W --> X[SPD/CSSD Actions]
        X --> X1[Review all tray contents]
        X --> X2[Update count sheets]
        X --> X3[Communicate temporary shortages]
        X --> X4[Coordinate loaner needs]
        X --> X5[Prevent reintroduction to workflow]
    end

    subgraph Closure["8. DOCUMENTATION & CLOSURE"]
        X1 --> Y[Complete Documentation]
        X2 --> Y
        X3 --> Y
        X4 --> Y
        X5 --> Y

        Y --> Z[Close Recall in Tracking System]
    end

    style N1 fill:#ff6b6b,color:#fff
    style N2 fill:#6bcb77,color:#fff
    style F fill:#90EE90
    style Z fill:#90EE90
```

## Robotic Surgery System Considerations

Robotic surgical systems (e.g., da Vinci, Mako) have unique recall considerations:

| Aspect | Consideration |
|--------|--------------|
| **Case Tracking** | All procedures logged; easier patient identification |
| **Software Updates** | May be pushed remotely |
| **Instrument Arms** | Tracked individually, may require calibration |
| **Training Records** | May need to notify trained surgeons |
| **Service Contracts** | Manufacturer often manages updates |

## Loaner/Consignment Instrument Workflow

```mermaid
flowchart TD
    A[Recall Received] --> B[Check for Loaner/Consignment Instruments]

    B --> C{Instrument Status?}

    C -->|In-house currently| D[Quarantine immediately]
    C -->|Recently returned| E[Contact vendor to<br/>confirm receipt]
    C -->|Expected for<br/>upcoming case| F[Notify vendor<br/>Do not accept]

    D --> G[Follow standard<br/>recall process]
    E --> H[Document confirmation]
    F --> I[Source alternative<br/>for case]

    style D fill:#ff6b6b,color:#fff
    style E fill:#ffd93d,color:#000
    style F fill:#ffd93d,color:#000
```

## Response Timeline by Recall Class

| Class | Quarantine | Investigation | Corrective Action |
|-------|------------|---------------|-------------------|
| **Class I** | Immediate | 24-48 hours | ASAP |
| **Class II** | Same day | 1 week | 2-4 weeks |
| **Class III** | 1-3 days | As needed | Standard timing |

## Common Surgical Instrument Recall Causes

| Cause | Examples | Patient Impact Likelihood |
|-------|----------|--------------------------|
| **Breakage/Fatigue** | Tip breaks off, retained in patient | High |
| **Sterility Breach** | Packaging failure | Moderate |
| **Manufacturing Defect** | Wrong material, sharp edges | Variable |
| **Labeling Error** | Wrong size indicated | Variable |
| **Software Bug** | Robotic system calculation error | High |
| **Cleaning Issues** | Scope reprocessing concerns | High |

## Sources

- [FDA Recalls, Corrections and Removals](https://www.fda.gov/medical-devices/postmarket-requirements-devices/recalls-corrections-and-removals-devices)
- [24x7 Magazine: Effectively Managing Recalls](https://24x7mag.com/standards/regulations/effectively-managing-recalls/)
- [ECRI Alerts Workflow](https://home.ecri.org/pages/ecri-alerts-workflow-automated-recall-management-software)
