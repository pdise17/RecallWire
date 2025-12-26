# Hospital Internal Recall Response Workflow

## Overview

This document describes the workflow a hospital or health system follows when responding to a medical device recall. This process is governed by Joint Commission standard EC.02.01.01 EP 11, which requires hospitals to have procedures for monitoring and acting on product hazard notices and recalls.

## Organizational Structure

### Recommended Recall Committee Composition

| Department | Role in Recall Process |
|------------|----------------------|
| **Clinical Engineering / Biomed** | Equipment identification, service coordination |
| **Materials Management / Supply Chain** | Inventory tracking, product procurement |
| **Risk Management** | Liability assessment, documentation oversight |
| **Quality / Patient Safety** | Patient impact assessment, outcome tracking |
| **Radiology** | Department-specific imaging equipment |
| **Surgery / OR** | Surgical instruments, implants |
| **Nursing** | Point-of-care devices, patient notification |
| **Pharmacy** | Drug-device combinations |
| **IT** | Software devices, system updates |
| **Administration** | Resource allocation, executive decisions |

### Key Roles

| Role | Responsibilities |
|------|-----------------|
| **Recall Coordinator** | Central point for receiving/acting on all recalls |
| **Department Liaisons** | Department-level implementation |
| **Patient Navigator** | Patient communication for implant recalls |

## Workflow Diagram

### Sequence Diagram: Hospital Recall Response

```mermaid
sequenceDiagram
    autonumber
    participant SRC as Notification Source
    participant RC as Recall Coordinator
    participant INV as Inventory Systems
    participant DEPT as Affected Departments
    participant MFR as Manufacturer

    rect rgb(255, 245, 238)
        Note over SRC,RC: NOTIFICATION RECEIPT
        SRC->>RC: Manufacturer mail / ECRI alert / FDA database
        RC->>RC: Log receipt date and details
    end

    rect rgb(240, 248, 255)
        Note over RC: INITIAL ASSESSMENT
        RC->>RC: Review recall classification
        alt Class I
            Note over RC: Immediate Response < 24 hrs
        else Class II
            Note over RC: Standard Response 1-7 days
        else Class III
            Note over RC: Routine Response as able
        end
        RC->>RC: Determine affected departments
    end

    rect rgb(240, 255, 240)
        Note over RC,INV: INVENTORY ASSESSMENT
        RC->>INV: Search inventory management system
        RC->>INV: Search equipment management system
        RC->>INV: Search implant registry
        INV-->>RC: Match lot/serial numbers
        alt Affected Products Found
            RC->>DEPT: Proceed to quarantine
        else No Affected Products
            RC->>RC: Document "Not Affected" & Close
        end
    end

    rect rgb(255, 250, 205)
        Note over RC,DEPT: QUARANTINE & REMOVAL
        RC->>DEPT: Remove from active use
        DEPT->>DEPT: Tag as RECALLED - DO NOT USE
        DEPT->>DEPT: Segregate in designated area
        RC->>INV: Block in purchasing system
    end

    rect rgb(255, 240, 245)
        Note over RC,MFR: CORRECTIVE ACTION
        alt Return to Manufacturer
            DEPT->>MFR: Package and ship with RMA
        else On-Site Correction
            DEPT->>DEPT: Apply fix/update/relabel
        else Destroy/Dispose
            DEPT->>DEPT: Follow destruction protocol
        end
    end

    rect rgb(248, 240, 255)
        Note over RC,MFR: DOCUMENTATION & CLOSURE
        RC->>RC: Complete all documentation
        RC->>MFR: Submit manufacturer response form
        RC->>RC: Verification checklist
        RC->>RC: Close recall in tracking system
    end
```

### Flowchart: Hospital Recall Decision Tree

