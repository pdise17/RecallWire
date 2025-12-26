# RecallWire Enterprise Pricing & Margin Analysis

## Market Intelligence

| Data Point | Value | Source |
|------------|-------|--------|
| Mount Sinai current spend | ~$50k/year | User intel |
| TraceLink quoted price (215 users) | $67,337/year | Proposal doc |
| Enterprise sweet spot | $40-45k/year | User feedback |
| RecallWire differentiator | AI capabilities | - |

**Implication:** Price at $40-45k to undercut competitors while AI justifies premium over budget options.

---

## Revised Enterprise Pricing Structure

### Option A: Simplified Enterprise Tiers

| Enterprise Tier | Annual Price | Locations | Target Customer |
|-----------------|--------------|-----------|-----------------|
| **Enterprise Essentials** | $25,000 | 21-35 | Small health systems entering enterprise |
| **Enterprise Standard** | $40,000 | 36-75 | Mid-size health systems (sweet spot) |
| **Enterprise Plus** | $60,000 | 76-150 | Large regional systems |
| **Enterprise Premier** | $85,000+ | 150+ | National chains, academic medical centers |

### Option B: Base + Per-Location (More Flexible)

```
Enterprise Price = $20,000 base + $400/location
```

| Locations | Calculated Price | Effective Per-Location |
|-----------|------------------|------------------------|
| 25 | $30,000 | $1,200 |
| 50 | $40,000 | $800 |
| 75 | $50,000 | $667 |
| 100 | $60,000 | $600 |
| 150 | $80,000 | $533 |

**With volume discounts:**

| Locations | Base Formula | Discount | Final Price |
|-----------|--------------|----------|-------------|
| 21-50 | $20k + $400/loc | 0% | $28,400-$40,000 |
| 51-100 | $20k + $400/loc | 10% | $38,340-$54,000 |
| 101-150 | $20k + $400/loc | 15% | $51,170-$68,000 |
| 150+ | Custom | 20%+ | Negotiated |

### Recommended: Hybrid Approach

**Public positioning:** "Enterprise starts at $25,000/year"

**Internal pricing logic:**
- Base: $20,000 (covers platform, base support, all categories)
- Per-location: $350-500 (based on volume)
- AI capacity: Included in base (up to reasonable limits)
- High-volume surcharge: Negotiated for 100k+ alerts/year

**Sweet spot deal (Mount Sinai profile):**
- ~50 locations
- ~100-200 users
- ~100k alerts/year
- Price: **$40,000-45,000/year**
- Positioning: "20% below your current spend, with AI included"

---

## Margin Analysis by Tier

### Cost Structure Assumptions

#### Fixed Costs (Allocated per customer)

| Cost Category | Monthly | Annual | Notes |
|---------------|---------|--------|-------|
| Infrastructure base | $50 | $600 | Base platform (shared) |
| Security/compliance | $25 | $300 | SOC2, HIPAA overhead |
| Product/engineering | Allocated by ARR | ~8-12% of revenue | R&D allocation |

#### Variable Costs (Scale with usage)

| Cost Driver | Unit Cost | Notes |
|-------------|-----------|-------|
| **Bedrock (Claude)** | $0.015/1k input + $0.075/1k output tokens | ~$0.02-0.05 per AI query |
| **Textract** | $1.50/1,000 pages | Document processing |
| **RDS** | $0.10-0.20/GB-month + compute | Database |
| **Lambda** | $0.20/1M requests | Alert processing |
| **S3** | $0.023/GB-month | Storage |
| **Data transfer** | $0.09/GB | Outbound |

#### People Costs (Allocated)

| Role | Annual Cost | Accounts Covered | Per-Account |
|------|-------------|------------------|-------------|
| CSM (Enterprise) | $90,000 | 15-20 accounts | $4,500-6,000 |
| CSM (Business, shared) | $75,000 | 40-50 accounts | $1,500-1,875 |
| Support (Starter/Pro) | $60,000 | 200+ accounts | $300 |
| Sales (amortized CAC) | Varies | - | 10-15% of ACV |

---

### Tier-by-Tier Margin Analysis

#### Starter Tier ($1,499/year)

| Line Item | Amount | % of Revenue |
|-----------|--------|--------------|
| **Revenue** | $1,499 | 100% |
| AWS infrastructure | ($180) | 12% |
| AWS variable (light usage) | ($60) | 4% |
| Support allocation | ($150) | 10% |
| CAC (PLG, low-touch) | ($150) | 10% |
| **Gross Profit** | **$959** | **64%** |
| R&D allocation (10%) | ($150) | 10% |
| G&A allocation (8%) | ($120) | 8% |
| **Net Margin** | **$689** | **46%** |

