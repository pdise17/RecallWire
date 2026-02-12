# RecallWire Feature-Driven Pricing Model

## Overview

This document enhances the existing 2-tier pricing model (Document 10) with a **feature-progression framework** derived from the RecallWire competitive feature matrix. The model creates clear pricing tiers that **uptick in price as features become more advanced** and critical to completing the full recall workflow — closing every loop from FDA alert to final resolution.

**Design Principle:** Essential features are accessible at lower price points. As customers need to close more loops in the recall lifecycle, they move up tiers that add automation, intelligence, and end-to-end workflow completion capabilities.

---

## Feature Classification: The Recall Lifecycle Ladder

Every feature maps to a stage in the recall lifecycle. Higher stages = more loops closed = higher price tier.

```
STAGE 4: CLOSE EVERY LOOP (Enterprise Complete)
  ┌─────────────────────────────────────────────────────────────┐
  │  Automated Substitute/Replacement                           │
  │  End-to-End Tracking & Data Capture                         │
  │  Completed Forms Returned to Vendor                         │
  │  RFID/Smartphone Integration                                │
  │  Automated FDA Intake → Direct to End Users                 │
  │  Active Directory / Facility-Level Mapping                  │
  │  Org vs Field Statistical Comparisons                       │
  │  Live Product Recall Ticker (Chrome Ext.)                   │
  └───────────────────────────┬─────────────────────────────────┘
                              │
STAGE 3: ACT & RESOLVE (Professional)
  ┌───────────────────────────┴─────────────────────────────────┐
  │  Action Tracking (Quarantine, Destroy, Return, Credit)      │
  │  AI Custom Reporting / Advanced Analytics / Presentations   │
  │  Item Master Integration (Removals, Discontinuations)       │
  │  Email Templates / Scheduling / Auto Follow-ups             │
  │  Open PO Awareness / Purchasing                             │
  │  Direct FDA Feed                                            │
  └───────────────────────────┬─────────────────────────────────┘
                              │
STAGE 2: MATCH & ANALYZE (Standard)
  ┌───────────────────────────┴─────────────────────────────────┐
  │  Scan Purchase & Sales Data vs Affected Part Numbers        │
  │  Scan for Duplicates, SKU Variations, Distributor Crossover │
  │  Scan Sales Order / Purchase Order Data Daily               │
  │  Custom Escalations via Prompt                              │
  │  AI Product Identification Tool                             │
  │  AI Search Capabilities                                     │
  │  Storage & Repository: Audit Compliance (3 years)           │
  └───────────────────────────┬─────────────────────────────────┘
                              │
STAGE 1: DETECT & ALERT (Essentials)
  ┌───────────────────────────┴─────────────────────────────────┐
  │  Daily FDA Processing (Timed)                               │
  │  Early FDA Alerts                                           │
  │  PDF Recall Analyzer                                        │
  │  Directory of Recalls by Part Number                        │
  │  Basic Dashboard & Notifications                            │
  │  Storage & Repository (1 year)                              │
  └─────────────────────────────────────────────────────────────┘
```

---

## MVP Feature List (Launch Priority)

These are the features that must ship for a viable product. All are **built or in active development**.

### MVP Tier 1 — Minimum Viable Product (Essentials)

| # | Feature | Status | Competitive Advantage |
|---|---------|--------|----------------------|
| 1 | Daily FDA Processing (Timed) | Built | **Nobody else does this** |
| 2 | Early FDA Alerts | Built | **Nobody else does this** |
| 3 | PDF Recall Analyzer | Built | **Nobody else does this** |
| 4 | Directory of Recalls by Part Number | Built | **Nobody else does this** |
| 5 | Basic Dashboard & Email Notifications | Built | Table stakes |
| 6 | Storage & Repository (1 year retention) | Built | **Nobody else does this** |

**Value delivered:** Customer *knows* about recalls faster than anyone else in the market.

### MVP Tier 2 — Core Matching & Intelligence (Standard)

