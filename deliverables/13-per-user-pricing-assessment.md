# Per-User Pricing Model Assessment

## Executive Summary

This document provides a data-driven assessment of per-user pricing for RecallWire, informed by market analysis and healthcare buyer preferences.

**Recommendation: Do not adopt per-user pricing.**

Per-user pricing creates sales friction, revenue unpredictability, and administrative overhead without providing meaningful advantages over per-location pricing in the healthcare recall management market.

---

## Part 1: Per-User Pricing Overview

### What is Per-User Pricing?

Per-user (or per-seat) pricing charges customers based on the number of individuals who access the platform. Common in B2B SaaS (Salesforce, Slack, Office 365).

### Per-User Economics Example

```
Base platform cost: ~$18,000-20,000 (estimated)
Per-user variable cost: ~$180-200 (with margin)
Target gross margin: ~50-60% (industry standard SaaS)
```

**Typical volume discount curve:**

| Users | Per-User Rate | Discount from Base |
|-------|---------------|-------------------|
| 50 | $400 | 0% (base) |
| 100 | $380 | -5% |
| 150 | $345 | -14% |
| 200 | $320 | -20% |

---

## Part 2: Arguments For Per-User Pricing

### Potential Advantages

| Advantage | Description | Applicability to RecallWire |
|-----------|-------------|----------------------------|
| **Granular scaling** | Revenue scales precisely with customer size | Medium - locations scale similarly |
| **Land-and-expand** | Easy to add users incrementally | Low - recall mgmt has defined user base |
| **Industry familiarity** | Common in SaaS | Medium - but healthcare prefers site licenses |
| **Usage correlation** | More users = more platform usage | Low - usage driven by recall volume, not users |

### When Per-User Works Well

Per-user pricing is effective when:

1. **User count correlates with value delivered** - e.g., Salesforce (more reps = more CRM value)
2. **Users are the unit of work** - e.g., Slack (more users = more messages)
3. **Customer knows their user count** - e.g., Office 365 (IT knows employee count)
4. **Adding users is frequent** - e.g., growing sales teams

**RecallWire fit assessment:**

| Criterion | Fit | Explanation |
|-----------|-----|-------------|
| User count = value | **Poor** | Value is recall coverage, not user count |
| Users are unit of work | **Poor** | Recalls are the unit of work |
| Customer knows user count | **Poor** | "Who touches recalls?" is ambiguous |
| Frequent user additions | **Poor** | Recall coordinators are stable roles |

---

## Part 3: Arguments Against Per-User Pricing

### 1. Sales Cycle Friction

**The "user count" conversation creates delays:**

| Sales Stage | Per-Location | Per-User |
|-------------|--------------|----------|
| Discovery | "How many facilities?" (known) | "How many users touch recalls?" (unknown) |
| Scoping | Immediate answer | Requires internal research |
| Proposal | Single price | Price range or TBD |
| Negotiation | Location count fixed | User count negotiable |
| Close | Days | Weeks |

**Real-world scenario:**

> **Prospect:** "What's the price for our 8-hospital system?"
>
> **Per-user model:** "How many users?"
>
> **Prospect:** "I don't know... maybe 10-30 people per hospital?"
>
> **Sales:** "So 80-240 users? That's $30K to $90K."
>
> **Prospect:** "Let me figure out the exact count and get back to you."
>
> *[2-4 weeks pass while prospect surveys departments]*

**Estimated impact:** +2-4 weeks to sales cycle, 15-20% deal slippage risk

### 2. Revenue Unpredictability

**User counts fluctuate; locations don't:**

| Scenario | Location Impact | User Impact |
|----------|-----------------|-------------|
| Hospital acquires clinic | +1 location (clear) | +5-20 users (unclear) |
| Department reorganization | None | -10 to +10 users |
| Staff turnover | None | Users churn/replace |
| Budget cuts | Facility closure (rare) | License reduction (common) |
| Seasonal staffing | None | Travel nurses, temps |

**Revenue recognition challenges:**

| Issue | Description | Financial Impact |
|-------|-------------|------------------|
| True-up complexity | Annual reconciliation of actual vs. licensed users | AR delays, disputes |
| Shelfware pressure | Customers pressure to reduce unused licenses | Downward price pressure |
| Audit requirements | Need to verify user counts | Operational overhead |

### 3. Definition Ambiguity

**"Who is a user?" creates disputes:**

