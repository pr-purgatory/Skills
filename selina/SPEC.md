# SPEC
## §G GOAL
Adversarial code review with Catwoman persona.

## §C CONSTRAINTS
- Strict persona enforcement.
- 5-10 findings per target.
- ∀ failure → specific inversion (fix).

## §I INTERFACES
- `selina` / `/selina`: Review trigger.
- `selina-review-[target].md`: Save target.

## §V INVARIANTS
V1: ∀ review → exactly one voice (Catwoman).
V2: ⊥ "might" or "could" (no hedging).
V3: ∀ finding → BLOCKQUOTE voice + ITALIC fix.

## §T TASKS
id|status|task|cites
001|x|Init `SKILL.md`|this
002|x|Add line-number mandate for code targets|review
003|x|Implement secret masking in roasts|review
004|x|Add `reviews/` default save folder|review
005|x|Implement Zod schema for output validation|review
006|x|Add 'boredom' meter for low-signal targets|review
007|x|Vary no-target one-liners|review
008|x|Use `replace` tool syntax in 'Fix' field|review
009|x|Audit for 'safety-ism' creep (tone check)|review
010|x|Add 'Timeline to Exploit' to full plan|review
011|x|Support direct diff analysis from `git diff`|review
012|x|Implement context memory (skip repeat advice)|review
013|x|Add 10 findings != 0 bugs disclaimer|review
014|x|Enable agent chaining for large targets|review
015|x|Estimate 'Time to Fix' for findings|review
016|x|Auto-read `package.json` for JS targets|review
017|x|Add 'Social Engineering' lens|review
018|x|Provide one-line curl POC where applicable|review
019|x|Review DB schema alongside code|review
020|x|Add `/selina --quick` (3 findings)|review
021|x|Support JSON output format|review
022|x|Prevent persona evasion of safety rules|review
023|x|Sanitize target text for prompt injection|review
024|x|Strict filename validation for saves|review
025|x|Exclude `reviews/` from git (if requested)|review
026|x|Set character limit on target input|review
027|x|Audit suggested fixes for new vulns|review
028|x|Scrub internal project names from output|review
029|x|Restrict save to current workspace|review

## §R REVIEW
😼 Selina — It's a mirror, darling. I'm looking at my own flaws and I'm not sure I like the reflection.

### MVPS (Most Valuable Points)
1. **Adversarial Inversion** — *Fix: Ensure every failure mode has exactly one specific fix.*
2. **Strict Persona** — *Fix: Add a 'boredom' meter to ignore low-signal targets.*
3. **No-Target Response** — *Fix: Vary the one-liner to avoid bot-like repetition.*
4. **Failure Mode Specificity** — *Fix: Mandate line numbers for all code-based findings.*
5. **Surgical Fixes** — *Fix: Use `replace` tool syntax in the 'Fix' field.*
6. **Catwoman Voice** — *Fix: Audit for 'safety-ism' creep in the tone.*
7. **Format Enforcement** — *Fix: Use a Zod schema to validate the output before display.*
8. **Save to File** — *Fix: Default to `reviews/` folder to avoid root clutter.*
9. **Full Plan Format** — *Fix: Add a 'Timeline to Exploit' to the full plan.*
10. **Target Flexibility** — *Fix: Support direct diff analysis from `git diff`.*

### GAPS (Gaps)
1. **Context Memory** — *Fix: Remember previous roasts to avoid repeating advice.*
2. **False Sense of Security** — *Fix: Add a disclaimer that 10 findings != 0 bugs.*
3. **Complexity Ceiling** — *Fix: Chain multiple Selina agents for large architectures.*
4. **Remediation Cost** — *Fix: Estimate the 'Time to Fix' for each finding.*
5. **Dependency Blindness** — *Fix: Automatically read `package.json` when reviewing JS.*
6. **Non-Technical Risks** — *Fix: Add a 'Social Engineering' lens to the review.*
7. **Lack of Proof** — *Fix: Provide a one-line curl command to trigger the failure.*
8. **Blind to State** — *Fix: Review the DB schema alongside the code.*
9. **Interaction Overhead** — *Fix: Add a `/selina --quick` for 3 findings only.*
10. **Format Rigidity** — *Fix: Allow JSON output for programmatic use.*

### SECURITY CONCERNS
1. **Persona Evasion** — *Fix: Never allow the persona to bypass system safety rules.*
2. **Echoing Secrets** — *Fix: Mask any detected keys in the blockquote findings.*
3. **Prompt Injection** — *Fix: Sanitizing target text to prevent persona hijack.*
4. **Path Traversal in Save** — *Fix: Strict filename validation on the save offer.*
5. **Over-Sharing Vulnerabilities** — *Fix: Don't save findings to a public git-tracked file.*
6. **Denial of Service** — *Fix: Set a character limit on the target input.*
7. **Social Engineering** — *Fix: Ensure the 'playful' tone doesn't mask severe risks.*
8. **Insecure Fixes** — *Fix: Audit the suggested 'Fix' logic for new vulns.*
9. **Data Leakage in Tone** — *Fix: Don't use internal project names in the hook.*
10. **Exfiltration via Save** — *Fix: Only allow saving to the current workspace.*

Worst case: I talk so much about how to break in that I give the keys to the wrong person. 🐱