| # | Feature | Status | Competitive Advantage |
|---|---------|--------|----------------------|
| 7 | Scan Purchase & Sales Data vs Affected Part Numbers | Built | Partial competition |
| 8 | Scan for Duplicates, SKU Variations, Distributor Crossover PNs | Built | Partial competition |
| 9 | Custom Escalations through Prompt | Built | Partial competition |
| 10 | AI Search Capabilities | Built | Partial competition |
| 11 | Scan Sales Order / Purchase Order Data Daily | Built | **Nobody else does this** |
| 12 | AI Product Identification Tool | Built | **Nobody else does this** |
| 13 | Storage & Repository (3 year retention) | Built | **Nobody else does this** |

**Value delivered:** Customer can *match* recalls to their specific inventory and take informed action.

### MVP Tier 3 — Resolution & Compliance (Professional)

| # | Feature | Status | Competitive Advantage |
|---|---------|--------|----------------------|
| 14 | AI Custom Reporting / Advanced Analytics / Presentations | Built | **Nobody else does this** |
| 15 | Item Master Integration (Removals, Discontinuations) | Built | **Nobody else does this** |
| 16 | Action Tracking (Quarantine, Destroy, Return, Credit) | Roadmap | **Nobody else does this** |
| 17 | Email Templates / Email Scheduling (Auto Follow-ups) | Roadmap | **Nobody else does this** |
| 18 | Open PO Awareness / Purchasing | Coming Soon | **Nobody else does this** |
| 19 | Direct FDA Feed (not screen scrape) | Roadmap | **Nobody else does this** |
| 20 | Storage & Repository (7 year retention) | Built | **Nobody else does this** |

**Value delivered:** Customer can *act on, resolve, and document* recalls with full compliance.

### MVP Tier 4 — Full Loop Closure (Enterprise Complete)

| # | Feature | Status | Competitive Advantage |
|---|---------|--------|----------------------|
| 21 | Active Custom "Live" Product Recall Ticker (Chrome Ext.) | Coming Soon | **Nobody else does this** |
| 22 | Completed Forms Returned to Vendor | Coming Soon | **Nobody else does this** |
| 23 | RFID Scanner / Smartphone Integration | Coming Soon | Partial competition |
| 24 | Automated Substitute / Replacement Capabilities | Coming Soon | **Nobody else does this** |
| 25 | Active Directory Integration | Roadmap | **Nobody else does this** |
| 26 | Facility / Dept. Level Mapping | Roadmap | **Nobody else does this** |
| 27 | Automated Intake from FDA – Direct to Affected End Users | Roadmap | Partial competition |
| 28 | End-to-End Tracking and Data Capture | Roadmap | Partial competition |
| 29 | Insights: Org vs Field Statistical Comparisons | Roadmap | **Nobody else does this** |
| 30 | Unlimited Storage & Repository | Built | **Nobody else does this** |

**Value delivered:** Every loop in the recall lifecycle is closed. Detection through resolution through vendor closure through compliance reporting — fully automated, zero gaps.

---

## Pricing Model: Feature-Driven Tiers

### Published Pricing (Customer-Facing)

The external pricing maintains the simplified 2-tier structure from Document 10, but internally each tier maps to feature stages.

| | Essentials | Standard | Professional | Enterprise Complete |
|--|------------|----------|--------------|---------------------|
| **Annual** | $1,999/yr | $4,999/yr | $12,999/yr | Starting at $25,000/yr |
| **Monthly** | $199/mo | $449/mo | $1,199/mo | Contact Sales |
| **Locations** | 1 | 1-5 | 1-10 | Unlimited |
| **Lifecycle Stage** | Detect & Alert | Match & Analyze | Act & Resolve | Close Every Loop |
| **Best For** | Single clinic, small practice | Multi-site clinics, ASCs | Regional systems, compliance-focused | Health systems, hospital networks |
| | [Start Free Trial] | [Start Free Trial] | [Start Free Trial] | [Contact Sales] |

