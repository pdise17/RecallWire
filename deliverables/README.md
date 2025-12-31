# RecallWire Pricing Strategy & Go-to-Market Deliverables

Complete pricing strategy, competitive analysis, and go-to-market materials for RecallWire's multi-tier pricing model.

**Last Updated:** December 2025

---

## Document Overview

| # | Document | Category | Audience | Status |
|---|----------|----------|----------|--------|
| 01 | [Current State Analysis](./01-current-state-analysis.md) | Foundation | Internal | Reference |
| 02 | [Competitive Analysis](./02-competitive-analysis.md) | Foundation | Internal | Active |
| 03 | [Pricing Recommendations](./03-pricing-recommendations.md) | Strategy | Internal | Archived (superseded by 10) |
| 04 | [Implementation Roadmap](./04-implementation-roadmap.md) | Strategy | Internal | Active |
| 06 | [Multi-Dimensional Pricing](./06-multi-dimensional-pricing-model.md) | Strategy | Internal | Reference |
| 08 | [Enhanced Self-Service](./08-enhanced-self-service-strategy.md) | Operations | Internal | Active |
| 09 | [Enterprise Use Case](./09-enterprise-use-case-academic-medical-center.md) | Sales | External | Active |
| 10 | [Pricing One-Pager](./10-pricing-one-pager.md) | Marketing | External | **Current** |
| 11 | [Land & Expand + RMaaS](./11-land-expand-and-rmaas-strategy.md) | Strategy | Internal | Active |
| 12 | [ROI Analysis](./12-roi-analysis-competitive-comparison.md) | Sales | Both | Active |
| 13 | [Per-User Pricing Assessment](./13-per-user-pricing-assessment.md) | Strategy | Internal | Reference (not recommended) |

**Note:** Documents 05 and 07 were consolidated into document 06 during the December 2025 pricing simplification.

---

## Quick Access by Use Case

### For Sales Conversations
| Document | Use When |
|----------|----------|
| [Pricing One-Pager](./10-pricing-one-pager.md) | Sharing pricing with prospects |
| [Enterprise Use Case](./09-enterprise-use-case-academic-medical-center.md) | Selling to large health systems |
| [ROI Analysis](./12-roi-analysis-competitive-comparison.md) | Justifying value vs. competitors or manual |

### For Internal Strategy
| Document | Use When |
|----------|----------|
| [Multi-Dimensional Pricing](./06-multi-dimensional-pricing-model.md) | Understanding full pricing architecture |
| [Land & Expand + RMaaS](./11-land-expand-and-rmaas-strategy.md) | Planning customer growth and RMaaS launch |
| [ROI Analysis](./12-roi-analysis-competitive-comparison.md) | Evaluating deal profitability and competitive positioning |

### For Product/Engineering
| Document | Use When |
|----------|----------|
| [Multi-Dimensional Pricing](./06-multi-dimensional-pricing-model.md) | Implementing feature flags and usage limits |
| [Enhanced Self-Service](./08-enhanced-self-service-strategy.md) | Building self-service capabilities |
| [Implementation Roadmap](./04-implementation-roadmap.md) | Planning technical milestones |

---

## Document Relationships

```
FOUNDATION
│
├── 01-Current State Analysis ─────┐
│   (Product capabilities)         │
│                                  ├──→ 06-Multi-Dimensional Pricing
├── 02-Competitive Analysis ───────┤    (Master pricing architecture)
│   (Market landscape)             │
│                                  │
STRATEGY                           │
│                                  ▼
├── 06-Multi-Dimensional Pricing ──┬──→ 10-Pricing One-Pager (Current)
│   (4 dimensions: Location,       │    (Customer-facing pricing)
│    Tier, Category, Usage)        │
│                                  └──→ 09-Enterprise Use Case
│                                       (Sales document)
│
├── 11-Land & Expand + RMaaS Strategy
│   (Growth mechanics, managed services)
│
OPERATIONS
│
├── 04-Implementation Roadmap
│   (Launch sequence)
│
├── 08-Enhanced Self-Service Strategy
│   (Margin improvement)
│
SALES ENABLEMENT
│
├── 09-Enterprise Use Case ◄─── Uses ROI data
│   (Large health system sales)
│
├── 10-Pricing One-Pager ◄────── SOURCE OF TRUTH
│   (2-tier model: Standard $4,999 / Enterprise $25K+)
│
└── 12-ROI Analysis
    (Value justification, competitive positioning)
```

