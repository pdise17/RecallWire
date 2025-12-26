# RecallWire Multi-Dimensional Pricing Model

## Overview

This document outlines a pricing structure built on three dimensions plus usage limits to protect platform costs:

1. **Locations** - Primary scaling metric (customer-friendly)
2. **Feature Tier** - AI and advanced capabilities gated by tier
3. **Categories** - Industry modules (Medical Devices, Food, Pharma, etc.)
4. **Usage Limits** - Per-tier caps with overage pricing

---

## Pricing Architecture

```
Total Price = Base Tier Price + Category Add-ons + Usage Overages
              (includes location allowance)
```

---

## Dimension 1: Feature Tiers (with Location Allowances)

| Tier | Monthly | Annual | Locations Included | Target Customer |
|------|---------|--------|-------------------|-----------------|
| **Starter** | $149/mo | $1,499/yr | 1 | Single-facility clinics, ASCs |
| **Professional** | $399/mo | $3,999/yr | Up to 5 | Multi-site practices |
| **Business** | $799/mo | $7,999/yr | Up to 20 | Regional health systems |
| **Enterprise** | Custom | $25,000+/yr | Unlimited | Large health systems |

### Additional Locations (for Starter/Professional/Business)

| Tier | Additional Location Price |
|------|--------------------------|
| Starter | $99/mo per location |
| Professional | $69/mo per location |
| Business | $49/mo per location |
| Enterprise | Included (volume discounts negotiated) |

---

## Dimension 2: Feature Gating by Tier

### Feature Flag Matrix

| Feature | Starter | Professional | Business | Enterprise |
|---------|---------|--------------|----------|------------|
| **Core Alerts** | | | | |
| FDA recall alerts | Yes | Yes | Yes | Yes |
| Email notifications | Yes | Yes | Yes | Yes |
| Basic dashboard | Yes | Yes | Yes | Yes |
| Audit trail | Yes | Yes | Yes | Yes |
| Guided resolution workflow | Yes | Yes | Yes | Yes |
| | | | | |
| **Data & Matching** | | | | |
| CSV import | Yes | Yes | Yes | Yes |
| Basic inventory matching | Yes | Yes | Yes | Yes |
| Advanced inventory matching | - | Yes | Yes | Yes |
| PO matching | - | Basic | Advanced | Custom |
| API access (read) | - | Yes | Yes | Yes |
| API access (write) | - | - | Yes | Yes |
| | | | | |
| **Multi-Facility** | | | | |
| Multi-facility hierarchy | - | Yes | Yes | Yes |
| Department routing | - | Basic | Advanced | Custom |
| Cross-facility reporting | - | Yes | Yes | Yes |
| | | | | |
| **AI Features** | | | | |
| RecallWire Assistant | Limited | Standard | Priority | Unlimited |
| AI-powered matching | - | - | Yes | Yes |
| Smart prioritization | - | - | Yes | Yes |
| Natural language search | - | - | Yes | Yes |
| | | | | |
| **Workflow & Automation** | | | | |
| Basic escalations | Email | Email | Multi-channel | Custom |
| SLA management | - | Basic | Advanced | Custom |
| Custom workflows | - | - | Limited | Unlimited |
| Automation rules | - | - | Yes | Yes |
| | | | | |
| **Security & Compliance** | | | | |
| SSO | - | Ready | Yes | Yes |
| Security review | - | - | Basic | Premium |
| Custom data retention | - | - | - | Yes |
| Sandbox environment | - | - | - | Yes |
| | | | | |
| **Support** | | | | |
| Help center | Yes | Yes | Yes | Yes |
| Email support | - | Priority (24hr) | Priority (8hr) | Premium (4hr) |
| Phone support | - | - | Yes | Yes |
| Dedicated CSM | - | - | Shared | Dedicated |
| Implementation services | Self-serve | Guided | White-glove | Dedicated team |

### AI Feature Details

**RecallWire Assistant Tiers:**

| Tier | Monthly Query Limit | Response Priority | Features |
|------|--------------------|--------------------|----------|
| Starter (Limited) | 50 queries | Standard | Basic Q&A only |
| Professional (Standard) | 200 queries | Standard | Q&A + guidance |
| Business (Priority) | 1,000 queries | Priority queue | Full capabilities |
| Enterprise (Unlimited) | Unlimited | Dedicated capacity | Custom training |

---

## Dimension 3: Category Modules

Categories are add-on modules that expand recall coverage beyond base medical devices.

### Base Coverage (Included in All Tiers)
- FDA Medical Device Recalls
- FDA Drug Recalls (basic)

### Add-on Category Modules