### Annual Savings (vs Monthly)

| Tier | Monthly Total | Annual Price | You Save |
|------|---------------|-------------|----------|
| Essentials | $2,388/yr | $1,999/yr | $389 (16%) |
| Standard | $5,388/yr | $4,999/yr | $389 (7%) |
| Professional | $14,388/yr | $12,999/yr | $1,389 (10%) |
| Enterprise Complete | Custom | Custom | Negotiated |

---

## Complete Feature Matrix by Tier

### Stage 1: Detection & Awareness

| Feature | Essentials | Standard | Professional | Enterprise |
|---------|:----------:|:--------:|:------------:|:----------:|
| Daily FDA Processing (Timed) | Yes | Yes | Yes | Yes |
| Early FDA Alerts | Yes | Yes | Yes | Yes |
| PDF Recall Analyzer | Yes | Yes | Yes | Yes |
| Directory of Recalls by Part Number | Yes | Yes | Yes | Yes |
| Basic Dashboard | Yes | Yes | Yes | Yes |
| Email Notifications | Yes | Yes | Yes | Yes |

### Stage 2: Matching & Analysis

| Feature | Essentials | Standard | Professional | Enterprise |
|---------|:----------:|:--------:|:------------:|:----------:|
| Scan Purchase & Sales Data vs Affected PNs | — | Yes | Yes | Yes |
| Scan Duplicates, SKU Variations, Distributor Crossover | — | Yes | Yes | Yes |
| Scan Sales Order / PO Data Daily | — | Yes | Yes | Yes |
| Custom Escalations via Prompt | — | Yes | Yes | Yes |
| AI Search Capabilities | Limited | Full | Full | Full |
| AI Product Identification Tool | — | Yes | Yes | Yes |

### Stage 3: Resolution & Compliance

| Feature | Essentials | Standard | Professional | Enterprise |
|---------|:----------:|:--------:|:------------:|:----------:|
| Action Tracking (Quarantine, Destroy, Return, Credit) | — | — | Yes | Yes |
| AI Custom Reporting / Advanced Analytics | — | — | Yes | Yes |
| AI-Powered Presentations | — | — | Yes | Yes |
| Item Master Integration (Removals, Discontinuations) | — | — | Yes | Yes |
| Email Templates / Scheduling / Auto Follow-ups | — | — | Yes | Yes |
| Open PO Awareness / Purchasing | — | — | Yes | Yes |
| Direct FDA Feed (not screen scrape) | — | — | Yes | Yes |

### Stage 4: Full Loop Closure

| Feature | Essentials | Standard | Professional | Enterprise |
|---------|:----------:|:--------:|:------------:|:----------:|
| Live Product Recall Ticker (Chrome Extension) | — | — | — | Yes |
| Completed Forms Returned to Vendor | — | — | — | Yes |
| RFID Scanner / Smartphone Integration | — | — | — | Yes |
| Automated Substitute / Replacement Capabilities | — | — | — | Yes |
| Active Directory Integration | — | — | — | Yes |
| Facility / Dept. Level Mapping | — | — | — | Yes |
| Automated FDA Intake → Direct to End Users | — | — | — | Yes |
| End-to-End Tracking & Data Capture | — | — | — | Yes |
| Insights: Org vs Field Statistical Comparisons | — | — | — | Yes |

### Platform & Support

| Feature | Essentials | Standard | Professional | Enterprise |
|---------|:----------:|:--------:|:------------:|:----------:|
| **Storage / Data Retention** | 1 year | 3 years | 7 years | Unlimited / Custom |
| **AI Assistant Queries** | 100/mo | 500/mo | 2,000/mo | Unlimited |
| **Document Scans** | 100/mo | 500/mo | 2,000/mo | Unlimited |
| **API Access** | Read | Read | Read/Write | Full |
| **SSO** | — | — | — | Yes |
| **Custom Integrations** | — | — | Limited | Unlimited |
| **Users** | 2 | 10 | 25 | Unlimited |
| **Support** | Help Center | Email (24hr) | Email (8hr) + Phone | Dedicated CSM |
| **Implementation** | Self-serve | Self-serve + call | Guided | White-glove |
| **SLA** | — | 99.5% | 99.9% | Custom |

