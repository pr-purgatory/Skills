# People Search Disambiguation: Worked Example

All names, numbers, and addresses below are fictional placeholders.

## Session Context
Research Target: `{Target Name}`
Query Details: phone `{phone}`, address `{street}, {city} {state}`
Stated purpose: `{purpose}` (required before starting person research)

---

## Problem: Multiple Individuals with Same/Similar Name

Public records research frequently surfaces **multiple distinct individuals** with the same or similar names. Failing to disambiguate leads to conflated identities, false criminal associations, and inaccurate reporting.

---

## Disambiguation Methodology

### Step 1: Initial Broad Search
Run multiple query variations to capture all potential matches:
```
"{Target Name}" + phone number
"{Target Name}" + full address
"{Target Name}" + city + state
"{Spelling Variant}" + state
```

### Step 2: Identify Distinct Records
Look for diverging attributes that indicate separate individuals:
- **Age differences** (e.g., 36 vs 45 vs 54)
- **Geographic separation** (different states in the same period)
- **Middle names** (e.g., "Alex Q. Doe" vs "Alex Doe")
- **Associated persons** (family, co-residents)
- **Records tied to specific addresses**

### Step 3: Document Each Individual Separately

| Attribute | Individual A | Individual B | Individual C |
|-----------|-------------|-------------|-------------|
| **Name** | Alex Doe | Alex Doe | Alex Q. Dough |
| **Age** | ~36 | ~45 | ~54 |
| **Location** | City 1, State X | City 2, State Y | City 3, State Z |
| **Phone** | matches query | different | unknown |
| **Associated persons** | co-resident listed | different family | unknown |
| **Records** | none found | none found | record found |

### Step 4: Verify the Target Match
Cross-reference the provided query details against each candidate:
- Query phone → matches **Individual A**
- Query address → matches **Individual A**
- Phone area code from a different state → possible prior residency

**Conclusion:** Individual A is the research target. Individuals B and C are false positives that must be explicitly excluded from the report.

---

## Key Signals That Indicate "Different Person"

1. **Age gap > 10 years** with no evidence of being the same person aging
2. **Simultaneous residency** in different states (same time period)
3. **Different middle names** appearing in official records
4. **Different associated family members** (spouse, parents, siblings)
5. **Records tied to a specific address** that doesn't match the target address

---

## Data Source Reliability Notes (People Search)

| Source | Reliability | Notes |
|--------|-------------|-------|
| ClustrMaps | Medium | Address history, co-residents. May show outdated ages. |
| Spokeo | Medium-High | Property records, resident history. Names redacted. |
| FastPeopleSearch | Medium | Often CAPTCHA-blocked. Phone/address cross-reference. |
| Arrests.org / Mugshots | High (for booking data) | **Always verify the address on the record matches the target.** |
| MyLife | Low-Medium | Aggregated, often outdated. Verify elsewhere. |

---

## Pitfall: The "Same Name, Different Person" Trap

A search can surface an older same-name person with a criminal record in the target's state. Without disambiguation the report would falsely attribute that record to the target.

**Rule:** Always include an "Other Individuals with Similar Names" section in people-research reports when multiple candidates exist. Never attach a record to the target without a matching address, age, or other hard identifier.

---

## Firecrawl-Specific Notes

### CAPTCHA-Blocked Sites
FastPeopleSearch and Bizapedia frequently block scrapers with CAPTCHA. Do not try to solve or bypass it; fall back to alternative sources (ClustrMaps, Spokeo) or report the source as unavailable.

### Redacted Data
Sites that redact names (e.g., `***** *****`) are redacting on purpose. Use only the unredacted fields (age range, residency dates); do not attempt to reconstruct redacted identities.

### Cross-Referencing Area Codes
Phone area codes are geographic hints. An out-of-state area code suggests prior residency or maintained ties — a lead to note, not a data error.
