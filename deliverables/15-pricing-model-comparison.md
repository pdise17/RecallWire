# RecallWire Pricing Model Comparison: Three Models Tested

## Purpose

This document stress-tests three pricing models against real customer scenarios to determine the right pricing structure for a product where **71% of features have zero competition** and customers are multi-location, multi-user healthcare organizations.

**Models Tested:**
- **Model A:** Per-User + Per-Location (hybrid)
- **Model B:** Feature-Tier Based (from Document 14)
- **Model C:** Per-Location + Feature Tier (hybrid, recommended)

---

## Market Context: What Comparable Tools Actually Charge

### Healthcare Compliance SaaS — Real Pricing Data

| Vendor | Model | Per-User Rate | Typical ACV |
|--------|-------|---------------|-------------|
| Greenlight Guru (QMS) | Per-user | $249/user/mo | $25K-$60K/yr |
| Qualio (QMS) | Base + per-user | $12K base + $3K/user/yr | $25K-$75K/yr |
| MasterControl (Quality) | Per-user | ~$50-$140/user/mo | $25K-$600K+/yr |
| Veeva (Life Sciences) | Per-user per module | $50-$200/user/mo | $500K+/yr |
| Egnyte (Document Mgmt) | Per-user | $20-$66/user/mo | $5K-$50K/yr |
| ComplianceQuest (EQMS) | Per-user | $30/user/mo | $10K-$50K/yr |

### Healthcare Recall Management — Real Pricing Data

| Vendor | Model | Price | Users |
|--------|-------|-------|-------|
| ECRI Alerts | Site license | $75,878/yr (verified) | Unlimited |
| Inmar OneRecall | Per-facility | $25K-$75K+ est. | Unlimited |
| PAR Excellence | Flat SaaS | ~$2,400/yr est. | Unlimited |

**Critical finding:** All three recall management competitors include unlimited users. Per-user pricing would be a competitive disadvantage in this specific market.

**However:** The broader healthcare compliance SaaS market (QMS, life sciences, document management) heavily uses per-user pricing at $30-$250/user/month. RecallWire's features extend beyond pure recall management into compliance, analytics, and workflow — where per-user pricing is standard.

---

## The Three Models

---

## Model A: Per-User + Per-Location

### Structure

| Component | Price |
|-----------|-------|
| **Platform base fee** | $500/mo ($6,000/yr) |
| **Per-location fee** | $200/mo per location ($2,400/yr) |
| **Per-user fee** | $75/mo per user ($900/yr) |
| **Annual discount** | 15% off total (pay upfront) |

### Typical User Counts by Facility Type

| Facility Type | Typical Users | Roles |
|---------------|---------------|-------|
| Small clinic / ASC | 2-3 | Materials coordinator, manager |
| Community hospital | 5-8 | Materials mgmt, risk, quality, biomed, supply chain |
| Large hospital | 8-15 | Above + department heads, compliance, nursing leads |
| Academic medical center | 15-25 | Above + research, residency, multi-specialty |

### Model A: Customer Scenario Pricing

| Scenario | Locations | Users | Monthly | Annual | Annual (15% disc.) |
|----------|-----------|-------|---------|--------|-------------------|
| **Single clinic** | 1 | 3 | $925 | $11,100 | **$9,435** |
| **Small ASC group** | 3 | 8 | $1,700 | $20,400 | **$17,340** |
| **5-location practice** | 5 | 15 | $2,625 | $31,500 | **$26,775** |
| **15-location regional** | 15 | 60 | $8,000 | $96,000 | **$81,600** |
| **25-location health system** | 25 | 100 | $13,000 | $156,000 | **$132,600** |
| **75-location enterprise** | 75 | 300 | $38,000 | $456,000 | **$387,600** |
| **150-location national** | 150 | 600 | $75,500 | $906,000 | **$770,100** |

### Model A: Pros and Cons

| Pros | Cons |
|------|------|
| Revenue scales precisely with customer size | "How many users?" slows sales cycle 2-4 weeks |
| Higher revenue from large deployments | Competitors include unlimited users — disadvantage |
| Familiar to SaaS buyers | User count ambiguity (who counts as a user?) |
| Forces customer to think about adoption | License management overhead |
| | Healthcare prefers site licenses over per-seat |
| | Revenue unpredictable (user counts fluctuate) |

---

## Model B: Feature-Tier Based (Document 14)