---

## Competitive Positioning by Tier

### Why This Model Wins

| Tier | Competitor Comparison | RecallWire Advantage |
|------|----------------------|---------------------|
| **Essentials ($1,999)** | Below PAR Excellence (~$2,400 est.) | Lower price + FDA-direct features PAR doesn't have |
| **Standard ($4,999)** | 2x PAR but with full matching | Complete AI matching engine vs. notification-only |
| **Professional ($12,999)** | 1/6th of ECRI ($75,878) | Action tracking, analytics, compliance — at a fraction of cost |
| **Enterprise ($25,000+)** | Competitive with Inmar OneRecall | Full loop closure features nobody else offers |

### Feature Exclusivity Summary

| Feature Category | # Features | RecallWire Only | Partial Competition |
|------------------|:----------:|:---------------:|:-------------------:|
| Stage 1: Detect & Alert | 6 | 5 (83%) | 1 |
| Stage 2: Match & Analyze | 6 | 2 (33%) | 4 |
| Stage 3: Act & Resolve | 7 | 6 (86%) | 1 |
| Stage 4: Close Every Loop | 9 | 7 (78%) | 2 |
| **Total** | **28** | **20 (71%)** | **8** |

**71% of features have zero competition.** This justifies premium pricing at higher tiers.

---

## Uptick / Downtick Pricing Logic

### How Price Scales With Feature Value

```
Price    $25K+ ─────────────────────────────────────  Enterprise Complete
  ▲                                                    (28 features)
  │                                                    Close every loop
  │
  │      $12,999 ──────────────────────────────────  Professional
  │                                                    (19 features)
  │                                                    Act & Resolve
  │
  │      $4,999 ───────────────────────────────────  Standard
  │                                                    (12 features)
  │                                                    Match & Analyze
  │
  │      $1,999 ───────────────────────────────────  Essentials
  │                                                    (6 features)
  │                                                    Detect & Alert
  ▼
         Loops Closed ──────────────────────────────►
         (fewer)                               (all)
```

### Downtick: When to Offer Lower Pricing

| Scenario | Action | Resulting Tier |
|----------|--------|---------------|
| Customer only needs alerts (no matching) | Offer Essentials at $1,999 | Saves $3,000 vs Standard |
| Single location, limited budget | Offer Essentials with category add-on | $1,999 + $799 = $2,798 |
| Competitive displacement (from PAR) | Offer Essentials at $1,999, below PAR price | Wins on price + features |
| Pilot / proof of concept | 14-day free trial → Essentials annual | Low-risk entry |

### Uptick: When to Drive Higher Pricing

| Scenario | Trigger | Upgrade Path |
|----------|---------|-------------|
| Customer needs to track recall actions | Action Tracking is Professional+ | Standard → Professional (+$8,000) |
| Customer facing Joint Commission audit | Compliance reporting is Professional+ | Any → Professional |
| Customer managing 6+ locations | Location limit at Professional | Professional → Enterprise |
| Customer wants automated vendor forms | Loop closure is Enterprise only | Professional → Enterprise (+$12,000+) |
| Customer needs RFID/mobile scanning | Enterprise exclusive | Professional → Enterprise |
| Customer wants substitute automation | Enterprise exclusive | Professional → Enterprise |
| Customer wants end-to-end tracking | Enterprise exclusive | Professional → Enterprise |

### The "Complete Workflow" Upgrade Narrative

The most powerful sales lever: **Only Enterprise Complete closes every loop.**