#### Professional Tier ($3,999/year)

| Line Item | Amount | % of Revenue |
|-----------|--------|--------------|
| **Revenue** | $3,999 | 100% |
| AWS infrastructure | ($300) | 8% |
| AWS variable (moderate usage) | ($240) | 6% |
| Support allocation | ($400) | 10% |
| CAC (guided sales) | ($600) | 15% |
| **Gross Profit** | **$2,459** | **61%** |
| R&D allocation (10%) | ($400) | 10% |
| G&A allocation (8%) | ($320) | 8% |
| **Net Margin** | **$1,739** | **43%** |

#### Business Tier ($7,999/year)

| Line Item | Amount | % of Revenue |
|-----------|--------|--------------|
| **Revenue** | $7,999 | 100% |
| AWS infrastructure | ($600) | 8% |
| AWS variable (higher usage) | ($720) | 9% |
| CSM allocation (shared) | ($1,600) | 20% |
| Support allocation | ($400) | 5% |
| CAC (sales-assisted) | ($1,200) | 15% |
| **Gross Profit** | **$3,479** | **43%** |
| R&D allocation (10%) | ($800) | 10% |
| G&A allocation (8%) | ($640) | 8% |
| **Net Margin** | **$2,039** | **25%** |

*Note: Business tier margins are tighter due to CSM allocation. Consider whether shared CSM is necessary or if enhanced self-service could work.*

#### Enterprise Tier ($42,500/year - Sweet Spot)

| Line Item | Amount | % of Revenue |
|-----------|--------|--------------|
| **Revenue** | $42,500 | 100% |
| AWS infrastructure | ($3,600) | 8% |
| AWS variable (high usage - 100k alerts) | ($4,200) | 10% |
| - Bedrock (AI queries) | ($1,800) | - |
| - Textract (docs) | ($600) | - |
| - Compute/Lambda | ($1,200) | - |
| - Storage/DB | ($600) | - |
| Dedicated CSM | ($5,000) | 12% |
| Premium support | ($2,000) | 5% |
| CAC (enterprise sales) | ($6,375) | 15% |
| **Gross Profit** | **$21,325** | **50%** |
| R&D allocation (10%) | ($4,250) | 10% |
| G&A allocation (8%) | ($3,400) | 8% |
| **Net Margin** | **$13,675** | **32%** |

---

### Enterprise Margin Sensitivity

#### By Deal Size

| Enterprise Price | AWS Costs | CSM | CAC | Gross Margin | Net Margin |
|------------------|-----------|-----|-----|--------------|------------|
| $25,000 | $5,500 | $5,000 | $3,750 | $10,750 (43%) | $5,750 (23%) |
| $35,000 | $6,500 | $5,000 | $5,250 | $18,250 (52%) | $11,400 (33%) |
| **$42,500** | **$7,800** | **$5,000** | **$6,375** | **$23,325 (55%)** | **$15,175 (36%)** |
| $50,000 | $8,500 | $5,000 | $7,500 | $29,000 (58%) | $20,000 (40%) |
| $60,000 | $9,500 | $5,000 | $9,000 | $36,500 (61%) | $26,600 (44%) |

#### By Usage Volume (at $42,500 price point)

| Alert Volume | AI Queries | AWS Variable | Gross Margin | Net Margin |
|--------------|------------|--------------|--------------|------------|
| 50,000/yr | 6,000/yr | $3,200 | $25,700 (60%) | $17,550 (41%) |
| 100,000/yr | 12,000/yr | $7,800 | $21,100 (50%) | $12,950 (30%) |
| 150,000/yr | 18,000/yr | $12,400 | $16,500 (39%) | $8,350 (20%) |
| 200,000/yr | 24,000/yr | $17,000 | $11,900 (28%) | $3,750 (9%) |

**Key insight:** At 150k+ alerts/year, margins get squeezed significantly. This is where usage limits or tiered enterprise pricing becomes critical.

---

### Margin Improvement Levers

#### 1. AI Cost Optimization

| Strategy | Potential Savings | Implementation |
|----------|-------------------|----------------|
| Query caching | 20-30% of Bedrock costs | Cache common recall questions |
| Smaller models for simple queries | 40-50% per query | Route simple → Haiku, complex → Sonnet |
| Batch processing | 15-20% | Non-real-time alert matching |
| Prompt optimization | 10-20% | Reduce token usage |