**Pricing Evolution:**
- 03: Original 4-tier proposal (archived)
- 05, 07: Extended analysis (consolidated into 06)
- 10: **Current 2-tier simplified model**

---

## Detailed Document Summaries

### Foundation Documents

#### [01 - Current State Analysis](./01-current-state-analysis.md)
**Category:** Foundation | **Audience:** Internal

Analyzes RecallWire's current product capabilities, existing tier structure, and the core pricing challenge: bridging an enterprise-grade product ($40k+ value) with SMB market expectations (~$2k/location).

**Key Contents:**
- 6 core platform features with enterprise vs. SMB value mapping
- Current 3-tier structure (Essential, Professional, Enterprise)
- Target industries and market segmentation
- The 20x price differential challenge

**Relationship:** Starting point for all pricing strategy work. Feeds into Pricing Recommendations (03).

---

#### [02 - Competitive Analysis](./02-competitive-analysis.md)
**Category:** Foundation | **Audience:** Internal

Deep dive into the competitive landscape with detailed profiles of major players and pricing intelligence.

**Competitors Covered:**
- Inmar OneRecall (60% market share, enterprise-focused)
- ECRI Alerts (premium, 50+ years expertise)
- PAR Excellence/NotiSphere (budget positioning, acquired Jan 2025)
- TraceLink (partial pricing transparency, DSCSA focus)
- IntelliGuard (RFID niche)

**Key Intelligence:**
- TraceLink actual pricing: $313/user at scale, or $600-800/site
- OneRecall alert breakdown: 7.8% food category (expansion opportunity)
- Market gap: No competitor has transparent public pricing
- PAR Excellence gap: Task-level tracking only, no Recall Action tracking

**Relationship:** Informs Pricing Recommendations (03) and ROI Analysis (12).

---

### Strategy Documents

#### [03 - Pricing Recommendations](./03-pricing-recommendations.md)
**Category:** Strategy | **Audience:** Internal

Original 4-tier pricing proposal with feature segmentation and go-to-market considerations.

**Proposed Tiers:**
| Tier | Price | Locations |
|------|-------|-----------|
| Starter | $149/mo | 1 |
| Professional | $399/mo | 2-5 |
| Business | $799/mo | 6-20 |
| Enterprise | $25k+/yr | 21+ |

**Relationship:** Extended by Pricing Addendum (05) and Multi-Dimensional Pricing (06).

---

#### [04 - Implementation Roadmap](./04-implementation-roadmap.md)
**Category:** Strategy | **Audience:** Internal

5-phase implementation plan for rolling out the new pricing structure.

**Phases:**
1. Foundation (internal alignment, product/ops readiness)
2. Go-to-Market Preparation (marketing, sales enablement)
3. Soft Launch (new customers first)
4. Existing Customer Migration
5. Scale & Optimize

**Relationship:** Execution guide that follows strategy approval.

---

#### [06 - Multi-Dimensional Pricing Model](./06-multi-dimensional-pricing-model.md)
**Category:** Strategy | **Audience:** Internal

**THE MASTER PRICING DOCUMENT** - Comprehensive pricing architecture combining four dimensions.

**The Four Dimensions:**
1. **Locations** - Primary scaling metric (customer-friendly)
2. **Feature Tier** - AI and advanced capabilities gated by tier
3. **Categories** - Industry modules (Medical Devices, Food, Pharma, etc.)
4. **Usage Limits** - Per-tier caps to protect AWS costs (Bedrock, Textract)

**Category Add-Ons:**
| Category | Monthly | Annual |
|----------|---------|--------|
| Food & Dietary | $99 | $999 |
| Pharmaceutical+ | $149 | $1,499 |
| Laboratory | $79 | $799 |
| Radiology/Imaging | $79 | $799 |
| Surgical/OR | $99 | $999 |

**Bundles:**
| Bundle | Monthly | Savings |
|--------|---------|---------|
| Medical Devices (Radiology + Surgical) | $150 | 16% |
| Clinical (Lab + Radiology + Surgical) | $199 | 23% |
| Compliance (Food + Pharma+) | $199 | 20% |
| Healthcare Complete (All 5) | $349 | 31% |

**Relationship:** Central pricing document. Informs Pricing One-Pager (10) and product implementation.

---

#### [11 - Land & Expand + RMaaS Strategy](./11-land-expand-and-rmaas-strategy.md)
**Category:** Strategy | **Audience:** Internal

Comprehensive strategy for customer acquisition, expansion, and managed services.