```
Customer Journey Without Enterprise:

  FDA Alert → Match to Inventory → ??? → ??? → ??? → Vendor Resolution
                                    ▲
                                    │
                        GAPS: No action tracking
                              No auto-substitutes
                              No vendor form return
                              No end-to-end tracking
                              No facility mapping


Customer Journey With Enterprise Complete:

  FDA Alert → Match → Action Track → Substitute → Forms to Vendor → Resolved
     ↓           ↓         ↓              ↓              ↓             ↓
   Early      AI Match  Quarantine/   Auto-suggest   Auto-return    Full audit
   Alert      + SKU     Destroy/      replacement    completed      trail +
   (Direct    Crossover Return/       parts          forms to       analytics
    FDA)               Credit                        manufacturer   + insights
```

---

## Enterprise Sub-Tier Pricing (Internal — Not Published)

| Sub-Tier | Locations | Annual Range | All Stage 4 Features |
|----------|-----------|--------------|---------------------|
| Enterprise | 6-35 | $25,000-$45,000 | Yes (phased rollout) |
| Enterprise Plus | 36-100 | $45,000-$75,000 | Yes (full) |
| Enterprise Premier | 100+ | $75,000+ | Yes + custom |

---

## Category Add-Ons (Available on All Tiers)

Unchanged from Document 10. Category add-ons extend recall coverage beyond base medical devices.

| Category | Annual | Monthly |
|----------|--------|---------|
| Food & Dietary | $999/yr | $99/mo |
| Pharmaceutical+ | $1,499/yr | $149/mo |
| Laboratory | $799/yr | $79/mo |
| Radiology/Imaging | $799/yr | $79/mo |
| Surgical/OR | $999/yr | $99/mo |
| **Healthcare Complete (all 5)** | **$3,499/yr** | **$349/mo** |

---

## RMaaS Integration (Available on Standard+)

RMaaS tiers from Document 11 remain unchanged. Availability by software tier:

| RMaaS Tier | Essentials | Standard | Professional | Enterprise |
|------------|:----------:|:--------:|:------------:|:----------:|
| RMaaS Essentials ($499/mo) | — | Yes | Yes | Yes |
| RMaaS Core ($999/mo) | — | Yes | Yes | Yes |
| RMaaS Complete ($2,499/mo) | — | — | Yes | Yes |
| Bundle Discount | — | 10% | 15% | 20% |

---

## Pricing Examples

### Example 1: Small Clinic — Awareness Only

| Component | Price |
|-----------|-------|
| Essentials (1 location) | $1,999/yr |
| **Total** | **$1,999/yr** |

*Loops closed: Detection & Alerting only. Knows about recalls before competitors.*

### Example 2: ASC Network — Full Matching

| Component | Price |
|-----------|-------|
| Standard (4 locations) | $4,999/yr |
| Surgical/OR add-on | $999/yr |
| **Total** | **$5,998/yr** |

*Loops closed: Detection + Matching. Can identify affected inventory across all locations.*

### Example 3: Regional Hospital — Compliance Focused

| Component | Price |
|-----------|-------|
| Professional (8 locations) | $12,999/yr |
| Healthcare Complete bundle | $3,499/yr |
| RMaaS Essentials (15% off) | $5,089/yr |
| **Total** | **$21,587/yr** |

*Loops closed: Detection + Matching + Resolution + Compliance. Action tracking, auto follow-ups, full analytics. Audit-ready.*

### Example 4: Health System — Every Loop Closed

| Component | Price |
|-----------|-------|
| Enterprise Complete (25 locations) | $35,000/yr |
| Healthcare Complete bundle | Included |
| RMaaS Core (20% off) | $9,590/yr |
| **Total** | **$44,590/yr** |

*Loops closed: ALL. End-to-end from FDA alert to vendor form return. Automated substitutes, facility mapping, RFID verification, full insights.*

### Example 5: National Health System — Full Suite

| Component | Price |
|-----------|-------|
| Enterprise Premier (120 locations) | $85,000/yr |
| All categories included | Included |
| RMaaS Complete (20% off) | $23,990/yr |
| Implementation | $15,000 one-time |
| **Total** | **$108,990/yr + $15,000 implementation** |