| Role | Full User? | Read-Only? | No License? |
|------|------------|------------|-------------|
| Recall Coordinator | Yes | — | — |
| Department Manager (reviews dashboards) | ? | ? | ? |
| Compliance Officer (runs reports) | ? | ? | ? |
| Nurse Manager (receives alerts) | ? | ? | ? |
| Executive (quarterly reviews) | ? | ? | ? |
| Auditor (annual access) | ? | ? | ? |

**Industry comparison:**

| Vendor | User Definition | Clarity |
|--------|-----------------|---------|
| Salesforce | Named user with login | High |
| Slack | Active user (message sent) | Medium |
| ECRI | Membership (unlimited users) | High |
| OneRecall | Site license (unlimited) | High |

**Key insight:** ECRI and OneRecall—the market leaders—don't use per-user pricing. They use site/membership models.

### 4. Healthcare Buyer Preference

**Healthcare organizations prefer site licenses:**

| Procurement Model | Healthcare Familiarity | Examples |
|-------------------|----------------------|----------|
| Per-bed | Very High | EHR, clinical systems |
| Per-facility | Very High | Most healthcare IT |
| Per-user | Medium | Back-office SaaS |
| Usage-based | Low | Emerging |

**Buyer psychology:**

| Per-Location | Per-User |
|--------------|----------|
| "We have 8 hospitals, so $X" | "How many people is that?" |
| Predictable budgeting | Variable budgeting |
| No license management | License compliance burden |
| IT-friendly | IT headache |

### 5. Competitive Disadvantage

**Primary recall management competitors don't use per-user:**

| Competitor | Model | User Pricing |
|------------|-------|--------------|
| ECRI | Membership | Unlimited users included |
| OneRecall (Inmar) | Enterprise/site | Unlimited users included |
| PAR/NotiSphere | SaaS flat | Unlimited users included |

**Positioning risk:**

If RecallWire adopts per-user while ECRI/OneRecall offer unlimited users:

> **Prospect:** "ECRI includes unlimited users for $76K. Why does RecallWire charge per user?"
>
> **Sales:** "Our model scales with your organization..."
>
> **Prospect:** "But I don't want to manage licenses. ECRI doesn't make me do that."

### 6. Operational Overhead

**Per-user requires infrastructure:**

| Requirement | Description | Cost |
|-------------|-------------|------|
| License management UI | Customer portal to manage seats | Dev time |
| Usage tracking | Monitor active vs. licensed users | Infrastructure |
| True-up billing | Annual reconciliation workflow | Finance ops |
| Compliance auditing | Verify customer isn't over-licensed | Legal/sales |
| Overage processing | Handle mid-cycle additions | Billing complexity |

**Estimated operational overhead:** $50-100K/year in systems and headcount for a per-user model at scale.

---

## Part 4: Hybrid Approaches Considered

### Option A: Per-User for Enterprise Only

| Tier | Model |
|------|-------|
| Standard | Per-location |
| Enterprise | Per-user |

**Pros:** Captures enterprise granularity
**Cons:** Confusing model transition, still has enterprise sales friction

**Verdict:** Not recommended

### Option B: User Bands (Not Pure Per-User)

| Band | Users Included | Price |
|------|----------------|-------|
| Small | Up to 50 | $35,000 |
| Medium | Up to 150 | $50,000 |
| Large | Up to 300 | $70,000 |
| Unlimited | No limit | $90,000 |

**Pros:** Simpler than pure per-user
**Cons:** Still requires user counting, band boundaries create friction

**Verdict:** Possible but suboptimal

### Option C: Location + User Hybrid

```
Price = Base Location Price + (Users above threshold × $X)
```

Example: $500/location + $100/user above 10 users per location

**Pros:** Captures both dimensions
**Cons:** Complex, requires two counts, difficult to quote

**Verdict:** Not recommended

### Option D: Per-Location with User Fair-Use Policy (Recommended)

| Tier | Locations | Users Included | Overage |
|------|-----------|----------------|---------|
| Standard | 1-5 | Up to 100 | Upgrade to Enterprise |
| Enterprise | 6-35 | Up to 500 | Contact sales |
| Enterprise Plus | 36-100 | Up to 1,000 | Contact sales |
| Enterprise Premier | 100+ | Unlimited | — |

**Pros:** Simple quoting, fair-use protects against abuse
**Cons:** Requires light enforcement mechanism

**Verdict:** Recommended approach

---

## Part 5: Recommendation

### Primary Model: Per-Location with User Fair-Use

**Structure:**

