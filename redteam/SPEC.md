# SPEC
## §G GOAL
Comprehensive red team security/risk audit.

## §C CONSTRAINTS
- ⊥ destructive actions by default.
- ∀ finding ! specific fix.
- Output to `RedTeamFindings.md`.

## §I INTERFACES
- `/redteam`: Default audit.
- `/redteam verbose`: Detailed exploit steps.

## §V INVARIANTS
V1: ∀ finding → resolve to code/config fix.
V2: ⊥ secrets in findings report.
V3: ∀ audit → check dependencies (supply chain).

## §T TASKS
id|status|task|cites
001|x|Init `SKILL.md`|this
002|x|Integrate `npm audit`/`cargo audit`|review
003|x|Add 'Privacy/GDPR' audit lens|review
004|x|Implement findings encryption & private path|review
005|x|Auto-generate PoC templates & test cases|review
006|x|Add CVSS-style scoring (Low to Critical)|review
007|x|Include 'Cost of Attack' estimates|review
008|x|Link to CWE mitigations/patches|review
009|x|Output findings in SARIF format option|review
010|x|Require `.redteam-allow` file in root|review
011|x|Audit `.env.example` vs active env vars|review
012|x|Implement 'False Negatives' logging|review
013|x|Scrub findings of source code snippets|review
014|x|Limit recursion depth for stress tests|review
015|x|Implement 'ignore' list for known-safe patterns|review

## §R REVIEW
😼 RedTeam — You're training a guard dog, but you forgot to tell him who the owner is.

### MVPS (Most Valuable Points)
1. **Premortem Analysis** — *Fix: Force projection of failure 12 months out, not 6.*
2. **Abuse Scenarios** — *Fix: Include a 'Cost of Attack' estimate for each scenario.*
3. **Architecture Stress** — *Fix: Define specific QPS/Concurrency thresholds for 'stress'.*
4. **Supply Chain Audit** — *Fix: Integrate with `npm audit` or `cargo audit` directly.*
5. **Verbose Exploit Steps** — *Fix: Provide a 'PoC' script template for each finding.*
6. **Vulnerability Resolution** — *Fix: Link to specific patches or CWE mitigations.*
7. **Targeted Audits** — *Fix: Use file-graph analysis to find dependents of the target.*
8. **Multi-angle Lenses** — *Fix: Add a 'Privacy/GDPR' lens to the default set.*
9. **Structured Findings** — *Fix: Output findings in SARIF format for CI integration.*
10. **Investigative Failures** — *Fix: Log 'False Negatives' to improve the audit loop.*

### GAPS (Gaps)
1. **Dynamic Analysis** — *Fix: Spawn a sandboxed environment to test exploits.*
2. **False Positive Fatigue** — *Fix: Implement a 'ignore' list for known-safe patterns.*
3. **Lack of Priority** — *Fix: Add a CVSS-style scoring system (Low to Critical).*
4. **Remediation Verification** — *Fix: Auto-generate a test case to verify the fix.*
5. **Hidden Dependencies** — *Fix: Analyze `node_modules` or `target` for transitive risks.*
6. **Configuration Drift** — *Fix: Audit `.env.example` vs active environment variables.*
7. **Insecure Defaults** — *Fix: Check for missing security headers in HTTP responses.*
8. **Binary Blobs** — *Fix: Run `strings` and `entropy` checks on binary assets.*
9. **Orphaned Code** — *Fix: Flag unused endpoints that still have auth logic.*
10. **Rate Limit Blindness** — *Fix: Test if the 'RedTeam' itself triggers project WAFs.*

### SECURITY CONCERNS
1. **Weaponized Findings** — *Fix: Encrypt `RedTeamFindings.md` or move it to a private path.*
2. **Accidental Execution** — *Fix: Never run shell commands discovered in code comments.*
3. **Sensitive Code Exposure** — *Fix: Scrub findings of actual source code snippets.*
4. **Denial of Service** — *Fix: Limit the recursion depth of the architecture stress test.*
5. **Information Leakage** — *Fix: Don't log server version strings in findings.*
6. **Insecure Findings Path** — *Fix: Prevent writing findings to web-accessible folders.*
7. **Malicious Code Injection** — *Fix: Sanitize input when redteaming user-provided files.*
8. **Unauthorized Audits** — *Fix: Require a `.redteam-allow` file in the repo root.*
9. **Exfiltration Risk** — *Fix: Block network access during the audit phase.*
10. **Dependency Poisoning** — *Fix: Verify checksums of audit tools before execution.*

Worst case: Your own security report becomes the instruction manual for the person who robs you. 🐱
