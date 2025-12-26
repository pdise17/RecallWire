# FDA & Manufacturer Recall Initiation Workflow

## Overview

This document describes the workflow from the manufacturer's perspective when initiating a medical device recall, and the FDA's role in classification and oversight.

## Recall Initiation Types

| Type | Authority | Frequency |
|------|-----------|-----------|
| **Voluntary Recall** | 21 CFR Part 7 & 21 CFR Part 806 | ~99% of recalls |
| **Mandatory Recall** | 21 CFR 810 | Rare (FDA-ordered) |

## Workflow Diagram

```mermaid
sequenceDiagram
    autonumber
    participant QC as Quality Control
    participant MFR as Manufacturer
    participant FDA as FDA
    participant HC as Healthcare Facilities

    rect rgb(255, 240, 240)
        Note over QC,MFR: DISCOVERY PHASE
        QC->>MFR: Quality testing findings
        Note right of MFR: OR Customer complaints
        Note right of MFR: OR Adverse event reports
        MFR->>MFR: Issue identified (Safety/Quality)
    end

    rect rgb(240, 248, 255)
        Note over MFR: DECISION PHASE
        MFR->>MFR: Assess scope & health hazard
        alt Correction
            MFR->>MFR: Plan fix in place
        else Removal
            MFR->>MFR: Plan retrieval from field
        end
        MFR->>MFR: Develop recall strategy
    end

    rect rgb(240, 255, 240)
        Note over MFR,FDA: FDA NOTIFICATION
        MFR->>FDA: Submit via eSubmitter or email to DRC
        FDA->>FDA: Review recall strategy
        FDA->>FDA: Assign classification
        Note over FDA: Class I = Highest Risk
        Note over FDA: Class II = Moderate Risk
        Note over FDA: Class III = Lowest Risk
    end

    rect rgb(255, 250, 240)
        Note over MFR,HC: RECALL EXECUTION
        MFR->>HC: Send recall communications
        Note right of HC: Letters marked "MEDICAL DEVICE RECALL"
        Note right of HC: Bold red type on envelope
        HC-->>MFR: Response/acknowledgment
        MFR->>MFR: Track response rates & device status
    end

    rect rgb(248, 240, 255)
        Note over FDA,MFR: FDA OVERSIGHT
        loop Until Complete
            MFR->>FDA: Progress reports
            FDA->>FDA: Review & verify execution
            FDA->>HC: May conduct audit checks
        end
        FDA->>MFR: Recall termination (Goal: 3 months)
    end
```

### Flowchart View: Recall Decision Tree

```mermaid
flowchart TD
    subgraph Discovery["MANUFACTURER DISCOVERY"]
        A1[Quality Control Testing] --> B
        A2[Customer Complaints] --> B
        A3[Adverse Event Reports] --> B
        B[Issue Identified]
    end

    subgraph Decision["MANUFACTURER DECISION"]
        B --> C[Assess Scope & Health Hazard]
        C --> D{Action Type?}
        D -->|Fix in place| E1[CORRECTION]
        D -->|Retrieve from field| E2[REMOVAL]
        E1 --> F[Develop Recall Strategy]
        E2 --> F
    end

    subgraph Notification["FDA NOTIFICATION"]
        F --> G[Submit to FDA]
        G --> H[FDA Reviews Strategy]
        H --> I[FDA Assigns Classification]
        I --> J1[Class I<br/>Highest Risk]
        I --> J2[Class II<br/>Moderate Risk]
        I --> J3[Class III<br/>Lowest Risk]
    end

    subgraph Execution["RECALL EXECUTION"]
        J1 --> K[Send Communications]
        J2 --> K
        J3 --> K
        K --> L[Healthcare Facilities]
        K --> M[Distributors]
        K --> N[Healthcare Providers]
        L --> O[Track Responses]
        M --> O
        N --> O
    end

    subgraph Oversight["FDA OVERSIGHT"]
        O --> P[Progress Reports to FDA]
        P --> Q{Complete?}
        Q -->|No| P
        Q -->|Yes| R[Recall Termination]
    end

    style J1 fill:#ff6b6b,color:#fff
    style J2 fill:#ffd93d,color:#000
    style J3 fill:#6bcb77,color:#fff
```

## Recall Communication Requirements

### Required Content in Recall Notices

| Element | Description |
|---------|-------------|
| **Device Identification** | Name, model, lot/serial numbers, UDI if applicable |
| **Problem Description** | Clear explanation of the issue |
| **Health Hazard** | Potential risks to patients/users |
| **Instructions** | What the recipient should do |
| **Contact Information** | How to reach manufacturer |
| **Response Requested** | What the manufacturer needs back |

### Reporting Timeline

| Action | Timeframe |
|--------|-----------|
| Initial report to FDA | Within 10 working days of initiating recall |
| Periodic status reports | As requested by FDA |
| Final status report | When recall is complete |

## Key Differences by Recall Class

| Aspect | Class I | Class II | Class III |
|--------|---------|----------|-----------|
| **FDA Public Notice** | Press release likely | May be posted | Rarely publicized |
| **Reporting to FDA** | Required | Required | Record-keeping only |
| **Urgency** | Immediate | Standard | Low priority |
| **Audit Likelihood** | High | Moderate | Low |

## Tracking Requirements (21 CFR 821)

For certain high-risk and implantable devices, manufacturers must maintain tracking systems that allow:
- Identification of each device by lot or serial number
- Location of device (facility or patient)
- Date of distribution/implantation
- Patient identification (for implants)

Tracked devices include:
- Life-sustaining/life-supporting devices used outside facilities
- Permanently implantable devices
- Devices designated by FDA for tracking

## Sources

- [FDA Recalls, Corrections and Removals](https://www.fda.gov/medical-devices/postmarket-requirements-devices/recalls-corrections-and-removals-devices)
- [FDA Industry Guidance for Recalls](https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts/industry-guidance-recalls)
- [21 CFR Part 7 - Enforcement Policy](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-7)
- [21 CFR Part 806 - Medical Devices; Reports of Corrections and Removals](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-806)