| Category Module | Monthly | Annual | Description |
|-----------------|---------|--------|-------------|
| **Food & Dietary** | $99/mo | $999/yr | FDA food recalls, USDA, state health dept |
| **Pharmaceutical+** | $149/mo | $1,499/yr | Enhanced drug coverage, DEA, state pharmacy boards |
| **Laboratory** | $79/mo | $799/yr | Lab equipment, reagents, diagnostics |
| **Radiology/Imaging** | $79/mo | $799/yr | Imaging equipment, contrast agents |
| **Surgical/OR** | $99/mo | $999/yr | Surgical instruments, implants, OR equipment |

### Category Bundle Discounts

| Bundle | Categories | List Price | Bundle Price | Savings |
|--------|------------|------------|--------------|---------|
| **Healthcare Complete** | All 5 modules | $505/mo | $349/mo | 31% |
| **Medical Devices** | Radiology + Surgical | $178/mo | $150/mo | 16% |
| **Clinical Bundle** | Lab + Radiology + Surgical | $257/mo | $199/mo | 23% |
| **Compliance Bundle** | Food + Pharma+ | $248/mo | $199/mo | 20% |

### Category Availability by Tier

| Category | Starter | Professional | Business | Enterprise |
|----------|---------|--------------|----------|------------|
| Base (Devices + Drugs) | Included | Included | Included | Included |
| Individual add-ons | Yes | Yes | Yes | Negotiated |
| Category bundles | - | Yes | Yes | Custom |
| All categories included | - | - | - | Option |

---

## Dimension 4: Usage Limits & Overages

### Why Usage Limits Matter

Your platform has variable costs that scale with customer usage:

| Cost Driver | AWS Service | Scaling Factor |
|-------------|-------------|----------------|
| AI queries | Bedrock | Per inference call |
| Document processing | Textract | Per page/document |
| Alert processing | Lambda/EC2 | Per alert matched |
| Data storage | RDS/S3 | Per GB stored |
| API calls | API Gateway | Per request |

### Per-Tier Usage Allowances

| Usage Metric | Starter | Professional | Business | Enterprise |
|--------------|---------|--------------|----------|------------|
| **Alerts processed/mo** | 500 | 2,500 | 10,000 | 50,000+ |
| **AI queries/mo** | 50 | 200 | 1,000 | Unlimited |
| **Document scans/mo** | 100 | 500 | 2,000 | 10,000+ |
| **API calls/mo** | - | 10,000 | 50,000 | Unlimited |
| **Data retention** | 2 years | 3 years | 5 years | Custom |
| **Storage (GB)** | 5 | 25 | 100 | Custom |

### Overage Pricing

| Usage Metric | Overage Rate | Notes |
|--------------|--------------|-------|
| Additional alerts | $0.10/alert | After tier limit |
| Additional AI queries | $0.50/query | After tier limit |
| Additional doc scans | $0.25/page | Textract pass-through + margin |
| Additional API calls | $0.001/call | After tier limit |
| Additional storage | $2/GB/mo | Above tier allowance |

### Overage Handling Options

**Option A: Soft Limits with Notifications**
- Alert customer at 80% and 100% of limit
- Allow overage up to 150% of limit
- Bill overage at end of billing cycle
- Recommend tier upgrade if consistent overages

**Option B: Hard Limits with Upgrade Prompts**
- Alert customer at 80% of limit
- Pause non-critical functions at 100%
- Require tier upgrade or overage package to continue
- Better for margin protection, worse for UX

**Option C: Automatic Tier Adjustment (Recommended)**
- Track rolling 3-month average usage
- Proactively recommend tier upgrade when trending over
- Apply temporary overage billing if spike
- Credit overage toward upgrade if customer upgrades within billing cycle

---

## Complete Pricing Examples

### Example 1: Single ASC (Simple)

| Component | Price |
|-----------|-------|
| Starter tier (1 location) | $149/mo |
| No add-ons | - |
| **Total** | **$149/mo ($1,788/yr)** |

### Example 2: 3-Location Surgical Center Group

| Component | Price |
|-----------|-------|
| Professional tier (up to 5 locations) | $399/mo |
| Surgical/OR category add-on | $99/mo |
| **Total** | **$498/mo ($5,976/yr)** |

### Example 3: 12-Location Regional Health System

| Component | Price |
|-----------|-------|
| Business tier (up to 20 locations) | $799/mo |
| Food & Dietary add-on | $99/mo |
| Pharmaceutical+ add-on | $149/mo |
| **Total** | **$1,047/mo ($12,564/yr)** |

### Example 4: 8-Location System (Exceeds Professional)

| Component | Price |
|-----------|-------|
| Professional tier (5 locations included) | $399/mo |
| 3 additional locations @ $69/mo | $207/mo |
| Clinical Bundle (Lab + Radiology + Surgical) | $199/mo |
| **Total** | **$805/mo ($9,660/yr)** |

