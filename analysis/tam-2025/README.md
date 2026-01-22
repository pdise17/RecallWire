# TAM Analysis - January 2025

## Overview

Analysis of Total Addressable Market (TAM) for RecallWire across 4,555 US hospitals with recommended package assignments and pricing.

## Summary

| Metric | Value |
|--------|-------|
| **Total Hospitals** | 4,555 |
| **Individual TAM** | $102.8M |
| **Realistic TAM** | $79.8M |
| **TAM Reduction (System Discounts)** | $23.0M (22.4%) |
| **Average Deal Size** | $17,520 (blended) |

### System-Level Pricing

Health systems receive volume-based pricing that significantly reduces per-hospital cost:

| Metric | Value |
|--------|-------|
| **Health Systems Identified** | 51 (pattern-matched) |
| **Hospitals in Systems** | 916 (20.1%) |
| **Independent Hospitals** | 3,639 (79.9%) |
| **System-Level TAM** | $3.8M |
| **Independent TAM** | $76.0M |
| **Average Per-Hospital (System)** | $4,000-$7,000 |

**Mount Sinai Validation:** 5 hospitals @ $30,000 total ($6,000/hospital) - within target range of $25,000-$45,000

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

## Health System Rollup (V2 - Data-Driven)

### Summary

| Metric | Value |
|--------|-------|
| **Health Systems Identified** | 16 (verified) |
| **Affiliated Hospitals** | 473 |
| **System-Level TAM** | $1.8M |
| **Individual TAM (same hospitals)** | $12.9M |
| **Average Discount vs Individual** | ~87% |

### System Pricing Formula (V2)

**Key Insight:** Mount Sinai (7 hospitals) rejected $50K packages. Target is $25-45K.

System deals use per-hospital complexity pricing:

```
Base Price: $4,000 per hospital

Size Multipliers:
  Small (<200 beds): 1.0x = $4,000
  Medium (200-500 beds): 1.25x = $5,000
  Large (500-1000 beds): 1.5x = $6,000
  Enterprise (1000+ beds): 1.75x = $7,000

System Size Discount:
  2-5 hospitals: 5%
  6-15 hospitals: 10%
  16-50 hospitals: 15%
  51+ hospitals: 20%
```

### Top 10 Health Systems

| System | Hospitals | Individual TAM | System Deal | Per Hospital |
|--------|----------:|--------------:|------------:|-------------:|
| HCA Healthcare | 147 | $3.81M | $533K | $3,624 |
| Ascension | 84 | $2.18M | $308K | $3,667 |
| CommonSpirit Health | 80 | $1.68M | $278K | $3,470 |
| Providence | 39 | $1.01M | $150K | $3,836 |
| Kaiser Permanente | 37 | $1.20M | $149K | $4,022 |
| St. Luke's (PA) | 23 | $438K | $82K | $3,583 |
| NYC Health + Hospitals | 12 | $533K | $56K | $4,650 |
| CHI St. Luke's (TX) | 10 | $263K | $40K | $3,960 |
| **Mount Sinai** | **6** | **$369K** | **$32K** | **$5,250** |
| Northwell Health | 8 | $423K | $41K | $5,175 |

### Strategic Value

**Why target health systems?**

1. **Sales Efficiency:** 16 verified system deals covers 473 hospitals (30x leverage)
2. **Predictable Revenue:** Multi-year enterprise contracts
3. **Reduced CAC:** One procurement cycle per system
4. **Expansion Potential:** Land-and-expand within system

### Mount Sinai Case Study

| Metric | Value |
|--------|-------|
| **Hospitals in System** | 5-6 (in dataset) |
| **Individual TAM** | $284,300 - $368,800 |
| **System Deal** | $26,600 - $31,500 |
| **Per Hospital** | $5,250 - $5,320 |
| **Target Range** | $25,000 - $45,000 |
| **Status** | Within target range |

*Note: Some Mount Sinai facilities (Morningside, Queens, Brooklyn) not in dataset*

## Files

| File | Description |
|------|-------------|
| `executive-dashboard.html` | **Primary** - Full executive dashboard with 7 tabs + Data Explorer |
| `dashboard.html` | Simple interactive dashboard for quick demos |
| `hospitals_pricing.csv` | Full dataset with individual package assignments |
| `dashboard_data.json` | Aggregated data for dashboard |
| `health_systems.json` | Original health system rollup data |
| `health_systems_consolidated.json` | **V2** - Data-driven system consolidation with validated pricing |
| `scripts/health_system_consolidation.py` | Script for data-driven health system identification |

## Usage

Open `executive-dashboard.html` in any browser - no server required. The dashboard includes:

- Executive Summary with realistic TAM ($79.8M)
- Market Overview (regions, states, bed cohorts)
- Segment Analysis
- **Health Systems** with verified system-level pricing
- Revenue Projections (3-year scenarios)
- Competitive Landscape
- GTM Strategy
- Data Explorer with filters

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