**Estimated impact:** Reduce AI variable costs by 30-40%

#### 2. Tiered AI Access

Instead of unlimited AI at Enterprise, consider:

| Enterprise Sub-tier | AI Queries/mo | Base Price | Effective AI Cost |
|---------------------|---------------|------------|-------------------|
| Standard | 2,000 | $40,000 | Included |
| Plus | 5,000 | $50,000 | Included |
| Premier | Unlimited | $70,000+ | Absorbed |

#### 3. Self-Service for Lower Tiers

| Current | Proposed | Savings |
|---------|----------|---------|
| Shared CSM for Business | Enhanced self-service + office hours | $800-1,200/account |
| Priority email for Pro | AI-assisted support + escalation | $200-300/account |

#### 4. Implementation Fees

| Customer Size | Implementation Fee | Covers |
|---------------|-------------------|--------|
| Professional | $500 (optional) | Guided onboarding |
| Business | $2,000 | White-glove setup |
| Enterprise | $5,000-15,000 | Dedicated implementation |

This shifts some CAC to customer-paid implementation.

---

## Recommended Enterprise Pricing

### Target: $40-45k Sweet Spot with Healthy Margins

**Structure:**

```
Enterprise Standard: $40,000/year
├── Includes: Up to 50 locations
├── Includes: All category modules
├── Includes: Dedicated CSM
├── Includes: 2,000 AI queries/month
├── Includes: 100,000 alerts/year
└── Overages: Negotiated or upgrade to Plus
```

```
Enterprise Plus: $55,000/year
├── Includes: Up to 100 locations
├── Includes: All category modules
├── Includes: Dedicated CSM
├── Includes: 5,000 AI queries/month
├── Includes: 250,000 alerts/year
└── Overages: Negotiated or upgrade to Premier
```

```
Enterprise Premier: $75,000+/year
├── Includes: Unlimited locations
├── Includes: All category modules
├── Includes: Named CSM + executive sponsor
├── Includes: Unlimited AI
├── Includes: Custom SLAs
└── Custom terms negotiated
```

### Positioning vs. Competition

| Competitor | Their Price | RecallWire Price | RecallWire Advantage |
|------------|-------------|------------------|---------------------|
| Mount Sinai's current (TraceLink?) | ~$50k | $40-45k | 10-20% savings + AI |
| OneRecall (estimated) | $50-75k | $40-45k | Transparent, AI included |
| PAR/NotiSphere | $30-40k | $40-45k | Premium positioning, AI |

**Sales pitch:** "Get AI-powered recall management for less than you're paying today. $40k vs. your current $50k, with RecallWire Assistant included."

---

## Summary: Margin Expectations by Tier

| Tier | Revenue | Target Gross Margin | Target Net Margin |
|------|---------|--------------------|--------------------|
| Starter | $1,499/yr | 65-70% | 45-50% |
| Professional | $3,999/yr | 60-65% | 40-45% |
| Business | $7,999/yr | 50-55% | 30-35% |
| Enterprise ($40-45k) | $42,500/yr | 50-55% | 32-38% |
| Enterprise ($55k+) | $55,000+/yr | 55-60% | 38-45% |

**Blended target:** 55-60% gross margin, 35-40% net margin across portfolio.

### Key Margin Protection Rules

1. **Never go below $35k for true enterprise** (50+ locations) - margins collapse
2. **Usage limits are non-negotiable** at Business tier - protects against margin erosion
3. **AI queries must be metered or capped** below Premier tier
4. **High-volume customers (150k+ alerts) require Premier pricing** or custom surcharges
5. **Implementation fees offset CAC** for enterprise deals

---

## Appendix: Cost Benchmarks

### AWS Cost Estimates (Monthly)

| Component | Starter | Professional | Business | Enterprise |
|-----------|---------|--------------|----------|------------|
| RDS | $25 | $50 | $150 | $400 |
| Lambda | $5 | $15 | $50 | $150 |
| S3 | $5 | $10 | $25 | $75 |
| Bedrock | $10 | $40 | $150 | $300 |
| Textract | $5 | $20 | $50 | $100 |
| Other | $10 | $25 | $50 | $100 |
| **Total** | **$60** | **$160** | **$475** | **$1,125** |
| **Annual** | **$720** | **$1,920** | **$5,700** | **$13,500** |
