# RecallWire Pricing Strategy Recommendations

## Executive Summary

RecallWire faces a fundamental pricing challenge: the platform is built to enterprise-grade specifications ($40k+/year value) but needs to serve non-enterprise customers at ~$2,000/year per location. This analysis recommends a **4-tier pricing structure** with transparent public pricing, designed to capture the underserved SMB market while preserving enterprise revenue.

**Key Recommendation:** Be the first competitor to publish clear, public pricing tiers.

---

## Recommended Pricing Structure

### Tier Overview

| Tier | Monthly Price | Annual Price | Target Customer | Locations |
|------|---------------|--------------|-----------------|-----------|
| **Starter** | $149/mo | $1,499/yr | Single-facility clinics, ASCs | 1 |
| **Professional** | $399/mo | $3,999/yr | Multi-site practices, small hospitals | 2-5 |
| **Business** | $799/mo | $7,999/yr | Regional health systems | 6-20 |
| **Enterprise** | Custom | $25,000+/yr | Large health systems | 21+ |

---

## Detailed Tier Specifications

### Tier 1: Starter ($149/month or $1,499/year)

**Target Customer:**
- Single-facility clinics
- Ambulatory Surgery Centers (ASCs)
- Imaging centers
- Physician groups
- Small practices needing compliance coverage

**Included Features:**
- Real-time FDA recall alerts
- Basic inventory matching (CSV upload)
- Core dashboard
- Email notifications
- Guided resolution workflow
- Audit trail and compliance documentation
- Help center access
- RecallWire Assistant (limited queries)

**Excluded Features:**
- Multi-facility hierarchy
- SLA escalations
- Department routing
- API access
- SSO
- Priority support

**Operational Model:**
- Self-service onboarding
- No dedicated CSM
- Community support + help center
- Automated billing (credit card)

**Justification:**
- Price point: $1,499/year = ~$125/month, competitive with user's $2,000/location target
- Self-service model keeps CAC and support costs low
- Captures underserved SMB market completely ignored by competitors
- TraceLink offers "3 sites free" but with limited features; this tier offers full core workflow

---

### Tier 2: Professional ($399/month or $3,999/year)

**Target Customer:**
- Multi-site practices (2-5 locations)
- Small community hospitals
- Specialty clinic networks
- Growing ASC groups

**Included Features:**
Everything in Starter, plus:
- Multi-facility hierarchy (up to 5 locations)
- Department mapping and routing
- Basic SLA tracking
- Advanced dashboards
- Priority email support
- API access (read-only)
- SSO readiness
- RecallWire Assistant (standard queries)
- Quarterly business reviews (virtual)

**Excluded Features:**
- Custom workflows
- API write access
- Sandbox environments
- Dedicated CSM
- Security/compliance reviews

**Operational Model:**
- Guided self-service onboarding
- Priority email support (24hr SLA)
- Monthly usage reports
- Virtual QBRs

**Justification:**
- $3,999/year ÷ 5 locations = $800/location/year (below $2k target)
- Bridges gap between self-service and enterprise
- Matches PAR/NotiSphere positioning but with clearer value
- Multi-facility features justify 2.6x price increase from Starter

---

### Tier 3: Business ($799/month or $7,999/year)

**Target Customer:**
- Regional health systems (6-20 locations)
- Mid-market hospital networks
- Large ASC chains
- Growing health systems pre-enterprise

**Included Features:**
Everything in Professional, plus:
- Extended multi-facility support (up to 20 locations)
- Advanced SLA management and escalations
- Custom department workflows
- API access (read + write)
- Dedicated success manager (shared)
- Phone support
- Quarterly business reviews (in-person option)
- RecallWire Assistant (priority access)
- Custom reporting

**Excluded Features:**
- Sandbox environments
- Premium security reviews
- Dedicated CSM (1:1)
- Custom integrations
- Data retention customization

**Operational Model:**
- White-glove onboarding
- Shared CSM (1:many)
- Phone + email support
- Implementation consulting included

