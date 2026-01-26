# One-Pager Generator

Generate professional HTML one-pagers for RecallWire. This skill creates print-ready marketing collateral.

## Usage

```
/one-pager --type <type> [--output <filename>]
```

### Parameters

- `--type` (required): Type of one-pager to generate
  - `executive` - C-Suite focused: compliance risk, audit readiness, strategic value
  - `operations` - Materials/Supply Chain: workflow efficiency, time savings, day-to-day benefits
  - `technical` - IT/Security: architecture, integrations, implementation timeline

- `--output` (optional): Output filename (default: auto-generated based on type)

### Examples

```
/one-pager --type executive
/one-pager --type operations
/one-pager --type technical --output q1-sales-collateral.html
```

## Instructions for Claude

When this skill is invoked:

### 1. Read Brand Context (REQUIRED FIRST STEP)

**Always read `CLAUDE.md` first** to get company-specific information:
- Company name: RecallWire
- Brand colors:
  - Primary Blue: #1E3A5F (headers, trust elements)
  - Accent Teal: #00B4A0 (CTAs, highlights, AI elements)
  - Alert Red: #DC2626 (urgency, use sparingly)
  - Text Dark: #1F2937 (body copy)
  - Background Light: #F9FAFB (cards, backgrounds)
- Logo: Wordmark "RECALLWIRE" stacked as "RECALL" / "WIRE" with teal accents on "A" and "I"
- Tagline: "Respond to recalls 10x faster with complete compliance documentation"
- Website: https://www.recallwire.com
- LinkedIn: https://www.linkedin.com/company/recall-wire/
- Key metrics (use exact values from CLAUDE.md)

### 2. Check for existing templates and content

Look for these files:
- Template: `collateral/templates/one-pager-template.html`
- Content reference: `creatives/one-pagers-content.md`
- Brand guide: `creatives/brand-foundation.md`
- Existing one-pagers in `collateral/` directory

### 3. Generate content based on type

**For `executive` type:**
- Audience: C-Suite, Risk Managers, Board presentations
- Lead with: Compliance risk, audit readiness, liability protection
- Stats emphasis: 10x faster, 100% audit traceability, 75+ Class I recalls
- Tone: Strategic, ROI-focused
- Sections: The Compliance Challenge + RecallWire Delivers

**For `operations` type:**
- Audience: Materials Managers, Supply Chain Directors, Quality
- Lead with: Time savings (40 hours → 4), workflow efficiency
- Stats emphasis: 40→4 hours, 98% noise reduction, 60% fewer manual steps
- Tone: Practical, day-in-the-life focused
- Sections: Current Reality (pain) + RecallWire Workflow (solution)

**For `technical` type:**
- Audience: IT Directors, Security Officers, Integration teams
- Lead with: Security (SOC 2), fast implementation, minimal IT lift
- Stats emphasis: 4-8 weeks implementation, SOC 2, API-ready, SSO
- Tone: Technical but accessible
- Sections: Security/Compliance + Integration + Deployment Timeline

### 4. Apply design standards

**Colors** (from CLAUDE.md):
- Primary (Navy Blue): #1E3A5F
- Accent (Teal): #00B4A0
- White: #FFFFFF
- Light Gray: #F9FAFB
- Dark Gray: #1F2937
- Light Teal (callouts): #E6FAF8
- Header background: Navy gradient

**Icons** - Lucide-style SVG:
- ViewBox: `0 0 24 24`
- Stroke width: `2`
- Fill: `none`
- Stroke linecap/linejoin: `round`

**Typography**:
- Font: Inter or Montserrat (Google Fonts)
- Headers: 700 weight
- Body: 400 weight

**Page setup**:
- Size: 8.5in x 11in (US Letter)
- Include print-specific CSS
- No `flex: 1` on content sections (causes PDF overflow)

### 5. Output the file

- Save to `collateral/` directory
- Naming: `[type]-one-pager.html` (e.g., `executive-one-pager.html`)
- Confirm file location to user

### 6. Provide next steps

