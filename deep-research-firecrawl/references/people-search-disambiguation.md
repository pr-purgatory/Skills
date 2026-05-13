# People Search Disambiguation: Worked Example

## Session Context
Date: 2026-05-07  
Research Target: Alex Doe  
Query Details: Phone {phone A}, Address {street A}, {city} {state} {zip}  
Researcher: Hermes Agent (self-hosted Firecrawl + web search)

---

## Problem: Multiple Individuals with Same/Similar Name

Public records research frequently surfaces **multiple distinct individuals** with the same or similar names. Failing to disambiguate leads to conflated identities, false criminal associations, and inaccurate reporting.

---

## Disambiguation Methodology

### Step 1: Initial Broad Search
Run multiple query variations to capture all potential matches:
```
"Alex Doe" + phone number
"Alex Doe" + full address
"Alex Doe" + city + state
"Alex Dough" + state  (spelling variation)
```

### Step 2: Identify Distinct Records
Look for diverging attributes that indicate separate individuals:
- **Age differences** (e.g., 36 vs 45 vs 54)
- **Geographic separation** (e.g., Saint Paul MN vs Snyder TX vs Lawrence KS)
- **Middle names** (e.g., "Alex Q. Dough" vs "Alex Doe")
- **Associated persons** (family, co-residents)
- **Criminal records tied to specific addresses**

### Step 3: Document Each Individual Separately

| Attribute | Individual A | Individual B | Individual C |
|-----------|-------------|-------------|-------------|
| **Name** | Alex Doe | Alex Doe | Alex Q. Dough |
| **Age** | ~36 | ~45 | 54-55 (b. 1970) |
| **Location** | Saint Paul, MN | Snyder, TX | Lawrence, KS |
| **Address** | {street A} | {street B} | {street C} (past: Eden Prairie, MN) |
| **Phone** | {phone A} | {phone B} | Unknown |
| **Family** | {Co-resident} (co-resident) | {Relative 1}, {Relative 2} | Unknown |
| **Criminal** | None found | None found | Domestic assault (2025), Controlled substance (2021) |
| **Business** | "{Business Name}" at address | Unknown | Unknown |

### Step 4: Verify the Target Match
Cross-reference the provided query details against each candidate:
- Phone {phone A} → Matches **Individual A** (Saint Paul)
- Address {street A} → Matches **Individual A** (Saint Paul)
- Area code 512 = Texas → Suggests possible Texas origin or maintained ties

**Conclusion:** Individual A is the research target. Individuals B and C are false positives that must be explicitly excluded from the report.

---

## Key Signals That Indicate "Different Person"

1. **Age gap > 10 years** with no evidence of being the same person aging
2. **Simultaneous residency** in different states (same time period)
3. **Different middle names** appearing in official records
4. **Different associated family members** (spouse, parents, siblings)
5. **Criminal records tied to a specific address** that doesn't match the target address

---

## Data Source Reliability Notes (People Search)

| Source | Reliability | Notes |
|--------|-------------|-------|
| ClustrMaps | Medium | Good for address history, co-residents, property data. May show outdated ages. |
| Spokeo | Medium-High | Detailed property records, resident history. Requires parsing redacted content. |
| FastPeopleSearch | Medium | Often blocked by CAPTCHA. Good for phone/address cross-reference. |
| Arrests.org / Mugshots | High (for criminal) | Official booking records. **Always verify the address on the arrest record matches the target.** |
| MyLife | Low-Medium | Aggregated, often outdated. Good for birthdate hints but verify elsewhere. |

---

## Pitfall: The "Same Name, Different Person" Trap

In this session, the search initially surfaced:
- A **Alex Q. Dough** (age 54) with recent domestic assault arrest in Minnesota
- A **Alex Doe** (age 45) in Snyder, Texas
- The target **Alex Doe** (age ~36) in Saint Paul

Had these not been disambiguated, the report would have falsely attributed a criminal record to the target individual.

**Rule:** Always include an "IMPORTANT DISTINCTION" or "Other Individuals with Similar Names" section in people-research reports when multiple candidates exist.

---

## Firecrawl-Specific Techniques for People Search

### Handling CAPTCHA-Blocked Sites
FastPeopleSearch and Bizapedia frequently block scrapers with CAPTCHA. Workarounds:
1. Use `waitFor: 5000-10000` to allow JS challenges to complete (sometimes works)
2. Fall back to alternative sources (ClustrMaps, Spokeo often have similar data)
3. Use `delegate_task` with browser toolset for interactive sites

### Scraping Spokeo Property Pages
Spokeo property pages contain rich resident history but heavily redact names. The markdown output shows:
- Redacted names as `***** *****`
- Age hints (e.g., "Age 36")
- Residency date ranges (e.g., "Lived here for 4 Years (2022 - Present)")
- Associated relative surnames (e.g., "Relatives: {Surname} {Surname} {Surname} {Other}")

Parse these patterns to reconstruct identity matches.

### Cross-Referencing Area Codes
Phone area codes are geographic hints:
- 512 = Austin/Round Rock, Texas
- 651 = Saint Paul, Minnesota
- 325 = Snyder, Texas

A Texas area code on a Minnesota resident suggests prior Texas residency or maintained ties.