**Justification:**
- $7,999/year ÷ 20 locations = $400/location/year (well below target)
- Volume discount rewards growth
- Competes with ECRI and OneRecall on features at fraction of price
- Natural upsell path from Professional

---

### Tier 4: Enterprise (Custom, starting $25,000/year)

**Target Customer:**
- Large health systems (21+ locations)
- Academic medical centers
- National hospital chains
- Complex multi-entity organizations

**Included Features:**
Everything in Business, plus:
- Unlimited locations
- Sandbox/staging environments
- Custom integrations and workflows
- Dedicated Customer Success Manager (1:1)
- Premium support (SLA-backed, 4hr response)
- Security and compliance reviews
- Custom data retention policies
- Executive business reviews
- Dedicated implementation team
- Volume-based pricing discounts
- Custom contract terms

**Operational Model:**
- Consultative sales process
- Dedicated implementation team
- Named CSM
- Premium SLA-backed support
- Annual/multi-year contracts

**Pricing Model:**
- Base: $25,000/year (21-50 locations)
- Additional locations: ~$400-500/location/year (volume discounts apply)
- Implementation: $5,000-15,000 one-time
- Custom integrations: Quoted separately

**Justification:**
- Preserves enterprise revenue stream
- Matches competitors on features and support
- Custom pricing allows flexibility for large deals
- Implementation fees offset high-touch costs

---

## Feature Segmentation Matrix

| Feature | Starter | Professional | Business | Enterprise |
|---------|---------|--------------|----------|------------|
| **Real-time FDA Alerts** | Yes | Yes | Yes | Yes |
| **Non-FDA Alerts** | Limited | Yes | Yes | Yes |
| **Locations Included** | 1 | 5 | 20 | Unlimited |
| **Data Import** | CSV | CSV + Basic API | Full API | Custom |
| **Inventory Matching** | Basic | Advanced | Advanced+ | Custom |
| **PO Matching** | No | Basic | Advanced | Custom |
| **Guided Resolution** | Yes | Yes | Yes | Custom |
| **Audit Trail** | Yes | Yes | Yes | Enhanced |
| **Dashboards** | Core | Advanced | Custom | Custom |
| **Department Routing** | No | Basic | Advanced | Custom |
| **SLA Management** | No | Basic | Advanced | Custom |
| **Escalations** | Email | Email | Multi-channel | Custom |
| **API Access** | No | Read | Read/Write | Full |
| **SSO** | No | Ready | Yes | Yes |
| **RecallWire Assistant** | Limited | Standard | Priority | Unlimited |
| **Support** | Help Center | Priority Email | Phone + Email | Premium SLA |
| **CSM** | No | No | Shared | Dedicated |
| **Onboarding** | Self-service | Guided | White-glove | Dedicated |
| **Security Review** | No | No | Basic | Premium |
| **Sandbox** | No | No | No | Yes |
| **Custom Workflows** | No | No | Limited | Yes |
| **Data Retention** | Standard | Standard | Standard | Custom |

---

## Pricing Rationale

### Addressing the Core Challenge

**Problem:** Enterprise-grade product ($40k+) needs to serve $2k/location customers.

**Solution Components:**

1. **Feature Segmentation**: Clear boundaries justify tier differences
2. **Self-Service for SMB**: Dramatically reduces CAC and support costs for lower tiers
3. **Per-Location Scaling**: Value scales with customer size
4. **Preserved Enterprise Value**: Full-featured tier maintains revenue from large accounts

### Unit Economics by Tier

| Tier | Revenue | Est. CAC | Est. Support Cost | Est. Margin |
|------|---------|----------|-------------------|-------------|
| **Starter** | $1,499/yr | $200 (PLG) | $100/yr | 80%+ |
| **Professional** | $3,999/yr | $800 | $400/yr | 70%+ |
| **Business** | $7,999/yr | $2,000 | $1,200/yr | 65%+ |
| **Enterprise** | $25,000+/yr | $8,000 | $4,000/yr | 60%+ |

### Competitive Positioning