*Note: At $805/mo, customer should consider Business tier at $799/mo for more locations and AI features*

### Example 5: Large Academic Medical Center (50 locations)

| Component | Price |
|-----------|-------|
| Enterprise base (custom) | $35,000/yr |
| All categories included | Included |
| Additional usage capacity | $10,000/yr |
| Implementation | $8,000 one-time |
| **Total** | **$45,000/yr + $8,000 implementation** |

### Example 6: High-Volume Hospital with Usage Overages

| Component | Price |
|-----------|-------|
| Business tier | $799/mo |
| Usage (15,000 alerts vs 10,000 limit) | $500/mo overage |
| AI queries (1,500 vs 1,000 limit) | $250/mo overage |
| **Total** | **$1,549/mo** |

*Recommendation: Upgrade to Enterprise to avoid overages and get unlimited capacity*

---

## Pricing Page Presentation

### What to Show Publicly

**Simple tier comparison** (Locations + Key Features):

| | Starter | Professional | Business | Enterprise |
|-|---------|--------------|----------|------------|
| **Price** | $149/mo | $399/mo | $799/mo | Custom |
| **Locations** | 1 | Up to 5 | Up to 20 | Unlimited |
| **AI Assistant** | Limited | Standard | Priority | Unlimited |
| **Categories** | Base | Base + Add-ons | Base + Bundles | All Included |
| **Support** | Help Center | Priority Email | Phone + Email | Dedicated CSM |

### What to Keep Behind Sales Conversations

- Detailed usage limits and overage rates
- Enterprise volume discounts
- Multi-year discount structures
- Custom category packaging
- Implementation pricing

### What to Show in Self-Service Dashboard

- Current usage vs. limits (progress bars)
- Projected overages
- Upgrade recommendations
- Category add-on prompts

---

## Implementation Considerations

### Feature Flag Architecture

```
User Entitlements:
├── tier: "professional"
├── locations_allowed: 5
├── locations_used: 3
├── categories: ["base", "surgical"]
├── usage_limits:
│   ├── alerts_monthly: 2500
│   ├── ai_queries_monthly: 200
│   ├── doc_scans_monthly: 500
│   └── api_calls_monthly: 10000
├── usage_current:
│   ├── alerts_monthly: 1847
│   ├── ai_queries_monthly: 156
│   ├── doc_scans_monthly: 234
│   └── api_calls_monthly: 4521
└── feature_flags:
    ├── ai_assistant: true
    ├── ai_matching: false
    ├── advanced_workflows: false
    ├── api_write: false
    └── sso: "ready"
```

### Billing System Requirements

1. **Subscription management**: Base tier + add-ons
2. **Usage metering**: Real-time tracking of all usage dimensions
3. **Overage calculation**: Monthly aggregation and billing
4. **Proration**: Handle mid-cycle upgrades/downgrades
5. **Location counting**: Validate active locations vs. allowance

### Metrics to Track

| Metric | Purpose |
|--------|---------|
| Usage-to-limit ratio by tier | Identify upgrade candidates |
| Category attach rate | Measure add-on success |
| Overage frequency | Tune limit levels |
| Tier upgrade conversion | Measure pricing effectiveness |
| Location expansion rate | Track growth within accounts |

---

## Competitive Positioning

### vs. TraceLink (Per-User Model)

| Dimension | RecallWire | TraceLink |
|-----------|------------|-----------|
| Primary metric | Locations | Users |
| Customer clarity | High (know location count) | Medium (user count varies) |
| Adoption friction | Low | High (license management) |
| Expansion model | Add locations + categories | Add users |
| Enterprise range | $25k-100k+ | $38k-67k+ (per intel) |

**Positioning**: "Simple, location-based pricing that grows with your organization—no per-seat licensing headaches."

### vs. OneRecall (Opaque Enterprise)

| Dimension | RecallWire | OneRecall |
|-----------|------------|-----------|
| Pricing transparency | Public tiers | Contact sales only |
| SMB accessibility | Yes (Starter tier) | No |
| Category flexibility | Modular add-ons | Bundled |
| AI features | Tiered access | Unknown (rapidID) |

**Positioning**: "Transparent pricing with AI-powered capabilities at a fraction of enterprise-only alternatives."

---

## Summary

This multi-dimensional model achieves your goals:

| Goal | How Addressed |
|------|---------------|
| **Customer comprehension** | Locations as primary metric |
| **Feature upsell path** | Tier-based feature gating with AI |
| **Industry expansion** | Category add-on modules |
| **Cost protection** | Usage limits with overage pricing |
| **Flexibility** | Multiple dimensions scale independently |
| **Competitive positioning** | Simpler than per-user, more transparent than enterprise-only |

The key insight: **Keep the customer-facing model simple (locations + tier + categories) while using usage limits internally to protect margins.**
