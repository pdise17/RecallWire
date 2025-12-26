# RecallWire Pricing Strategy Addendum

## New Intelligence & Strategic Considerations

This addendum addresses two strategic questions raised after initial deliverables were completed, incorporating newly discovered competitive intelligence.

---

## Part 1: Usage-Based Pricing for High-Volume Facilities

### The Problem

Large health systems create disproportionate platform overhead compared to smaller facilities:

| Facility Type | Est. Annual Alerts | Platform Load | Current Pricing Impact |
|---------------|-------------------|---------------|------------------------|
| Single ASC | 500-2,000 | Low | $1,499/yr (appropriate) |
| Community Hospital | 5,000-15,000 | Medium | $3,999/yr (appropriate) |
| Regional System (20 sites) | 30,000-60,000 | High | $7,999/yr (may be underpriced) |
| Large Academic Medical Center | 100,000-150,000+ | Very High | $25k+/yr (needs tiering) |

**Real-world example:** Mount Sinai Health System receives ~117,000 alerts per year. A flat enterprise rate doesn't account for the processing, matching, and storage overhead this creates.

### Competitor Approaches to This Problem

#### TraceLink (Hybrid Model)
Discovered pricing from Mount Sinai proposal:

| User Count | Annual Price | Per-User Rate |
|------------|-------------|---------------|
| 100 users | $38,195 | $382/user |
| 150 users | $51,695 | $345/user |
| 200 users | $63,422 | $317/user |
| 215 users | $67,337 | $313/user |
| Additional | +$300/user | - |

**Also offers per-site pricing:**
- Tier 1 (1-3 sites): FREE
- Tier 2 (4-50 sites): $800/site/year
- Tier 3 (51-100 sites): $600/site/year
- Case study: 74-site health system = ~$52,000/year

#### OneRecall (Volume-Implicit)
No explicit usage pricing, but enterprise contracts likely factor in:
- Location count
- User count
- Integration complexity
- Support tier

### Recommended Usage-Based Pricing Model for RecallWire

#### Option A: Alert Volume Tiers (Recommended)

Add consumption-based component to Enterprise tier:

| Enterprise Sub-Tier | Annual Alerts | Base Price | Per-Alert Overage |
|--------------------|---------------|------------|-------------------|
| Enterprise Standard | Up to 50,000 | $25,000/yr | $0.15/alert |
| Enterprise Plus | Up to 100,000 | $40,000/yr | $0.12/alert |
| Enterprise Premium | Up to 200,000 | $60,000/yr | $0.10/alert |
| Enterprise Unlimited | Unlimited | $85,000+/yr | Negotiated |

**Advantages:**
- Aligns cost with actual platform usage
- Protects margins on high-volume accounts
- Creates natural upsell trigger
- Transparent and predictable for customers

**Implementation:**
- Track alert volume monthly
- Bill overage quarterly or annually
- Provide usage dashboard for visibility
- Set soft caps with alerts before hard limits

#### Option B: User-Based Pricing (Alternative)

Follow TraceLink's model for Enterprise tier:

| User Count | Annual Price | Per-User Rate |
|------------|-------------|---------------|
| 25-50 users | $25,000 | $500-1,000/user |
| 51-100 users | $35,000 | $350-700/user |
| 101-200 users | $50,000 | $250-500/user |
| 200+ users | Custom | $200-300/user |

**Advantages:**
- Easy to measure and communicate
- Familiar model for healthcare buyers
- Scales with organizational engagement

**Disadvantages:**
- Doesn't directly correlate to platform cost
- May discourage user adoption
- Gaming risk (shared logins)

#### Option C: Hybrid Model

Combine location + usage factors:

```
Enterprise Price = Base ($15,000) +
                   Location Fee ($400/location) +
                   Alert Volume Fee (tiered per above)
```

**Example calculations:**

| Customer Profile | Locations | Annual Alerts | Calculated Price |
|-----------------|-----------|---------------|------------------|
| Regional System | 25 | 40,000 | $15k + $10k + $6k = $31,000 |
| Large Academic | 50 | 120,000 | $15k + $20k + $14.4k = $49,400 |
| National Chain | 150 | 300,000 | $15k + $60k + $30k = $105,000 |

### Recommendation

**Implement Option A (Alert Volume Tiers)** for the following reasons:

1. **Direct cost correlation**: Alert processing is the primary cost driver
2. **Transparency**: Easy to explain and justify to procurement
3. **Competitive differentiation**: Most competitors use opaque enterprise pricing
4. **Growth alignment**: Revenue scales as customer's needs grow
5. **Fair to small enterprises**: Don't overpay to subsidize mega-systems

**Implementation priority**: Phase 5 (Scale & Optimize) - introduce after initial enterprise customers are onboarded and baseline metrics established.

---

## Part 2: Food/Supply Chain Industry Expansion

### Market Opportunity Assessment

#### Evidence of Cross-Industry Potential

From OneRecall's alert domain breakdown:
- Pharmaceutical: 33.4%
- OR Products: 19.9%
- Non-OR Products: 13.7%
- Lab: 8.6%
- Cardiology: 8.5%
- **Food: 7.8%**
- Radiology: 6.9%
- Ophthalmology: 1.3%

**Key insight:** OneRecall already handles 7.8% food-related recalls, indicating healthcare facilities have food recall needs (hospital cafeterias, dietary services, patient nutrition).

#### Adjacent Market: FSMA Compliance

The Food Safety Modernization Act (FSMA) creates compliance requirements similar to medical device recalls:

| Requirement | Medical Device (FDA) | Food Safety (FSMA) |
|-------------|---------------------|-------------------|
| Traceability | Yes | Yes (FSMA 204) |
| Recall notification | Required | Required |
| Audit trail | Required | Required |
| Supplier management | Best practice | Required |
| Timeline requirements | 24-72 hours | 24 hours |

#### Competitor Landscape: Food/Supply Chain

**TrackVision AI** (from reviewed materials):
- GS1 EPCIS 2.0 compliant platform
- Targets food/supply chain traceability
- End-to-end visibility focus
- Key features: lot-level tracking, shelf-life management, automated recall alerts

**Implications for RecallWire:**
- Food recall management is adjacent but distinct market
- Requires GS1/EPCIS integration for serious competition
- Healthcare food service is natural entry point (hospital dietary)

### Expansion Strategy Options

#### Option 1: Healthcare Food Service Focus (Low Risk)

**Target:** Hospital dietary departments, healthcare cafeterias

**Approach:**
- Extend existing FDA recall coverage to food categories
- Add food-specific recall sources (FDA, USDA, state health departments)
- Market to existing healthcare customers as "complete recall coverage"

**Pricing:** Include in existing tiers as feature expansion

**Pros:**
- Minimal product development
- Cross-sell to existing customers
- Stays within healthcare vertical

**Cons:**
- Limited market expansion
- Doesn't address broader food industry

#### Option 2: Food Industry Module (Medium Risk)

**Target:** Food manufacturers, distributors, retail food service

**Approach:**
- Develop food-specific module with FSMA compliance features
- Integrate GS1/EPCIS standards
- Separate go-to-market for food industry

**Pricing suggestion:**

| Tier | Monthly | Annual | Target |
|------|---------|--------|--------|
| Food Starter | $199/mo | $1,999/yr | Single facility restaurants, small food producers |
| Food Professional | $499/mo | $4,999/yr | Multi-location food service, regional distributors |
| Food Enterprise | Custom | $30,000+/yr | Large food manufacturers, national chains |

**Pros:**
- Significant TAM expansion
- Leverages existing platform capabilities
- Diversifies revenue streams

**Cons:**
- New market, new competition
- Product development required
- Separate sales/marketing investment

#### Option 3: Supply Chain Platform (High Risk/Reward)

**Target:** Broader supply chain traceability across industries

**Approach:**
- Build generalized traceability platform
- Position against TrackVision AI, TraceLink supply chain
- Multiple industry verticals

**Pros:**
- Largest potential market
- Platform strategy advantages

**Cons:**
- Significant pivot from current focus
- Heavy competition (SAP, Oracle, specialized players)
- Dilutes healthcare positioning

### Recommendation: Phased Expansion

**Phase 1 (Now):** Healthcare Food Service Focus
- Add food recall sources to existing platform
- Market "comprehensive recall coverage" including food
- No pricing change, feature enhancement for Professional+ tiers
- Estimated development: Minimal (data source integration)

**Phase 2 (Post-Enterprise Stabilization):** Food Industry Module
- Develop standalone food industry offering
- FSMA compliance features
- Separate pricing track
- Target: 12-18 months post core pricing launch