- Remind user to review and customize
- Note any placeholders needing updates
- Suggest opening in browser and printing to PDF

---

## Key Metrics Reference

Use these exact values in all one-pagers:

| Metric | Value | Context |
|--------|-------|---------|
| Speed | 10x faster | Recall response time (40 hrs → 4 hrs) |
| Noise reduction | 98% | Alerts filtered (150K → ~3K relevant) |
| Manual steps | 60% reduction | Workflow automation |
| Audit trail | 100% | Complete traceability |
| Implementation | 4-8 weeks | Time to go live |
| Manual effort | 40+ hours | Current pain point per recall |
| Class I recalls | 75+ in 2024 | 15-year high (urgency stat) |
| ROI | 747% | Mid-size health system |

---

## Icon Reference

Lucide-style SVG icons (24px viewBox, 2px stroke, no fill):

```svg
<!-- Shield (Security/Compliance) -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/>
</svg>

<!-- Clock (Time/Speed) -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="12" r="10"/>
  <polyline points="12 6 12 12 16 14"/>
</svg>

<!-- Activity (Monitoring) -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
</svg>

<!-- Search (Detection/Matching) -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="11" cy="11" r="8"/>
  <path d="m21 21-4.3-4.3"/>
</svg>

<!-- CheckCircle (Resolution/Complete) -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="12" r="10"/>
  <path d="m9 12 2 2 4-4"/>
</svg>

<!-- FileText (Documentation) -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
  <polyline points="14 2 14 8 20 8"/>
  <line x1="16" y1="13" x2="8" y2="13"/>
  <line x1="16" y1="17" x2="8" y2="17"/>
  <line x1="10" y1="9" x2="8" y2="9"/>
</svg>

<!-- AlertTriangle (Recalls/Urgency) -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/>
  <line x1="12" y1="9" x2="12" y2="13"/>
  <line x1="12" y1="17" x2="12.01" y2="17"/>
</svg>

<!-- Workflow (Process) -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <polyline points="16 3 21 3 21 8"/>
  <line x1="4" y1="20" x2="21" y2="3"/>
  <polyline points="21 16 21 21 16 21"/>
  <line x1="15" y1="15" x2="21" y2="21"/>
  <line x1="4" y1="4" x2="9" y2="9"/>
</svg>

<!-- Server (Integration/API) -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect width="20" height="8" x="2" y="2" rx="2" ry="2"/>
  <rect width="20" height="8" x="2" y="14" rx="2" ry="2"/>
  <line x1="6" x2="6.01" y1="6" y2="6"/>
  <line x1="6" x2="6.01" y1="18" y2="18"/>
</svg>

<!-- Lock (Security) -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect width="18" height="11" x="3" y="11" rx="2"/>
  <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
</svg>

<!-- Users (Team/Assignment) -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>
  <circle cx="9" cy="7" r="4"/>
  <path d="M22 21v-2a4 4 0 0 0-3-3.87"/>
  <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
</svg>

<!-- Building (Healthcare Facility) -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect x="4" y="2" width="16" height="20" rx="2"/>
  <path d="M9 22v-4h6v4"/>
  <path d="M8 6h.01M16 6h.01M12 6h.01M8 10h.01M16 10h.01M12 10h.01M8 14h.01M16 14h.01M12 14h.01"/>
</svg>
```

---

## Three-Step Product Summary

Use this in intro sections:

> **Detect** real-time FDA monitoring | **Match** AI-powered inventory matching | **Resolve** guided workflows with auto-documentation

---

## Pricing Reference (if needed)

| Tier | Price | Target |
|------|-------|--------|
| Standard | $4,999/year | 1-5 locations |
| Enterprise | Starting $25,000/year | 6+ locations |

---

## Competitive Advantages (for differentiation sections)

- **vs. Inmar/OneRecall:** Modern AI, transparent pricing, 4-8 week implementation vs 6+ months
- **vs. ECRI:** 1/3 the cost, comparable coverage, faster setup
- **vs. PAR Excellence:** Complete lifecycle (not just notifications), audit documentation
