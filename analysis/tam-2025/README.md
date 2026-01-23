# TAM Analysis - January 2025

## Overview

Analysis of Total Addressable Market (TAM) for RecallWire across 4,555 US hospitals with health system classification and tiered pricing.

## Summary

| Metric | Value |
|--------|-------|
| **Total Hospitals** | 4,555 |
| **Individual TAM** | $108.3M |
| **Realistic TAM** | $46.9M |
| **Health Systems Identified** | 408 |
| **System Members** | 2,042 (44.8%) |
| **Independent Hospitals** | 2,513 (55.2%) |

### TAM Breakdown

| Component | Value | Description |
|-----------|-------|-------------|
| **System-Level TAM** | $9.1M | Revenue from system deals (volume pricing) |
| **Independent TAM** | $37.8M | Revenue from independent hospitals |
| **Realistic TAM** | $46.9M | Combined addressable market |

### Package Distribution

| Package | Count | % | Description |
|---------|------:|---:|-------------|
| Standard | 1,773 | 38.9% | <50 beds |
| Enterprise | 2,197 | 48.2% | 50-399 beds |
| Enterprise Plus | 467 | 10.3% | 400-799 beds |
| Enterprise Premier | 118 | 2.6% | 800+ beds |

### Segment Distribution

| Segment | Count | Description |
|---------|------:|-------------|
| Community | 3,924 | Standard community hospitals |
| Regional | 497 | Regional medical centers |
| Academic | 72 | Academic medical centers |
| Critical Access | 35 | Rural critical access hospitals |
| Specialty | 27 | Specialty hospitals |

## Health System Classification

### Methodology

Config-driven pattern matching using `configs/health_systems.yaml` (v2.4):

1. **City Patterns**: Match hospital name + city for precise identification
2. **State Patterns**: Match hospital name within specific states
3. **General Patterns**: Match hospital name across all states
4. **Exclude Patterns**: Prevent false positives

### Top Health Systems by Hospital Count

| System | Hospitals |
|--------|----------:|
| HCA Healthcare | 95 |
| Ascension | 69 |
| CommonSpirit Health | 60 |
| Providence | 46 |
| AdventHealth | 38 |
| Kaiser Permanente | 37 |
| Baylor Scott & White Health | 33 |
| Mercy (Midwest) | 32 |
| Trinity Health | 28 |
| Baptist Health (Multi-state) | 27 |

### System Pricing

Health systems receive volume-based pricing:

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

## Files

### Core Data Files

| File | Description |
|------|-------------|
| `hospitals_classified.csv` | Full dataset with system classification and pricing |
| `hospitals_pricing.csv` | Source hospital data with pricing |
| `classification_summary.json` | Current classification statistics |

### Configuration

| File | Description |
|------|-------------|
| `configs/health_systems.yaml` | Health system patterns (v2.4, 408 systems) |
| `configs/classification.yaml` | Tier and pricing configuration |

### Scripts

| File | Description |
|------|-------------|
| `scripts/classify_hospitals.py` | Main classification workflow |
| `scripts/state_analysis.py` | State-by-state analysis for pattern discovery |
| `scripts/evaluate_matching.py` | Matching evaluation tools |

### Dashboards

| File | Description |
|------|-------------|
| `executive-dashboard.html` | Full executive dashboard |
| `dashboard.html` | Simple interactive dashboard |

## Usage

### Run Classification

```bash
cd /Users/justin/repo/biz-recallwire/analysis/tam-2025
python3 scripts/classify_hospitals.py
```

### Analyze Remaining Independents

```bash
python3 scripts/state_analysis.py
```

## Data Sources

- Hospital data: Apollo/ZoomInfo hospital list (4,555 US hospitals)
- Pricing model: `deliverables/06-multi-dimensional-pricing-model.md`
- Analysis date: January 2025
