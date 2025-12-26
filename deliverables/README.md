# RecallWire Pricing Strategy & Go-to-Market Deliverables

Complete pricing strategy, competitive analysis, and go-to-market materials for RecallWire's multi-tier pricing model.

**Last Updated:** December 2024

---

## Document Overview

| # | Document | Category | Audience | Description |
|---|----------|----------|----------|-------------|
| 01 | [Current State Analysis](./01-current-state-analysis.md) | Foundation | Internal | Product capabilities and pricing challenge analysis |
| 02 | [Competitive Analysis](./02-competitive-analysis.md) | Foundation | Internal | Market landscape and competitor intelligence |
| 03 | [Pricing Recommendations](./03-pricing-recommendations.md) | Strategy | Internal | Original 4-tier pricing proposal |
| 04 | [Implementation Roadmap](./04-implementation-roadmap.md) | Strategy | Internal | 5-phase launch plan with milestones |
| 05 | [Pricing Addendum](./05-pricing-addendum.md) | Strategy | Internal | Usage-based pricing and industry expansion |
| 06 | [Multi-Dimensional Pricing](./06-multi-dimensional-pricing-model.md) | Strategy | Internal | Complete pricing architecture (4 dimensions) |
| 07 | [Enterprise Pricing & Margins](./07-enterprise-pricing-margins.md) | Finance | Internal | Margin analysis and enterprise tier structure |
| 08 | [Enhanced Self-Service](./08-enhanced-self-service-strategy.md) | Operations | Internal | Self-service strategy for margin improvement |
| 09 | [Enterprise Use Case](./09-enterprise-use-case-academic-medical-center.md) | Sales | External | Sales document for large health systems |
| 10 | [Pricing One-Pager](./10-pricing-one-pager.md) | Marketing | External | Customer-facing pricing page content |
| 11 | [Land & Expand + RMaaS](./11-land-expand-and-rmaas-strategy.md) | Strategy | Internal | Growth strategy and managed services |
| 12 | [ROI Analysis](./12-roi-analysis-competitive-comparison.md) | Sales | Internal/External | ROI calculator and competitive positioning |

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
| [Enterprise Pricing & Margins](./07-enterprise-pricing-margins.md) | Evaluating deal profitability |
| [Land & Expand + RMaaS](./11-land-expand-and-rmaas-strategy.md) | Planning customer growth and RMaaS launch |

### For Product/Engineering
| Document | Use When |
|----------|----------|
| [Multi-Dimensional Pricing](./06-multi-dimensional-pricing-model.md) | Implementing feature flags and usage limits |
| [Enhanced Self-Service](./08-enhanced-self-service-strategy.md) | Building self-service capabilities |
| [Implementation Roadmap](./04-implementation-roadmap.md) | Planning technical milestones |

---

## Document Relationships

```
FOUNDATION (Start Here)
│
├── 01-Current State Analysis
│   └── Feeds into → 03-Pricing Recommendations
│
├── 02-Competitive Analysis
│   └── Feeds into → 03-Pricing Recommendations
│                  → 12-ROI Analysis
│
STRATEGY (Core Decisions)
│
├── 03-Pricing Recommendations (Original 4-tier proposal)
│   └── Extended by → 05-Pricing Addendum (usage-based, industry expansion)
│                   → 06-Multi-Dimensional Pricing (complete architecture)
│
├── 06-Multi-Dimensional Pricing (Master pricing document)
│   ├── Locations + Tiers + Categories + Usage Limits
│   └── Informs → 07-Enterprise Pricing & Margins
│              → 10-Pricing One-Pager
│
├── 07-Enterprise Pricing & Margins
│   └── Informs → 09-Enterprise Use Case
│              → 12-ROI Analysis
│
OPERATIONS & GROWTH
│
├── 04-Implementation Roadmap
│   └── Sequence for launching new pricing
│
├── 08-Enhanced Self-Service Strategy
│   └── Margin improvement for lower tiers
│
├── 11-Land & Expand + RMaaS Strategy
│   ├── Entry pricing: Single Facility Complete ($199/mo)
│   ├── Expansion mechanisms
│   └── RMaaS managed service offering
│
CUSTOMER-FACING
│
├── 09-Enterprise Use Case (Sales)
│   └── For large health system prospects (Mount Sinai profile)
│
├── 10-Pricing One-Pager (Marketing)
│   └── Website/collateral pricing content
│
└── 12-ROI Analysis (Sales/Marketing)
    └── Competitive positioning and value justification
```

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