### Structure

| Tier | Monthly | Annual | Locations | Users |
|------|---------|--------|-----------|-------|
| **Essentials** | $199/mo | $1,999/yr | 1 | 2 |
| **Standard** | $449/mo | $4,999/yr | 1-5 | 10 |
| **Professional** | $1,199/mo | $12,999/yr | 1-10 | 25 |
| **Enterprise** | Contact | $25,000+/yr | Unlimited | Unlimited |

### Model B: Customer Scenario Pricing

| Scenario | Locations | Users | Tier | Annual |
|----------|-----------|-------|------|--------|
| **Single clinic** | 1 | 3 | Standard | **$4,999** |
| **Small ASC group** | 3 | 8 | Standard | **$4,999** |
| **5-location practice** | 5 | 15 | Professional | **$12,999** |
| **15-location regional** | 15 | 60 | Enterprise | **$30,000** |
| **25-location health system** | 25 | 100 | Enterprise | **$40,000** |
| **75-location enterprise** | 75 | 300 | Enterprise Plus | **$60,000** |
| **150-location national** | 150 | 600 | Enterprise Premier | **$85,000** |

### Model B: Pros and Cons

| Pros | Cons |
|------|------|
| Simple to quote — location count is known | No revenue scaling for large facilities with many users |
| Aligns with competitor models (unlimited users) | Leaves significant money on the table at scale |
| Feature gates create clear upgrade path | Small clinics overpay relative to value ($4,999 for 3 users) |
| Fast sales cycle | Large systems underpay relative to value ($40K for 100 users) |
| No license management needed | Revenue gap: 75-location system pays $60K vs $387K in Model A |

---

## Model C: Per-Location + Feature Tier (Hybrid — Recommended)

### Structure

Combines the simplicity of location-based pricing with feature tiers that reflect the lifecycle value.

| Tier | Per-Location/mo | Platform Base/mo | Annual Discount | Features |
|------|----------------|-----------------|-----------------|----------|
| **Essentials** | $299/location | $499 | 15% | Stage 1: Detect & Alert |
| **Standard** | $399/location | $699 | 15% | Stage 1+2: Match & Analyze |
| **Professional** | $599/location | $999 | 15% | Stage 1+2+3: Act & Resolve |
| **Enterprise** | Custom | Custom | Negotiated | All Stages: Close Every Loop |

**Users: Unlimited at all tiers.** This matches competitors and removes sales friction.

### Model C: Customer Scenario Pricing

| Scenario | Locations | Tier | Monthly | Annual | Annual (15% disc.) |
|----------|-----------|------|---------|--------|-------------------|
| **Single clinic** | 1 | Essentials | $798 | $9,576 | **$8,140** |
| **Single clinic** | 1 | Standard | $1,098 | $13,176 | **$11,200** |
| **Small ASC group** | 3 | Standard | $1,896 | $22,752 | **$19,339** |
| **5-location practice** | 5 | Standard | $2,694 | $32,328 | **$27,479** |
| **5-location practice** | 5 | Professional | $3,994 | $47,928 | **$40,739** |
| **15-location regional** | 15 | Professional | $9,984 | $119,808 | **$101,837** |
| **25-location health system** | 25 | Professional | $15,974 | $191,688 | **$162,935** |
| **25-location health system** | 25 | Enterprise | Custom | — | **$75,000-$120,000** |
| **75-location enterprise** | 75 | Enterprise | Custom | — | **$150,000-$225,000** |
| **150-location national** | 150 | Enterprise | Custom | — | **$250,000-$400,000** |

### Model C: Enterprise Discount Schedule (Internal)

| Locations | Per-Location Effective | Discount from List |
|-----------|----------------------|-------------------|
| 6-15 | $500-$599 | 0% |
| 16-35 | $400-$499 | 17-33% |
| 36-75 | $300-$399 | 33-50% |
| 76-150 | $200-$299 | 50-67% |
| 150+ | $150-$250 | Negotiated |

### Model C: Pros and Cons

| Pros | Cons |
|------|------|
| Revenue scales with locations (known, stable number) | Higher sticker price may slow SMB adoption |
| Unlimited users — matches competitors | Per-location math visible to buyer (they can multiply) |
| Feature tiers create clear upgrade narrative | Requires enterprise discount schedule for large deals |
| No license management overhead | More complex than flat tier pricing (Model B) |
| Properly captures value of multi-location deployment | |
| Healthcare buyers understand per-facility models | |

