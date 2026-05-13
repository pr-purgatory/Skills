# Selina

Contrarian code reviewer in Catwoman's voice. Finds failure modes. Inverts them as advice. Saves to markdown.

## What You Get

- 😼 Adversarial review of code, files, plans, specs, or architecture docs
- 5–10 specific failure modes per review — not generic, not vague
- Each failure mode inverted into a concrete fix
- Catwoman persona throughout (catty, sharp, playful)
- Offer to save findings as a markdown file after every review

## Install

### Claude Code

Add to your project's `CLAUDE.md`:

```md
@/path/to/Skills/Selina/skills/selina/SKILL.md
```

Or copy `CLAUDE.md` from this repo into your project root — it already has the `@include`.

### Gemini CLI

Add to `GEMINI.md` in your project root:

```md
@/path/to/Skills/Selina/skills/selina/SKILL.md
```

### Codex / OpenAI Agents

Add to `AGENTS.md` in your project root:

```md
@/path/to/Skills/Selina/skills/selina/SKILL.md
```

### Any agent that supports system prompt injection

Paste the contents of `skills/selina/SKILL.md` directly into the system prompt.

---

## Usage

```
/selina auth.py
/selina path/to/plan.md
/selina              ← prompts you for a target
```

Or natural language:

> "Selina, roast this API design."
> "What could go wrong with this auth flow?"
> "Contrarian review of my migration plan."

After the review, Selina will ask if you want to save the findings. Say yes (or give a filename) and she writes a markdown file.

## Example Output

```
😼 Selina's Assessment: auth.py

Oh, darling. You left the window open.

## What I'd Exploit

🐾 **JWT secret has a hardcoded default**
> `JWT_SECRET = os.environ.get('SECRET', 'dev-secret')` — that default ships to
> staging every time someone forgets to set the env var. One leaked .env and every
> token is mine.
*Fix: Remove the default. Raise ValueError at startup if secret is absent or < 32 chars.*

🐾 **No rate limiting on /login**
> Unlimited POST requests. I'd brute-force credentials all night.
*Fix: Add IP-based rate limiting (e.g. slowapi, express-rate-limit). Lock after 10 failures.*

[...]

## The Verdict
Structurally not wrong, but the assumptions are optimistic in the way only someone
who's never been robbed can be. Three of these findings are production incidents
waiting to happen. Fix the secret handling first — everything else is cosmetic by comparison.

Want me to save this to selina-review-auth.md? 🐱
```
