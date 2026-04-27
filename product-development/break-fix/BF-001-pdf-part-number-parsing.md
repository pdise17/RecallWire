# BF-001 — PDF Part Number Parsing & PO Match Discrepancy

| Field | Detail |
|---|---|
| **ID** | BF-001 |
| **Reported By** | Chris Paradise, Co-Founder / Product Validator |
| **Date Reported** | 2026-04-16 |
| **Severity** | High |
| **Status** | Open |
| **Component** | PDF Analyzer → Purchase Order History Matching |

---

## Summary

The PDF analyzer is not consistently parsing the correct part numbers from recall documents. When part numbers are parsed, there are downstream discrepancies when attempting to match those part numbers against the facility's purchase order history.

---

## Observed Behavior

**Issue 1 — Inconsistent Part Number Extraction**
- The PDF analyzer does not reliably extract affected part numbers from recall notification PDFs.
- Parsing failures appear intermittent — some part numbers are captured correctly while others in the same document are missed or misread.

**Issue 2 — PO Match Discrepancies**
- Even when part numbers are parsed correctly, the system fails to consistently match them against purchase order history records.
- This results in either false negatives (affected product not flagged) or unmatched results where a match should clearly exist.

---

## Impact

- Facilities may not be alerted to recalled product they have on hand.
- Manual verification is required to compensate, undermining the core value proposition of automated recall-to-inventory matching.
- Audit-readiness documentation cannot be trusted if the underlying match is unreliable.
- Direct risk to patient safety and Joint Commission compliance.

---

## Steps to Reproduce

1. Upload a recall notification PDF containing multiple affected part/lot numbers.
2. Observe parsed part numbers in the system output.
3. Cross-reference parsed numbers against the source PDF — note any missing or incorrect extractions.
4. For correctly parsed numbers, run PO history match.
5. Compare matched results against known PO records containing the same part numbers — note any unmatched or incorrectly matched entries.

---

## Expected Behavior

- All affected part numbers listed in a recall PDF should be extracted accurately and completely.
- Extracted part numbers should match against PO history records where an exact or near-exact match exists, accounting for known formatting variations (e.g., leading zeros, dashes, spacing).

---

## Hypotheses / Areas to Investigate

| Area | Notes |
|---|---|
| PDF text extraction | OCR vs. native text — scanned PDFs may produce garbled part numbers |
| Part number format normalization | Dashes, spaces, leading zeros, and case may vary between recall doc and PO record |
| Regex / parsing pattern coverage | Parser may not account for all part number formats used across manufacturers |
| PO record field mapping | Part number field in PO history may not align with the field being matched against |
| Fuzzy vs. exact matching | System may be using strict exact match where fuzzy/normalized matching is needed |

---

## Attachments / Reference Material

- [ ] Sample recall PDF that exhibited the parsing failure
- [ ] Screenshot of parsed output vs. expected part numbers
- [ ] Sample PO history record showing the unmatched part number
- [ ] Any error logs or console output from the analyzer

---

## Developer Notes

> *(Developer to populate during investigation)*

---

## Resolution

> *(To be completed upon fix)*

| Field | Detail |
|---|---|
| **Fixed By** | |
| **Date Resolved** | |
| **Fix Description** | |
| **Commit / PR** | |
