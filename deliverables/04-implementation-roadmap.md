# RecallWire Pricing Implementation Roadmap

## Overview

This roadmap outlines the key milestones and activities required to implement RecallWire's new 4-tier pricing structure. The focus is on sequencing dependencies, not timelines - scheduling decisions should be made based on team capacity and business priorities.

---

## Phase 1: Foundation

**Objective:** Establish the infrastructure and internal alignment needed before external launch.

### Milestone 1.1: Internal Alignment

**Activities:**
- [ ] Executive sign-off on 4-tier pricing structure
- [ ] Finalize feature-to-tier mapping with product team
- [ ] Align sales team on new positioning and competitive differentiation
- [ ] Define success metrics for each tier (activation, retention, expansion)
- [ ] Establish pricing governance (who can discount, escalation paths)

**Dependencies:** None (starting point)

**Outputs:**
- Approved pricing matrix
- Internal pricing playbook
- Sales enablement materials draft

---

### Milestone 1.2: Product Readiness

**Activities:**
- [ ] Implement feature gating/entitlements system
- [ ] Build tier-based access controls
- [ ] Create self-service onboarding flow for Starter tier
- [ ] Develop in-app upgrade prompts
- [ ] Configure billing system for 4 tiers + annual discount
- [ ] Test tier transitions (upgrade/downgrade paths)

**Dependencies:** Milestone 1.1 (approved tier structure)

**Outputs:**
- Functional feature gating
- Self-service signup flow
- Billing configuration
- QA test results

---

### Milestone 1.3: Operations Readiness

**Activities:**
- [ ] Define support SLAs by tier
- [ ] Configure help desk with tier-based routing
- [ ] Create tier-specific onboarding playbooks
- [ ] Train support team on tier differences
- [ ] Establish CSM coverage model (dedicated vs. shared)
- [ ] Build self-service help center content

**Dependencies:** Milestone 1.1 (approved tier structure)

**Outputs:**
- Support SLA documentation
- Tiered support workflows
- Help center articles
- Trained support team

---

## Phase 2: Go-to-Market Preparation

**Objective:** Prepare all customer-facing materials and systems for launch.

### Milestone 2.1: Marketing & Messaging

**Activities:**
- [ ] Develop tier-specific value propositions
- [ ] Create pricing page copy and design
- [ ] Build comparison table for website
- [ ] Develop tier-specific landing pages
- [ ] Create case studies/testimonials by segment
- [ ] Prepare launch announcement content
- [ ] Update all sales collateral

**Dependencies:** Milestone 1.1 (approved pricing)

**Outputs:**
- New pricing page (ready to deploy)
- Updated sales deck
- Segment-specific collateral
- Launch announcement draft

---

### Milestone 2.2: Sales Enablement

**Activities:**
- [ ] Create competitive battle cards (vs. OneRecall, ECRI, PAR)
- [ ] Develop objection handling guides
- [ ] Build ROI calculator tool
- [ ] Create demo scripts by tier
- [ ] Train sales team on new pricing
- [ ] Establish trial-to-paid conversion process
- [ ] Define enterprise negotiation guardrails

**Dependencies:** Milestone 2.1 (messaging complete)

**Outputs:**
- Sales playbook
- Battle cards
- ROI calculator
- Trained sales team

---

### Milestone 2.3: Technical Infrastructure

**Activities:**
- [ ] Implement trial experience for Starter tier
- [ ] Build in-app billing/upgrade flows
- [ ] Configure analytics for tier tracking
- [ ] Set up conversion tracking and attribution
- [ ] Test credit card payment processing
- [ ] Implement usage-based metering (if applicable)

**Dependencies:** Milestone 1.2 (product readiness)

**Outputs:**
- Functional trial flow
- Self-service billing
- Analytics dashboards

---

## Phase 3: Soft Launch

**Objective:** Validate pricing with new customers before broad announcement.

### Milestone 3.1: New Customer Launch

**Activities:**
- [ ] Deploy new pricing page
- [ ] Enable self-service signup for Starter tier
- [ ] Begin selling new tiers to inbound leads
- [ ] Monitor conversion rates by tier
- [ ] Collect feedback from early customers
- [ ] Iterate on onboarding based on feedback

**Dependencies:** Phase 2 complete

**Outputs:**
- Live pricing page
- Initial conversion data
- Customer feedback log
- Iteration backlog

---

### Milestone 3.2: Metrics & Optimization

**Activities:**
- [ ] Track trial-to-paid conversion (Starter)
- [ ] Monitor demo-to-close rates (Professional, Business)
- [ ] Analyze tier distribution of new signups
- [ ] Identify friction points in self-service flow
- [ ] A/B test pricing page elements
- [ ] Refine support workflows based on volume

**Dependencies:** Milestone 3.1 (data collection period)

**Outputs:**
- Conversion benchmarks
- Optimization recommendations
- Updated processes

---

## Phase 4: Existing Customer Migration

**Objective:** Transition existing customers to new pricing structure.

### Milestone 4.1: Migration Strategy

**Activities:**
- [ ] Segment existing customers by current contract terms
- [ ] Map each customer to appropriate new tier
- [ ] Identify accounts requiring special handling (enterprise, strategic)
- [ ] Develop migration communication templates
- [ ] Establish grandfather/legacy policies
- [ ] Create account-specific migration plans for enterprise

