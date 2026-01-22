# TAM Analysis - January 2025

## Overview

Analysis of Total Addressable Market (TAM) for RecallWire across 4,555 US hospitals with recommended package assignments and pricing.

## Summary

| Metric | Value |
|--------|-------|
| **Total Hospitals** | 4,555 |
| **Total TAM** | $102.8M |
| **Average Deal Size** | $22,576 |

### Package Distribution

| Package | Count | % | Avg Price | TAM |
|---------|------:|---:|----------:|----:|
| Standard | 1,773 | 38.9% | $5,000 | $8.9M |
| Enterprise | 2,197 | 48.2% | $27,201 | $59.8M |
| Enterprise Plus | 467 | 10.3% | $51,991 | $24.3M |
| Enterprise Premier | 118 | 2.6% | $84,148 | $9.9M |

## Pricing Formula

### Tier Assignment (by bed count)

| Beds | Package |
|------|---------|
| <50 | Standard |
| 50-399 | Enterprise |
| 400-799 | Enterprise Plus |
| 800+ | Enterprise Premier |

### Pricing Calculation

```
Standard:
  $4,999/year (flat)

Enterprise:
  $20,000 + (beds - 50) × $50 + (revenue_$M / 20)
  Range: $20,000 - $44,999

Enterprise Plus:
  $45,000 + (beds - 400) × $50 + (revenue_$M / 15)
  Range: $45,000 - $74,999

Enterprise Premier:
  $75,000 + (beds - 800) × $30 + (revenue_$M / 10)
  Range: $75,000+
```

### Formula Rationale

1. **Beds as primary driver**: Bed count is the strongest proxy for device complexity, department count, and recall management burden.

2. **Revenue as secondary factor**: Scales pricing within tiers based on organizational budget capacity.

3. **Clear thresholds**: 50/400/800 bed thresholds create defensible, easy-to-explain tier boundaries.

## Files

| File | Description |
|------|-------------|
| `dashboard.html` | Interactive dashboard for strategy team demos |
| `hospitals_pricing.csv` | Full dataset with package assignments |
| `dashboard_data.json` | Aggregated data for dashboard |

## Usage

Open `dashboard.html` in any browser - no server required. The dashboard includes:

- Summary metrics
- TAM by package tier (bar chart)
- Hospital count by package (donut chart)
- TAM by bed size distribution
- Top 10 states by TAM
- Searchable/filterable top 50 opportunities table
- Pricing formula reference

## Guardrails & Considerations

### Usage Scaling

Larger hospitals are assigned higher tiers with increased usage limits:

| Tier | Alerts/mo | AI Queries/mo | Support Level |
|------|-----------|---------------|---------------|
| Standard | 2,500 | 500 | Email (24hr) |
| Enterprise | 10,000 | 2,000 | Phone (8hr) |
| Enterprise Plus | 25,000 | 5,000 | Dedicated CSM |
| Enterprise Premier | 50,000+ | Unlimited | Dedicated Team |

### Operational Overhead

Pricing scales with expected support burden:
- Larger hospitals = more stakeholders = more support tickets
- Enterprise+ tiers include dedicated CSM to handle complexity
- Premier tier pricing supports dedicated implementation teams

### 50-Bed Cliff

The jump from Standard ($5K) to Enterprise ($20K) at 50 beds is steep but defensible:
- 50+ bed hospitals have 4-5+ departments with device inventories
- Same Joint Commission requirements as larger facilities
- Sales can offer RMaaS bundles for price-sensitive 50-99 bed hospitals

## Data Sources

- Hospital data: `hospitals_enriched.csv` (4,555 US hospitals)
- Pricing model: `deliverables/06-multi-dimensional-pricing-model.md`
- Analysis date: January 2025