```mermaid
flowchart TD
    subgraph Receipt["1. NOTIFICATION RECEIPT"]
        A1[Manufacturer Direct Mail] --> B[Recall Coordinator<br/>Receives Notice]
        A2[Third-party Alert Service] --> B
        A3[FDA Website/Database] --> B
    end

    subgraph Assessment["2. INITIAL ASSESSMENT"]
        B --> C{Review Recall<br/>Classification}
        C -->|Class I| D1[Immediate Response<br/>< 24 hours]
        C -->|Class II| D2[Standard Response<br/>1-7 days]
        C -->|Class III| D3[Routine Response<br/>As able]
        D1 --> E[Determine Affected<br/>Departments]
        D2 --> E
        D3 --> E
    end

    subgraph Inventory["3. INVENTORY ASSESSMENT"]
        E --> F[Search Systems]
        F --> F1[Inventory Mgmt<br/>Consumables]
        F --> F2[Equipment Mgmt<br/>Capital Equip]
        F --> F3[Implant Registry<br/>If Applicable]
        F1 --> G[Match lot/serial #s<br/>to recall notice]
        F2 --> G
        F3 --> G
        G --> H{Affected<br/>Products?}
        H -->|No| I[Document Not Affected<br/>& Close]
        H -->|Yes| J[Continue to Quarantine]
    end

    subgraph Quarantine["4. QUARANTINE & REMOVAL"]
        J --> K1[Pull from shelves/storage]
        J --> K2[Tag RECALLED - DO NOT USE]
        J --> K3[Segregate in designated area]
        J --> K4[Block in purchasing system]
        K1 --> L{Device Type?}
        K2 --> L
        K3 --> L
        K4 --> L
    end

    subgraph PatientID["5. PATIENT IDENTIFICATION"]
        L -->|Non-Implantable| M[Skip to Corrective Action]
        L -->|Implantable| N[Cross-reference:<br/>Surgical records, Implant registry,<br/>EHR, Device tracking]
        N --> O[Generate affected patient list]
        O --> P[See: 03-implantable-device-workflow.md]
        P --> M
    end

    subgraph Corrective["6. CORRECTIVE ACTION"]
        M --> Q{Action Type?}
        Q -->|Return| R1[Package per instructions<br/>Obtain RMA #<br/>Ship & track]
        Q -->|On-Site Fix| R2[Apply software update<br/>Install fix<br/>Re-label product]
        Q -->|Destroy| R3[Follow destruction protocol<br/>Document disposal<br/>Obtain certificates]
        R1 --> S
        R2 --> S
        R3 --> S
    end

    subgraph Closure["7. DOCUMENTATION & CLOSURE"]
        S[Complete Documentation] --> T[Submit Manufacturer Response]
        T --> U{Verification<br/>Checklist}
        U --> V[Recall Closed in<br/>Tracking System]
    end

    style D1 fill:#ff6b6b,color:#fff
    style D2 fill:#ffd93d,color:#000
    style D3 fill:#6bcb77,color:#fff
    style I fill:#90EE90
    style V fill:#90EE90
```

## Response Timeline Guidelines

| Recall Class | Initial Response | Investigation | Completion |
|-------------|------------------|---------------|------------|
| **Class I** | Same day | 24-48 hours | ASAP |
| **Class II** | 1-2 days | 1 week | 2-4 weeks |
| **Class III** | 3-5 days | 2 weeks | As able |

## Common Challenges

| Challenge | Mitigation |
|-----------|-----------|
| **Multiple systems to search** | Implement unified recall management software |
| **Incomplete inventory data** | Enforce UDI scanning at receipt/use |
| **Decentralized receipt of notices** | Centralize to single recall coordinator |
| **Late manufacturer notifications** | Subscribe to third-party alert services |
| **Staff awareness** | Regular recall training, visible alerts |

## Compliance Requirements

### Joint Commission (EC.02.01.01 EP 11)
- Written procedure for monitoring hazard notices/recalls
- Designated responsible person
- Coordination across departments
- Documentation of actions taken

### CMS Conditions of Participation
- Maintain safe environment
- Report adverse events
- Respond to known hazards

## Sources

- [24x7 Magazine: Effectively Managing Recalls](https://24x7mag.com/standards/regulations/effectively-managing-recalls/)
- [ECRI Automated Recall Management](https://home.ecri.org/pages/ecri-alerts-workflow-automated-recall-management-software)
- [Remington Medical: What to Do After a Recall](https://remmed.com/what-to-do-if-a-medical-device-is-recalled/)