**Phase 3 (Evaluate Based on Phase 2):** Broader Supply Chain
- Only if food module shows strong traction
- Would require significant investment decision
- Consider acquisition vs. build

### Industry Expansion Pricing Framework

If pursuing multi-industry strategy, consider:

| Industry | Complexity | Suggested Premium/Discount |
|----------|------------|---------------------------|
| Healthcare (base) | High | Base pricing |
| Food Service | Medium | -10% (less complex workflows) |
| Food Manufacturing | High | Base pricing |
| Pharmaceutical | Very High | +20% (regulatory complexity) |
| General Supply Chain | Medium | -15% (less specialized) |

---

## Part 3: Updated Competitive Intelligence

### TraceLink Actual Pricing (Newly Discovered)

From Mount Sinai Health System proposal:

**Per-User Model:**
- 100 Users: $38,195/year ($382/user)
- 150 Users: $51,695/year ($345/user)
- 200 Users: $63,422/year ($317/user)
- 215 Users: $67,337/year ($313/user)
- Implementation: $4,000 one-time
- Additional users: $300/user

**Per-Site Model:**
- 1-3 sites: FREE
- 4-50 sites: $800/site/year
- 51-100 sites: $600/site/year

**Case Study:** 74-site health system ≈ $52,000/year

### OneRecall Key Differentiators (From Enterprise Deck)

- Co-developed with Johns Hopkins Health System
- 60% US hospital market share
- 18 of top 22 US News Honor Roll hospitals
- rapidID AI matching: 80% reduction in processing time
- 27 days faster notification vs. manual processes
- User role hierarchy: Recall Technicians → Recall Managers → Executive

### PAR Excellence/NotiSphere Positioning

- Targets "targeted notifications" - only 2.5% of alerts actually apply
- Notable customers: Mayo Clinic, BJC Healthcare, Ochsner Health
- Baptist Health case study: Successful Joint Commission audit defense
- 16+ days average alert speed improvement

### Revised Competitive Pricing Matrix

| Competitor | SMB (1-5 sites) | Mid-Market (6-50 sites) | Enterprise (50+) |
|------------|-----------------|------------------------|------------------|
| **RecallWire (Proposed)** | $1,499-$3,999/yr | $7,999/yr | $25,000+/yr |
| **TraceLink** | FREE-$4,000/yr | $32,000-$40,000/yr | $52,000-$67,000/yr |
| **OneRecall** | Not served | ~$15,000-30,000/yr (est.) | $40,000-100,000/yr (est.) |
| **PAR/NotiSphere** | ~$5,000-10,000/yr (est.) | ~$15,000-25,000/yr (est.) | ~$30,000-50,000/yr (est.) |
| **ECRI** | Not served | ~$25,000-40,000/yr (est.) | $50,000-100,000/yr (est.) |

### RecallWire Competitive Position

**Strengths to emphasize:**
1. **Best SMB value**: Significantly undercuts TraceLink's per-site model for small facilities
2. **Transparent pricing**: First to market with clear public tiers
3. **AI differentiation**: RecallWire Assistant vs. OneRecall's rapidID
4. **Modern platform**: vs. OneRecall's 2004-era foundation

**Watch points:**
1. TraceLink's free tier for 1-3 sites is aggressive
2. OneRecall's Johns Hopkins credibility and market share
3. PAR/NotiSphere may respond with clearer pricing post-acquisition

---

## Summary of Recommendations

### Immediate Actions

1. **Finalize proposed 4-tier pricing** as originally recommended
2. **Add healthcare food recalls** to Professional+ tiers (feature expansion)
3. **Plan for usage-based enterprise pricing** (Phase 5 implementation)

### Medium-Term (Post-Launch)

1. **Implement alert volume tiers** for Enterprise customers
2. **Develop food industry module** if healthcare food shows traction
3. **Monitor TraceLink and PAR/NotiSphere** pricing responses

### Pricing Model Summary

| Segment | Current Recommendation | Usage-Based Addition |
|---------|----------------------|---------------------|
| Starter | $149/mo flat | None needed |
| Professional | $399/mo flat | None needed |
| Business | $799/mo flat | Optional alert overage |
| Enterprise | $25,000+/yr base | + Alert volume tiers |

This maintains simplicity for SMB/mid-market while addressing the legitimate concern that mega-systems create disproportionate platform costs.