**Dependencies:** Phase 3 metrics (validated pricing works)

**Outputs:**
- Customer segmentation analysis
- Migration plan by segment
- Communication templates
- Policy documentation

---

### Milestone 4.2: Migration Execution

**Activities:**
- [ ] Communicate changes to customers (with appropriate notice)
- [ ] Execute self-service migrations for SMB
- [ ] Conduct 1:1 discussions with enterprise accounts
- [ ] Handle renewals on new pricing
- [ ] Monitor churn and customer feedback
- [ ] Address escalations and exceptions

**Dependencies:** Milestone 4.1 (migration strategy)

**Outputs:**
- Migrated customer base
- Churn analysis
- Lessons learned

---

## Phase 5: Scale & Optimize

**Objective:** Refine pricing based on market feedback and scale successful motions.

### Milestone 5.1: Performance Analysis

**Activities:**
- [ ] Analyze revenue by tier
- [ ] Calculate CAC and LTV by tier
- [ ] Identify highest-performing acquisition channels by segment
- [ ] Assess feature gate effectiveness
- [ ] Review competitive win/loss data
- [ ] Gather customer satisfaction data by tier

**Dependencies:** 3-6 months of data post-launch

**Outputs:**
- Tier economics analysis
- Channel effectiveness report
- Competitive intelligence update

---

### Milestone 5.2: Iteration & Expansion

**Activities:**
- [ ] Adjust pricing based on market feedback (if needed)
- [ ] Introduce add-on modules based on demand
- [ ] Expand self-service capabilities
- [ ] Consider geographic pricing variations
- [ ] Evaluate new tier opportunities (e.g., Free trial tier)
- [ ] Explore partner/reseller pricing

**Dependencies:** Milestone 5.1 (performance data)

**Outputs:**
- Pricing adjustments
- Add-on module launches
- Expanded product offerings

---

## Key Decision Points

Throughout implementation, the following decisions will need to be made:

| Decision | When | Owner | Options |
|----------|------|-------|---------|
| **Grandfather policy** | Before migration | Executive | Full grandfather / Time-limited / Price increase cap |
| **Trial length** | Before soft launch | Product | 7-day / 14-day / 30-day |
| **Discount authority** | Before launch | Sales Ops | By role / By deal size / Approval workflow |
| **Enterprise floor** | Before launch | Executive | Hard floor vs. negotiable |
| **Add-on priority** | Post-launch | Product | Based on demand signals |
| **Self-service scope** | Before launch | Product | Starter only / Starter + Professional |

---

## Success Metrics by Phase

### Phase 1-2 (Pre-Launch)
- Internal alignment: 100% team training completion
- Product readiness: All feature gates tested
- Operations: Support SLAs documented and configured

### Phase 3 (Soft Launch)
- Starter trial-to-paid conversion: >10%
- Professional demo-to-close: >25%
- Self-service activation (7-day): >60%
- Support ticket volume per Starter customer: <2/month

### Phase 4 (Migration)
- Customer migration completion: >95%
- Churn during migration: <5%
- NPS impact: Neutral or positive

### Phase 5 (Scale)
- Revenue growth: 20%+ YoY
- Starter tier contribution: >15% of new revenue
- Blended CAC payback: <12 months
- Net revenue retention: >110%

---

## Risk Register

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| **Enterprise price resistance** | High | Medium | Grandfathering, value demonstration, phased increases |
| **Self-service support overload** | Medium | Medium | Robust help center, community forums, automation |
| **Tier cannibalization** | High | Low | Clear feature differentiation, value selling |
| **Competitor price response** | Medium | Medium | First-mover advantage, feature differentiation |
| **Internal sales friction** | Medium | Medium | Early involvement, clear incentive alignment |
| **Billing system issues** | High | Low | Thorough testing, staged rollout |

---

## Appendix: Milestone Dependencies Diagram

```
Phase 1: Foundation
├── 1.1 Internal Alignment (START)
├── 1.2 Product Readiness ← 1.1
└── 1.3 Operations Readiness ← 1.1

Phase 2: Go-to-Market Prep
├── 2.1 Marketing & Messaging ← 1.1
├── 2.2 Sales Enablement ← 2.1
└── 2.3 Technical Infrastructure ← 1.2

Phase 3: Soft Launch
├── 3.1 New Customer Launch ← Phase 2 complete
└── 3.2 Metrics & Optimization ← 3.1

Phase 4: Existing Customer Migration
├── 4.1 Migration Strategy ← Phase 3 validated
└── 4.2 Migration Execution ← 4.1

Phase 5: Scale & Optimize
├── 5.1 Performance Analysis ← 3-6 months post-launch
└── 5.2 Iteration & Expansion ← 5.1
```

---

## Summary

This roadmap provides a structured approach to implementing RecallWire's new pricing model:

1. **Foundation first**: Get internal alignment and product/ops ready
2. **Prepare GTM**: Build all customer-facing materials before launch
3. **Soft launch with new customers**: Validate before broad announcement
4. **Migrate carefully**: Handle existing customers with appropriate notice and care
5. **Iterate continuously**: Use data to refine pricing and expand offerings

The sequencing prioritizes risk reduction (validate with new customers before migrating existing) while enabling the business to capture the underserved SMB market opportunity as quickly as capacity allows.