| Tier | Annual Price | Locations | Users Included | User Overage |
|------|-------------|-----------|----------------|--------------|
| Standard | $4,999 | 1-5 | Up to 100 | Upgrade to Enterprise |
| Enterprise | $25,000-45,000 | 6-35 | Up to 500 | Contact sales |
| Enterprise Plus | $45,000-75,000 | 36-100 | Up to 1,000 | Contact sales |
| Enterprise Premier | $75,000+ | 100+ | Unlimited | Included |

**Key principles:**

1. **Quote on locations** - simple, known quantity
2. **Include generous user allowance** - most customers won't hit limits
3. **Fair-use threshold** - protects against outlier abuse
4. **Overage is conversation, not automatic billing** - relationship-first

### Why This Works

| Stakeholder | Benefit |
|-------------|---------|
| **Sales** | Quote in one call, no user research delay |
| **Finance** | Predictable revenue, no true-up complexity |
| **Customer** | Simple budgeting, no license management |
| **Product** | No license tracking infrastructure required |
| **Support** | No "am I over my user limit?" tickets |

### User Fair-Use Implementation

**Monitoring (light touch):**
- Track monthly active users per account
- Alert internally (not customer) if >80% of fair-use threshold
- Proactive CSM outreach if sustained overage

**Enforcement (relationship-based):**
- No hard blocks or automatic billing
- CSM conversation: "You're getting great adoption! Let's discuss right-sizing your plan."
- Upsell to next tier or negotiate custom terms

**What NOT to do:**
- Don't show user limits prominently in UI
- Don't send automated "you're at 90% of users" emails
- Don't block access at threshold
- Don't audit customers on user counts

---

## Part 6: Competitive Positioning

### Sales Messaging

> "RecallWire charges by location with unlimited users included—so your whole team can access the platform without license management overhead. No counting, no true-ups, no surprises."

### Objection Handling

**"We want to pay for what we use"**

> "I understand the appeal. But recall management isn't like a CRM where more users means more value. Your value is comprehensive recall coverage and audit-ready documentation—whether 50 people access it or 500. Location-based pricing aligns with that value. You're paying for protection, not seats."

**"We only have a small team right now"**

> "That's fine—our pricing includes generous user allowances. And when you expand the program or involve more departments, your growth is included. No surprise license fees."

---

## Part 7: Financial Impact Analysis

### Revenue Predictability Comparison

| Metric | Per-Location | Per-User |
|--------|--------------|----------|
| Revenue variance (annual) | ±5% (facility changes) | ±15-25% (headcount flux) |
| Renewal predictability | High | Medium |
| Expansion revenue timing | Clear (new facility) | Unclear (gradual user adds) |
| Downsell risk | Low (facility closures rare) | Medium (license optimization) |

### Implementation Comparison

**If Per-User Were Adopted (Not Recommended):**

| Requirement | Effort | Timeline |
|-------------|--------|----------|
| License management system | High | 3-6 months |
| User tracking/metering | Medium | 2-3 months |
| Billing system changes | High | 2-4 months |
| Sales process redesign | Medium | 1-2 months |
| Contract template updates | Low | 2-4 weeks |
| **Total** | **High** | **6-12 months** |

**Per-Location with Fair-Use (Recommended):**

| Requirement | Effort | Timeline |
|-------------|--------|----------|
| User counting (internal only) | Low | 2-4 weeks |
| Fair-use threshold alerts | Low | 1-2 weeks |
| CSM playbook for overages | Low | 1 week |
| **Total** | **Low** | **1-2 months** |

---

## Conclusion

### Summary of Findings

| Factor | Per-User | Per-Location | Winner |
|--------|----------|--------------|--------|
| Sales velocity | Slower | Faster | Per-Location |
| Revenue predictability | Lower | Higher | Per-Location |
| Customer preference (healthcare) | Lower | Higher | Per-Location |
| Competitive positioning | Disadvantage | Favorable | Per-Location |
| Operational complexity | Higher | Lower | Per-Location |
| Margin protection | Similar | Similar | Tie |
| Growth alignment | Lower | Higher | Per-Location |

### Final Recommendation

**Maintain per-location pricing as the primary model.** Healthcare buyers prefer site-based licensing, primary competitors (ECRI, Inmar) use unlimited-user models, and per-user creates unnecessary sales friction.

Implement user fair-use thresholds as a margin protection mechanism, but do not make users a primary pricing dimension.

**Do not adopt per-user pricing.**

---

*Document updated: December 2025*
*Reflects decision to maintain per-location pricing model*
