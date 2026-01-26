# RecallWire Collateral

Marketing collateral and sales materials for RecallWire.

## Directory Structure

```
collateral/
├── README.md                    # This file
├── assets/
│   └── logos/
│       ├── recallwire.png       # Wordmark (black + teal accents)
│       └── rmaas.png            # RMaaS ram icon
├── templates/
│   └── one-pager-template.html  # Base template with placeholders
├── executive-one-pager.html     # Complete example
└── [other generated files]      # Operations, technical, etc.
```

## One-Pager Generator

Use the `/one-pager` skill to generate professional HTML one-pagers:

```
/one-pager --type executive
/one-pager --type operations
/one-pager --type technical
```

### One-Pager Types

| Type | Audience | Focus |
|------|----------|-------|
| `executive` | C-Suite, Risk Managers | Compliance risk, audit readiness, strategic value |
| `operations` | Materials Managers, Supply Chain | Time savings, workflow efficiency |
| `technical` | IT Directors, Security | Architecture, integrations, implementation |

### Output

Generated one-pagers are saved to this directory as HTML files. To convert to PDF:

1. Open the HTML file in a browser
2. Print to PDF (Cmd+P / Ctrl+P)
3. Select "Save as PDF" as destination
4. Use default margins or "None"

## Logo Usage

Two logo options are available:

| Logo | File | Best For |
|------|------|----------|
| **Wordmark** | `recallwire.png` | Light backgrounds, print |
| **RMaaS Icon** | `rmaas.png` | RMaaS-specific materials, favicons |

**On dark backgrounds** (like the navy header), use the CSS text treatment instead of the PNG. The text treatment mimics the wordmark with white text and teal accents on the "A" and "I".

## Brand Colors

| Color | Hex | Usage |
|-------|-----|-------|
| Primary Blue | #1E3A5F | Headers, trust elements |
| Accent Teal | #00B4A0 | CTAs, highlights, logo accents |
| Alert Red | #DC2626 | Urgency (use sparingly) |
| Dark Gray | #1F2937 | Body text |
| Light Gray | #F9FAFB | Backgrounds |

## Related Files

- **Brand Guide:** `creatives/brand-foundation.md`
- **Content Reference:** `creatives/one-pagers-content.md`
- **Skill Definition:** `.claude/skills/one-pager.md`