*Every loop closed at enterprise scale. Dedicated team, custom SLAs, unlimited everything.*

---

## Revenue Impact: 4-Tier vs 2-Tier

### New Revenue Opportunity: Essentials Tier

The Essentials tier at $1,999 captures customers who previously couldn't afford Standard ($4,999):

| Metric | 2-Tier Model | 4-Tier Model | Delta |
|--------|-------------|-------------|-------|
| Addressable market (facilities) | ~2,500 | ~4,000+ | +60% |
| Avg deal size (blended) | $15,000 | $12,000 | -20% |
| Total customers Y1 | 60 | 100+ | +67% |
| Y1 ARR (conservative) | $600K | $750K+ | +25% |

### Upgrade Revenue (Land & Expand)

| Upgrade Path | Price Delta | Expansion Multiplier |
|--------------|------------|---------------------|
| Essentials → Standard | +$3,000 | 2.5x |
| Essentials → Professional | +$11,000 | 6.5x |
| Standard → Professional | +$8,000 | 2.6x |
| Professional → Enterprise | +$12,000+ | 1.9x+ |
| Any tier + RMaaS | +$6,000-$30,000 | 2-4x |

---

## Implementation Strategy

### Phase 1: Launch with 3 Tiers (Now)

Publish **Essentials + Standard + Enterprise** (maintains simplicity from Document 10 while adding the entry-level tier).

- Essentials captures budget-conscious buyers and displaces PAR on price
- Standard remains the core offering with full matching
- Enterprise remains sales-led with full loop closure

### Phase 2: Introduce Professional (When Stage 3 features ship)

Once Action Tracking, Email Templates, and Direct FDA Feed ship:

- Introduce Professional tier at $12,999
- Move Action Tracking, Advanced Analytics, Item Master Integration behind Professional gate
- Standard customers who need these features have a clear upgrade path

### Phase 3: Full 4-Tier Model (When Stage 4 features ship)

Once Chrome Extension, RFID, Automated Substitutes, and End-to-End Tracking ship:

- These features are Enterprise-exclusive
- The "close every loop" narrative becomes the Enterprise sales driver
- Professional customers who need full automation upgrade to Enterprise

---

## Relationship to Existing Documents

| Document | Relationship |
|----------|-------------|
| **10-pricing-one-pager.md** | This document enhances but does not replace Doc 10. The 2-tier published model can evolve to 3-tier (Phase 1) then 4-tier (Phase 3). |
| **06-multi-dimensional-pricing-model.md** | Feature stages align with the multi-dimensional framework. This adds the lifecycle ladder concept. |
| **11-land-expand-and-rmaas-strategy.md** | RMaaS strategy unchanged. This document adds tier-based RMaaS availability (Standard+ for Essentials/Core, Professional+ for Complete). |
| **03-pricing-recommendations.md** | The original 4-tier model is partially revived here but with feature-lifecycle logic rather than location-based tiers. |

---

## Key Decisions Summary

| Decision | Outcome | Rationale |
|----------|---------|-----------|
| Number of tiers | 4 (Essentials, Standard, Professional, Enterprise) | Maps to recall lifecycle stages |
| Essentials price | $1,999/yr | Undercuts PAR Excellence, captures budget market |
| Standard price | $4,999/yr (unchanged) | Maintains current positioning |
| Professional price | $12,999/yr | Bridges gap between Standard and Enterprise |
| Enterprise price | $25,000+/yr (unchanged) | Full loop closure justifies premium |
| Feature gating logic | By lifecycle stage, not by location count | Features drive value, not just scale |
| Phased rollout | 3 phases aligned to feature shipping | Don't sell what isn't built yet |
| Loop-closure narrative | Enterprise only | Creates urgency for highest-value customers |

---

*Document created: February 2026*
*Builds on: Document 10 (Pricing One-Pager), Document 06 (Multi-Dimensional Model), Document 11 (Land & Expand)*
*Incorporates: RecallWire vs Competition Feature Matrix (February 2026)*