**Part 1: Land & Expand**
- Entry point: Single Facility Complete at $199/mo (beats PAR Excellence)
- 4-stage expansion framework (Land → Engage → Expand → Enterprise)
- Built-in upsell triggers and mechanisms
- Expansion revenue modeling (2-3x Year 1)

**Part 2: Recall Management as a Service (RMaaS)**

*Market Whitespace:* No competitor offers managed services to healthcare facilities. Managed services exist for manufacturers (IQVIA, Sedgwick) but not for the receiving end.

| RMaaS Tier | Monthly | What's Included |
|------------|---------|-----------------|
| Essentials | $499 | Daily triage, weekly reports, quarterly reviews |
| Core | $999 | + Active response management, monthly calls |
| Complete | $2,499 | + Dedicated specialist, vendor comms, audit support |

**Key Insight:** RMaaS customers have 3-5x higher LTV than software-only customers.

**Relationship:** Extends pricing strategy with growth and services components.

---

### Operations Document

#### [08 - Enhanced Self-Service Strategy](./08-enhanced-self-service-strategy.md)
**Category:** Operations | **Audience:** Internal

Strategy for improving margins at lower tiers through self-service support capabilities.

**Components:**
- RecallWire Assistant (AI-powered help)
- Interactive Help Center (50+ articles, video library)
- In-App Guidance System
- Community Forum (Professional+ tiers)
- Smart Escalation (AI-to-human handoff)
- Proactive Health Monitoring

**Financial Impact:**
| Metric | Before | After |
|--------|--------|-------|
| Annual support cost (350 customers) | $150,000 | $65,000 |
| Savings | - | $85,000/yr |

**Relationship:** Margin improvement initiative for lower tiers.

---

### Customer-Facing Documents

#### [09 - Enterprise Use Case: Academic Medical Center](./09-enterprise-use-case-academic-medical-center.md)
**Category:** Sales | **Audience:** External (Enterprise Prospects)

Sales-ready document for large academic medical center prospects (Mount Sinai profile).

**Use For:**
- Enterprise sales conversations
- RFP responses
- Executive presentations

**Key Elements:**
- Pain point narrative (alert overload, fragmented response, audit anxiety)
- Solution mapping with visual examples
- ROI analysis (747% ROI, $317k annual savings)
- Implementation timeline (12 weeks)
- Competitive positioning
- Proposal summary ($42,500/year)

**Relationship:** Uses data from Enterprise Pricing (07) and ROI Analysis (12).

---

#### [10 - Pricing One-Pager](./10-pricing-one-pager.md)
**Category:** Marketing | **Audience:** External (All Prospects)

Customer-facing pricing page content ready for website or PDF collateral.

**Contents:**
- Single Facility Complete package ($199/mo) - featured entry point
- Four-tier comparison table (Starter → Enterprise)
- Feature matrix
- Category add-ons and bundles
- RMaaS tiers and add-on services
- FAQ section
- CTAs for trial, demo, and enterprise

**Relationship:** Customer-facing version of Multi-Dimensional Pricing (06).

---

#### [12 - ROI Analysis & Competitive Comparison](./12-roi-analysis-competitive-comparison.md)
**Category:** Sales | **Audience:** Internal + External

Data-driven ROI analysis with competitive positioning and objection handling.

**Comparisons:**
- RecallWire vs. Manual (spreadsheets, paper, email)
- RecallWire vs. PAR Excellence (budget competitor)
- RecallWire vs. OneRecall/ECRI (enterprise competitors)

**Key Data Points:**
- TraceLink: 40% admin time reduction, 47% fewer shelf walks
- 70+ site system: 21,000+ hours/year saved
- CMS penalties: Up to $883,000+
- Medical device lawsuits: $1M-26M+ settlements

**Critical Insight - PAR Excellence Gap:**

PAR Excellence tracks at the **task level** (acknowledgement), but NOT at the **Recall Action level** (quarantine, return, destroy, correct). Per FDA 21 CFR Part 806/810, healthcare facilities must document the disposition of recalled devices—not just that they received notice.

| Level | PAR Excellence | RecallWire |
|-------|----------------|------------|
| Task (received, acknowledged) | ✓ | ✓ |
| Recall Action (quarantine) | ✗ | ✓ |
| Recall Action (return) | ✗ | ✓ |
| Recall Action (destroy) | ✗ | ✓ |
| Recall Action (correct) | ✗ | ✓ |
| Disposition documentation | ✗ | ✓ |