---

## Side-by-Side Comparison: All Three Models

### Annual Revenue by Customer Scenario

| Scenario | Locs | Users | Model A (Per-User+Loc) | Model B (Feature Tier) | Model C (Per-Loc+Tier) |
|----------|------|-------|----------------------|----------------------|----------------------|
| Single clinic | 1 | 3 | $9,435 | $4,999 | $8,140 |
| Small ASC group | 3 | 8 | $17,340 | $4,999 | $19,339 |
| 5-loc practice | 5 | 15 | $26,775 | $12,999 | $27,479 |
| 15-loc regional | 15 | 60 | $81,600 | $30,000 | $101,837 |
| 25-loc health system | 25 | 100 | $132,600 | $40,000 | $120,000* |
| 75-loc enterprise | 75 | 300 | $387,600 | $60,000 | $200,000* |
| 150-loc national | 150 | 600 | $770,100 | $85,000 | $350,000* |

*Enterprise tier with volume discounts applied

### Revenue Comparison Chart

```
Revenue by Scenario (Annual)

$800K ┤
      │                                          ████ Model A
$700K ┤                                          ████
      │
$600K ┤
      │
$500K ┤
      │
$400K ┤                              ████
      │                                          ░░░░ Model C
$350K ┤                                          ░░░░
      │
$300K ┤
      │
$200K ┤                              ░░░░
      │                  ████
$130K ┤                  ░░░░
$100K ┤          ████    ░░░░
      │          ░░░░
 $85K ┤                              ▓▓▓▓        ▓▓▓▓ Model B
 $60K ┤
 $40K ┤                  ▓▓▓▓
 $27K ┤  ████░░░░
      │
 $13K ┤          ▓▓▓▓
  $5K ┤  ▓▓▓▓
      └───────────────────────────────────────────────
       1-loc    5-loc   15-loc   75-loc   150-loc
```

---

## The Verdict: What the Numbers Say

### Model B (Feature-Tier) is drastically underpriced

| Evidence | Detail |
|----------|--------|
| A 75-location system pays $60K | Labor savings alone: $120K-$225K/yr (Doc 12) |
| A 25-location system pays $40K | ECRI charges $75,878 for comparable features at ONE system |
| A 5-location ASC pays $4,999 | Greenlight Guru charges $25K-$60K for per-user QMS with LESS exclusive features |
| Revenue capture rate | Model B captures only **11-22%** of Model A or C revenue at enterprise scale |

### Model A (Per-User+Location) maximizes revenue but creates friction

| Evidence | Detail |
|----------|--------|
| Highest revenue at every scenario | $770K for 150-location vs $85K (Model B) or $350K (Model C) |
| But: sales cycle adds 2-4 weeks | Healthcare buyers don't know user counts quickly |
| But: competitors offer unlimited users | ECRI, Inmar, PAR all include unlimited |
| But: user counts fluctuate | Turnover, seasonal staff, department changes |
| Revenue potential is theoretical | Actual close rates may suffer due to friction |

### Model C (Per-Location+Tier) balances revenue with market reality

| Evidence | Detail |
|----------|--------|
| Revenue 3-4x higher than Model B | Properly values multi-location deployment |
| Unlimited users | Matches competitors, removes friction |
| Healthcare buyers understand per-facility | EHR, credentialing, supply chain all price this way |
| Feature tiers drive upgrades | Lifecycle ladder intact |
| Enterprise discounts keep deals competitive | $200-$300/loc at scale vs ECRI's ~$250-$500/loc equivalent |

---

## Monthly vs. Annual: What the Market Data Shows

### Healthcare SaaS Discount Norms

| Commitment | General SaaS Discount | Healthcare SaaS Discount |
|------------|----------------------|-------------------------|
| Annual (pay upfront) | 10-20% (typically "2 months free") | **5-8%** |
| 2-year contract | 15-25% | **5-10%** |
| 3-year contract | 20-30% | **10-15%** |
| 5-year contract | N/A | **15-20%** |

Healthcare discounts are **more conservative** because:
- Longer sales cycles create higher switching costs
- Compliance requirements make switching painful
- Multi-year contracts are the norm (not the exception)
- Regulatory mandates make the tool "must-have" not "nice-to-have"

### Recommendation: Annual Discount Structure

