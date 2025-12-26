# Recall Workflows

Documentation of medical device recall workflows from FDA initiation through hospital response and closure.

**Last Updated:** December 2025

---

## Overview

Medical device recalls do **not** follow a single unified workflow. The process varies based on:

1. **Recall Classification** (Class I, II, III) - Determines urgency and reporting
2. **Device Type** - Implantable vs. capital equipment vs. consumables
3. **Device Category** - Imaging, surgical, cardiac, etc.

See [00-recall-workflow-overview.md](./00-recall-workflow-overview.md) for the complete framework.

---

## Documents

| # | Document | Description |
|---|----------|-------------|
| 00 | [Recall Workflow Overview](./00-recall-workflow-overview.md) | Framework for understanding recall variations; universal 5-phase workflow |
| 01 | [FDA & Manufacturer Workflow](./01-fda-manufacturer-workflow.md) | How recalls originate: manufacturer discovery, FDA notification, classification |
| 02 | [Hospital Recall Workflow](./02-hospital-recall-workflow.md) | Internal hospital response: receipt, assessment, quarantine, resolution |
| 03 | [Implantable Device Workflow](./03-implantable-device-workflow.md) | Patient identification, surgeon notification, explant decisions |
| 04 | [Imaging Equipment Workflow](./04-imaging-equipment-workflow.md) | Radiology/capital equipment: service coordination, downtime management |
| 05 | [Surgical Instrument Workflow](./05-surgical-instrument-workflow.md) | Sterile processing, instrument tracking, case log review |

---

## Quick Reference

### Recall Classifications

| Class | Risk Level | Example | Response Time |
|-------|------------|---------|---------------|
| **I** | Life-threatening | Pacemaker failure | Immediate |
| **II** | Temporary/reversible harm | Labeling error on syringe | Prompt |
| **III** | Unlikely to cause harm | Documentation issue | Standard |

### Workflow by Device Type

| Device Type | Primary Workflow | Key Consideration |
|-------------|------------------|-------------------|
| Implanted devices | [03-implantable-device-workflow.md](./03-implantable-device-workflow.md) | Patient identification required |
| Imaging/capital equipment | [04-imaging-equipment-workflow.md](./04-imaging-equipment-workflow.md) | Operational continuity |
| Surgical instruments | [05-surgical-instrument-workflow.md](./05-surgical-instrument-workflow.md) | Sterile processing coordination |
| Consumables | [02-hospital-recall-workflow.md](./02-hospital-recall-workflow.md) | Inventory sweep |

---

## Diagram Types

All workflow documents include Mermaid diagrams:

- **Sequence diagrams** - Chronological flow between stakeholders
- **Flowcharts** - Decision trees and process steps
- **Color coding** - Red (Class I), Yellow (Class II), Green (Class III)

---

## Related Documentation

- [Medical Devices: Regulatory Timeline](../medical_devices/06-regulatory-timeline.md) - FDA deadlines and compliance requirements
- [Medical Devices: Device Categories](../medical_devices/04-device-categories-recall-patterns.md) - Recall patterns by device type