**ROI Examples:**
| Scenario | RecallWire Cost | Annual Savings | ROI | Payback |
|----------|-----------------|----------------|-----|---------|
| Single facility | $2,388/yr | $38,700 | 1,521% | 23 days |
| 15 locations | $9,588/yr | $179,400 | 1,770% | 20 days |
| 50+ locations | $42,500/yr | $252,500 | 673% | 2 months |

**Relationship:** Uses competitive data from (02), pricing from (06/07), supports sales with (09).

---

## Pricing Summary (Current 2-Tier Model)

### Core Tiers
| Tier | Annual | Locations | Features |
|------|--------|-----------|----------|
| **Standard** | $4,999/year | 1-5 | Full recall lifecycle, AI assistant, audit documentation |
| **Enterprise** | Starting at $25,000/year | 6+ | Multi-facility coordination, custom integrations, dedicated success |

### Category Add-Ons
| Category | Monthly | Annual |
|----------|---------|--------|
| Food & Dietary | $99 | $999 |
| Pharmaceutical+ | $149 | $1,499 |
| Laboratory | $79 | $799 |
| Radiology/Imaging | $79 | $799 |
| Surgical/OR | $99 | $999 |
| **Medical Devices Bundle** | $150 | $1,499 |
| **Healthcare Complete Bundle** | $349 | $3,499 |

### RMaaS (Managed Services)
| Tier | Monthly | Description |
|------|---------|-------------|
| RMaaS Essentials | $499 | Daily triage, weekly reports, quarterly reviews |
| RMaaS Core | $999 | + Active response management, monthly calls |
| RMaaS Complete | $2,499 | + Dedicated specialist, vendor comms, audit support |

---

## Key Strategic Decisions

| Decision | Current Approach | Rationale |
|----------|------------------|-----------|
| Pricing model | 2-tier (Standard/Enterprise) | Simplified buyer journey, clear upgrade path |
| Standard tier | $4,999/year (1-5 locations) | Competitive with PAR, accessible entry |
| Enterprise tier | $25,000+ (6+ locations) | Undercuts OneRecall/ECRI significantly |
| Category modules | Add-on model ($799-$1,499/yr) | Enables expansion without base complexity |
| Managed services | RMaaS offering ($499-$2,499/mo) | Unique differentiator, no competitor offers this |
| Pricing transparency | Published rates | Differentiator vs. "contact sales" competitors |

---

## Research Sources

- [Kyle Poyar / Growth Unhinged - 2025 State of B2B Monetization](https://www.growthunhinged.com/p/2025-state-of-b2b-monetization)
- [High Alpha / OpenView - 2024 SaaS Benchmarks Report](https://www.highalpha.com/2024-saas-benchmarks-report)
- [Software Advice - Healthcare Software Pricing Models](https://www.softwareadvice.com/resources/healthcare-software-pricing-models/)
- [Cobloom - SaaS Value Metrics](https://www.cobloom.com/blog/how-to-determine-the-best-value-metric-for-your-saas-product)
- [TraceLink - 40% Reduction in Recall Time](https://www.tracelink.com/resources/resource-center/reduce-recall-management-time-by-40-percent)
- [FDA 21 CFR Part 806 - Corrections and Removals](https://www.fda.gov/medical-devices/postmarket-requirements-devices/recalls-corrections-and-removals-devices)
- [FDA 21 CFR Part 810 - Medical Device Recall Authority](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-810)
- Competitor materials (OneRecall, TraceLink, PAR/NotiSphere decks)

---

## Related Documentation

| Folder | Relevance |
|--------|-----------|
| [Sales](../sales/README.md) | Battlecards use pricing/ROI data from here |
| [Creatives](../creatives/README.md) | Design briefs for sales deck, one-pagers |
| [Medical Devices](../medical_devices/README.md) | Market context for competitive positioning |
| [Workflows](../workflows/README.md) | Product capabilities that inform pricing |

### Key Cross-References
- Competitive analysis (02) → Sales battlecards
- ROI analysis (12) → Sales deck stats, email campaigns
- Enterprise use case (09) → Direct sales document
- Pricing one-pager (10) → Website, creatives design source

---

## Next Steps

1. **Executive Review** - Approve pricing structure and margins
2. **Product/Engineering** - Implement feature flags, usage metering, tier gating
3. **Sales Enablement** - Train team on new tiers, competitive positioning, RMaaS
4. **Marketing** - Develop pricing page, collateral, launch messaging
5. **RMaaS Pilot** - Launch with 5-10 customers showing need signals
6. **Soft Launch** - New customers on new pricing
7. **Migration Planning** - Strategy for existing customers
