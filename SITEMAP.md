# RecallWire Documentation Sitemap

Visual map of all documentation and relationships.

---

## Repository Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        biz-recallwire/                                  │
│                                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │ deliverables│  │medical_devices│ │  workflows  │  │    sales    │    │
│  │  (10 docs)  │  │   (7 docs)  │  │  (6 docs)   │  │  (4 docs)   │    │
│  │             │  │             │  │             │  │             │    │
│  │  Pricing    │  │   Market    │  │   Recall    │  │ Battlecards │    │
│  │  Strategy   │  │   Intel     │  │  Processes  │  │  Campaigns  │    │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘    │
│         │                │                │                │           │
│         └────────────────┼────────────────┼────────────────┘           │
│                          │                │                            │
│                          ▼                ▼                            │
│                   ┌─────────────────────────────┐                      │
│                   │         creatives           │                      │
│                   │          (8 docs)           │                      │
│                   │                             │                      │
│                   │   Marketing Material Briefs │                      │
│                   │   (Pulls from all folders)  │                      │
│                   └─────────────────────────────┘                      │
│                                                                         │
│  ┌─────────────┐  ┌─────────────┐                                      │
│  │  templates  │  │ CHANGELOG   │                                      │
│  │  (5 docs)   │  │  SITEMAP    │                                      │
│  │             │  │  README     │                                      │
│  │  Starters   │  │             │                                      │
│  └─────────────┘  └─────────────┘                                      │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Document Flow by Use Case

### Sales Conversation
```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ Identify         │     │ Prepare          │     │ Follow Up        │
│ Competitor       │────▶│ Materials        │────▶│ & Close          │
└────────┬─────────┘     └────────┬─────────┘     └────────┬─────────┘
         │                        │                        │
         ▼                        ▼                        ▼
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ sales/           │     │ deliverables/    │     │ creatives/       │
│ battlecard-*.md  │     │ 10-pricing.md    │     │ 05-email.md      │
│                  │     │ 09-enterprise.md │     │ 01-sales-deck.md │
│                  │     │ 12-roi.md        │     │ 02-one-pagers.md │
└──────────────────┘     └──────────────────┘     └──────────────────┘
```

### Marketing Campaign
```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ Get Market       │     │ Create           │     │ Execute          │
│ Context          │────▶│ Content          │────▶│ Campaign         │
└────────┬─────────┘     └────────┬─────────┘     └────────┬─────────┘
         │                        │                        │
         ▼                        ▼                        ▼
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ medical_devices/ │     │ creatives/       │     │ sales/           │
│ 05-competitive   │     │ 00-runbook.md    │     │ campaign-hot-    │
│ deliverables/    │     │ 03-linkedin.md   │     │ recall.md        │
│ 12-roi.md        │     │ 06-movie.md      │     │                  │
└──────────────────┘     └──────────────────┘     └──────────────────┘
```

### Product Planning
```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ Understand       │     │ Define           │     │ Implement        │
│ Market           │────▶│ Pricing          │────▶│ Features         │
└────────┬─────────┘     └────────┬─────────┘     └────────┬─────────┘
         │                        │                        │
         ▼                        ▼                        ▼
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ medical_devices/ │     │ deliverables/    │     │ workflows/       │
│ 03-buyers.md     │     │ 06-pricing.md    │     │ 00-05 (all)      │
│ 04-categories.md │     │ 10-one-pager.md  │     │                  │
│ 06-regulatory.md │     │ 11-land-expand.md│     │                  │
└──────────────────┘     └──────────────────┘     └──────────────────┘
```

---

## Folder Contents

### /deliverables/ (10 documents)

```
deliverables/
├── README.md
├── 01-current-state-analysis.md        [Reference]
├── 02-competitive-analysis.md          [Active]
├── 03-pricing-recommendations.md       [Archived]
├── 04-implementation-roadmap.md        [Active]
├── 06-multi-dimensional-pricing.md     [Reference]
├── 08-enhanced-self-service.md         [Active]
├── 09-enterprise-use-case.md           [Active] ★ Sales doc
├── 10-pricing-one-pager.md             [Current] ★ Source of truth
├── 11-land-expand-rmaas.md             [Active]
├── 12-roi-analysis.md                  [Active] ★ Sales enablement
└── 13-per-user-assessment.md           [Reference]
```

### /medical_devices/ (7 documents)

```
medical_devices/
├── README.md
├── 00-overview.md                      Index & insights
├── 01-top-companies-by-revenue.md      Company rankings
├── 02-vendors-by-recall-count.md       Recall rankings
├── 03-hospital-buyer-landscape.md      GPOs, IDNs, personas
├── 04-device-categories-patterns.md    Category deep-dive
├── 05-competitive-landscape.md         Solution providers
└── 06-regulatory-timeline.md           FDA, EU MDR compliance
```

### /workflows/ (6 documents)

```
workflows/
├── README.md
├── 00-recall-workflow-overview.md      Framework
├── 01-fda-manufacturer-workflow.md     Recall origination
├── 02-hospital-recall-workflow.md      Internal response
├── 03-implantable-device-workflow.md   Patient identification
├── 04-imaging-equipment-workflow.md    Capital equipment
└── 05-surgical-instrument-workflow.md  Sterile processing
```

### /sales/ (4 documents)

```
sales/
├── README.md
├── battlecard-ecri.md                  Premium competitor
├── battlecard-inmar-onerecall.md       Market leader
├── battlecard-par-excellence.md        Budget competitor
└── campaign-hot-recall-outreach.md     Outbound playbook
```

### /creatives/ (8 documents)

```
creatives/
├── README.md
├── 00-launch-runbook.md                ★ START HERE
├── brand-foundation.md                 Colors, fonts, messaging
├── 01-sales-deck.md                    12-slide deck brief
├── 02-one-pagers.md                    3 versions
├── 03-linkedin-social.md               5 content series
├── 04-gif-animations.md                6 GIF concepts
├── 05-email-templates.md               4 email sequences
└── 06-movie-poster-prompts.md          AI image prompts
```

### /templates/ (5 documents)

```
templates/
├── README.md
├── strategy-document.md                For /deliverables/
├── market-research.md                  For /medical_devices/
├── workflow-document.md                For /workflows/
├── battlecard.md                       For /sales/
└── creative-brief.md                   For /creatives/
```

---

## Cross-Reference Matrix

| Document | Used By |
|----------|---------|
| **deliverables/10-pricing** | sales/*, creatives/01, creatives/02 |
| **deliverables/12-roi** | sales/*, creatives/01, creatives/05 |
| **medical_devices/05-competitive** | sales/battlecard-*, deliverables/02 |
| **workflows/*** | deliverables/01, creatives/04 |
| **sales/campaign** | creatives/05-email |

---

## Quick Navigation

| I need to... | Go to... |
|--------------|----------|
| Check current pricing | `deliverables/10-pricing-one-pager.md` |
| Prepare for competitor | `sales/battlecard-*.md` |
| Create marketing materials | `creatives/00-launch-runbook.md` |
| Understand recall processes | `workflows/00-recall-workflow-overview.md` |
| Research market data | `medical_devices/00-overview.md` |
| Add new document | `templates/` |

---

*Sitemap generated December 2025*