| Model | Monthly Rate | Annual (pay monthly) | Annual (prepaid) | Savings |
|-------|-------------|---------------------|-----------------|---------|
| Essentials | $798/loc | $798/mo × 12 = $9,576 | $8,140 | 15% |
| Standard | $1,098/loc | $1,098/mo × 12 = $13,176 | $11,200 | 15% |
| Professional | $3,994/5-loc | $3,994/mo × 12 = $47,928 | $40,739 | 15% |
| Enterprise | Custom | Custom | Custom | Negotiated |

**Multi-year incentives (Enterprise only):**

| Contract Length | Additional Discount | Effective Discount |
|----------------|--------------------|--------------------|
| 1 year | — | 15% (annual prepay) |
| 2 years | +5% | 20% |
| 3 years | +10% | 25% |

---

## Final Recommendation: Model C with Adjusted Pricing

### Why Model C Wins

| Criterion | Model A | Model B | Model C |
|-----------|---------|---------|---------|
| Revenue capture | Best | Worst | Strong |
| Sales velocity | Worst | Best | Good |
| Competitive positioning | Weak (per-user) | Strong (unlimited) | Strong (unlimited) |
| Healthcare buyer fit | Poor | Good | Best |
| Revenue predictability | Poor (user flux) | Good | Good |
| Value alignment | Good | Poor (underpriced) | Best |
| Operational complexity | High | Low | Low |

### Recommended Price Points (Model C)

| Tier | Per-Location/mo | Platform Base/mo | Annual (1 loc, prepaid) | Users |
|------|----------------|-----------------|----------------------|-------|
| **Essentials** | $299 | $499 | $8,140 | Unlimited |
| **Standard** | $399 | $699 | $11,200 | Unlimited |
| **Professional** | $599 | $999 | $16,300 (1 loc) | Unlimited |
| **Enterprise** | $200-$500 | Custom | $25,000+ | Unlimited |

### Revenue Validation Against Market

| Scenario | Model C Price | Market Comparables | Assessment |
|----------|-------------|-------------------|------------|
| 1-location clinic (Standard) | $11,200/yr | PAR: ~$2,400; Greenlight: $25K+ | Above recall competitors, below compliance SaaS. Justified by exclusive features. |
| 5-location ASC (Standard) | $27,479/yr | Greenlight 5-user: ~$15K; Qualio: $27K | In line with compliance SaaS market. |
| 15-location (Professional) | $101,837/yr | ECRI: $75,878; Inmar: $25K-$75K | Above recall competitors but includes 15x locations + advanced features. Per-location: $6,789 — comparable to healthcare SaaS norms. |
| 25-location (Enterprise) | $75K-$120K | ECRI: $75,878 (single entity); Inmar: $50K-$75K | Competitive at scale with volume discounts. |
| 75-location (Enterprise) | $150K-$225K | MasterControl 300-user: ~$510K; Veeva: $500K+ | Well below per-user compliance tools. Enterprise healthcare norm. |

### Key Pricing Principles

1. **Unlimited users at all tiers** — matches recall management competitors, no friction
2. **Per-location scaling** — healthcare buyers understand this, revenue grows with deployment
3. **Feature tiers drive upgrades** — lifecycle ladder from Detect to Close Every Loop
4. **Enterprise volume discounts** — keep competitive at 25+ locations against Inmar/ECRI
5. **15% annual prepay discount** — conservative, matching healthcare SaaS norms (not general SaaS 20%)
6. **Multi-year discounts for Enterprise** — 2yr: 20%, 3yr: 25%

---

## What Changed from Document 14

| Element | Document 14 | This Document | Why |
|---------|------------|---------------|-----|
| Pricing structure | Flat per-tier | Per-location + platform base | Captures multi-location value |
| 1-location Standard | $4,999/yr | $11,200/yr | Was underpriced for exclusive features |
| 5-location Standard | $4,999/yr | $27,479/yr | 5 locations = 5x value delivered |
| 15-location Professional | $12,999/yr | $101,837/yr | 15 locations + compliance features |
| Users | 2-25 (tiered) | Unlimited (all tiers) | Matches competitors, removes friction |
| Annual discount | 7-16% | 15% flat | Aligns with healthcare SaaS norms |

---

*Document created: February 2026*
*Builds on: Document 14, Document 13 (Per-User Assessment), Document 12 (ROI Analysis)*
*Market research: February 2026*