| Competitor | Their Positioning | RecallWire Advantage |
|------------|-------------------|---------------------|
| **OneRecall** | Enterprise-only, opaque pricing | Transparent tiers, SMB access |
| **ECRI** | Premium, bundled services | Standalone, clear value |
| **PAR/NotiSphere** | Budget, but still opaque | Transparent, better features |
| **TraceLink** | Free tier, pharmacy focus | Broader coverage, full workflow |

---

## Modularizable Features for Future Add-ons

These features can be offered as paid add-ons to increase ARPU:

### Potential Add-ons

| Add-on | Price Suggestion | Available Tiers |
|--------|------------------|-----------------|
| **Additional Locations** | $99/mo per location | Starter, Professional |
| **API Write Access** | $199/mo | Professional |
| **Advanced Integrations** | $299-499/mo | Professional, Business |
| **Premium Support Upgrade** | $199/mo | Starter, Professional |
| **Additional RecallWire Assistant Queries** | $49/mo pack | All |
| **Custom Reporting Pack** | $149/mo | Professional, Business |
| **Extended Data Retention** | $99/mo | All (except Enterprise) |
| **Dedicated Training Session** | $500 one-time | All |

### Add-on Strategy

1. **Start Simple**: Launch with clean tiers, minimal add-ons
2. **Track Friction**: Identify features customers frequently request upgrades for
3. **Modularize Gradually**: Add modules based on demand signals
4. **Preserve Tier Value**: Don't let add-ons cannibalize tier upgrades

---

## Volume Discounts

### Annual Prepay Discounts

| Payment Term | Discount |
|--------------|----------|
| Monthly | 0% |
| Annual Prepay | ~17% (2 months free) |
| Multi-year (2+) | 20-25% negotiated |

### Location Volume Discounts (Enterprise)

| Locations | Per-Location Rate |
|-----------|-------------------|
| 21-50 | $500/location/yr |
| 51-100 | $450/location/yr |
| 101-200 | $400/location/yr |
| 200+ | Custom negotiated |

---

## Go-to-Market Considerations

### Starter Tier (PLG Motion)

- **Acquisition**: SEO, content marketing, product-led growth
- **Conversion**: Free trial → self-service purchase
- **Success Metrics**: Time to value, activation rate, self-service conversion
- **Key Investment**: Onboarding UX, help center, in-app guidance

### Professional Tier (Hybrid Motion)

- **Acquisition**: Inbound leads, referrals, targeted outreach
- **Conversion**: Demo → guided trial → sales-assisted close
- **Success Metrics**: Qualified pipeline, demo-to-close rate
- **Key Investment**: Sales capacity, demo automation

### Business/Enterprise (Sales-Led Motion)

- **Acquisition**: Account-based marketing, industry events, referrals
- **Conversion**: Discovery → demo → pilot → contract
- **Success Metrics**: Enterprise pipeline, deal size, retention
- **Key Investment**: Enterprise sales team, CSM capacity, implementation services

---

## Risk Considerations

### Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| **Cannibalization**: Enterprises downgrade to lower tiers | Clear feature gates, enterprise-only features (sandbox, custom workflows, security reviews) |
| **Support Overwhelm**: SMB volume strains resources | Self-service first, automate onboarding, community support |
| **Price Sensitivity**: SMB churn on price | Annual prepay discounts, value demonstration, stickiness through workflow integration |
| **Enterprise Perception**: Lower tiers hurt brand | Separate messaging, enterprise-focused sales materials |
| **Competitor Response**: PAR/others match pricing | First-mover on transparency, feature differentiation, UX/AI advantage |

---

## Summary Recommendation

1. **Launch 4-tier structure** with transparent public pricing
2. **Lead with $149/month Starter** to capture underserved SMB market
3. **Maintain $25k+ Enterprise** to preserve high-value relationships
4. **Invest in self-service** to make lower tiers sustainable
5. **Use add-ons sparingly** initially, expand based on demand
6. **Be first to publish pricing** as competitive differentiator

*Implementation timeline in deliverable #4.*