#### [05 - Pricing Addendum](./05-pricing-addendum.md)
**Category:** Strategy | **Audience:** Internal

Supplemental analysis addressing usage-based pricing for high-volume facilities and food/supply chain industry expansion.

**Topics Covered:**
- Alert volume tiers for enterprise (protects AWS costs)
- Food/supply chain expansion opportunity (7.8% of OneRecall alerts)
- Updated competitive intelligence from new sources

**Relationship:** Extends original Pricing Recommendations (03). Informs Multi-Dimensional Pricing (06).

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

**Relationship:** Central pricing document. Informs Enterprise Pricing (07), Pricing One-Pager (10), and product implementation.

---

#### [07 - Enterprise Pricing & Margins](./07-enterprise-pricing-margins.md)
**Category:** Finance | **Audience:** Internal

Financial analysis of enterprise pricing with margin projections and cost modeling.

**Enterprise Sweet Spot:** $40-45k/year

**Margin Analysis at $42,500:**
- Gross margin: ~50%
- Net margin: ~32%

**Enterprise Tiers:**
| Tier | Annual | Locations | Alerts/yr |
|------|--------|-----------|-----------|
| Enterprise Standard | $40,000 | Up to 50 | 100k |
| Enterprise Plus | $55,000 | Up to 100 | 250k |
| Enterprise Premier | $75,000+ | Unlimited | Unlimited |

**Relationship:** Informs Enterprise Use Case (09) and deal pricing decisions.

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

## Pricing Summary

### Entry Point
| Package | Monthly | Annual | Includes |
|---------|---------|--------|----------|
| **Single Facility Complete** | $199 | $1,999 | 1 location + Medical Devices bundle + AI |

### Core Tiers
| Tier | Monthly | Annual | Locations |
|------|---------|--------|-----------|
| Starter | $149 | $1,499 | 1 |
| Professional | $399 | $3,999 | Up to 5 |
| Business | $799 | $7,999 | Up to 20 |
| Enterprise | Custom | $40,000+ | Unlimited |

### Enterprise Tiers
| Tier | Annual | Locations | AI Queries |
|------|--------|-----------|------------|
| Enterprise Standard | $40,000 | Up to 50 | 2,000/mo |
| Enterprise Plus | $55,000 | Up to 100 | 5,000/mo |
| Enterprise Premier | $75,000+ | Unlimited | Unlimited |

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

| Decision | Recommendation | Rationale |
|----------|----------------|-----------|
| Primary pricing metric | Per-location | Customer comprehension, healthcare industry standard |
| Competitive entry point | $199/mo (Single Facility Complete) | Matches PAR Excellence, includes AI differentiator |
| AI feature gating | Business+ tiers for advanced AI | Protects margins, creates upgrade path |
| Category modules | Add-on model | Enables industry expansion without base complexity |
| Usage limits | Enforced with overages | Protects AWS costs (Bedrock, Textract) |
| Enterprise sweet spot | $40-45k | Undercuts OneRecall/ECRI, healthy margins |
| Managed services | RMaaS offering | Unique differentiator, 3-5x LTV improvement |
| Self-service investment | Prioritize | Critical for lower-tier margin sustainability |

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

## Next Steps

1. **Executive Review** - Approve pricing structure and margins
2. **Product/Engineering** - Implement feature flags, usage metering, tier gating
3. **Sales Enablement** - Train team on new tiers, competitive positioning, RMaaS
4. **Marketing** - Develop pricing page, collateral, launch messaging
5. **RMaaS Pilot** - Launch with 5-10 customers showing need signals
6. **Soft Launch** - New customers on new pricing
7. **Migration Planning** - Strategy for existing customers
