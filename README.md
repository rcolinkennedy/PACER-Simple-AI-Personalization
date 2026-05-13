# PACER

A file-based memory and context system that gives any AI assistant persistent memory and a consistent identity across tools and sessions.

```
PACER/
├── AGENTS.md          ← the one file every AI reads at startup
├── BOOTSTRAP.md       ← first-run conversation to set up identity
├── WRAP.md            ← session-end ritual for capturing memory
├── user/              ← who you are (human-maintained, gitignored)
│   ├── AI-PERSONA.md
│   ├── PROFILE.md
│   ├── voice.md
│   ├── preferences.md
│   ├── values.md
│   └── goals.md
├── memory/            ← what the AI remembers (AI-maintained, gitignored)
│   ├── MEMORY.md      ← curated long-term memory (≤100 lines)
│   ├── daily/         ← raw session logs, one per day
│   ├── projects/
│   ├── people/
│   └── topics/
├── context/           ← scratch work (session-scoped, gitignored)
├── skills/            ← reference skills, loaded on demand
└── Outputs/           ← finished work (gitignored)
```

## Why this

Every AI conversation starts from zero. PACER fixes that with plain markdown files — no database, no vendor lock-in, no code.

- **Platform-independent.** One instruction file (`AGENTS.md`) works with Claude, GPT, Gemini, or anything that reads files. Add a one-line redirector for your tool (`CLAUDE.md`, etc.).
- **Your data stays yours.** All personal files are gitignored. The repo is scaffolding — clone it, fill it in, and nothing personal ever touches GitHub.
- **Two-tier memory.** Raw daily logs for everything that happened, a curated long-term memory file (≤100 lines) for what actually matters. The AI maintains both.
- **Hybrid loading.** Identity and preferences load every session. Voice, values, goals, entity files, and skills load on demand — keeps token costs low.
- **Goes mobile.** PACER-Lite compresses the system into a cloud-based context layer (Notion, etc.) for use from any device. Same identity, same memory, different surface.

## Get started

```bash
git clone https://github.com/rcolinkennedy/PACER-Simple-AI-Personalization.git
cd PACER-Simple-AI-Personalization
```

Open the folder in your AI tool (CoWork, Cursor, Windsurf, or anything that reads local files). The AI reads `AGENTS.md`, finds `BOOTSTRAP.md`, and starts a conversation to learn who you are and set up your identity files.

After bootstrap, just use it. The AI loads your context at session start and captures memory at session end (triggered by saying "we're done" or "wrap up").

## Usage

**First run**

```
# AI reads BOOTSTRAP.md automatically and starts a conversation:
# "Hey. I just came online. Who am I? Who are you?"
# Together you fill in user/AI-PERSONA.md, user/PROFILE.md, etc.
# Bootstrap deletes itself when done.
```

**Every session after**

```
# Session start: AI loads identity + preferences + memory automatically.
# Work normally. The AI knows who you are.

# Session end:
> "we're done"            # → auto mode: AI saves daily log + updates memory
> "what did you learn?"   # → review mode: AI shows draft first, you approve
```

**Going mobile with PACER-Lite**

Compress your identity and active context into a cloud layer (e.g. three Notion pages), write a static instruction file for a Claude Project or Notion Agent, and connect via MCP. The portable system syncs back to the full system through structured handoff entries. See the [PACER-Lite writeup](https://www.notion.so/rcolinkennedy/PACER-Lite-Making-a-Personalized-AI-System-Portable-32dc1a400ce680429589fca6031c15d5) for details.

## Key files

| File | What it does |
|------|-------------|
| `AGENTS.md` | Master instruction file. The only file the AI needs to find everything else. |
| `BOOTSTRAP.md` | First-run setup. Guides the identity conversation, then self-deletes. |
| `WRAP.md` | Session-end ritual. Captures daily log, updates memory, flags suggestions. |
| `CLAUDE.md` | One-line redirector for Claude-based tools. Add similar files for other platforms. |
| `skills/` | Reference skills from [Agent Skills for Context Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering). Loaded on demand. |

## Related

- [Agent Skills for Context Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) — memory systems and filesystem context skills this builds on
- [OpenClaw](https://github.com/openclaw/openclaw) — session management patterns adapted here
- [Personalized AI: PACER](https://www.notion.so/rcolinkennedy/Personalized-AI-PACER-32cc1a400ce680408e3ae68150ffe6b9) — original writeup
- [PACER-Lite](https://www.notion.so/rcolinkennedy/PACER-Lite-Making-a-Personalized-AI-System-Portable-32dc1a400ce680429589fca6031c15d5) — making it portable
- [PACER-Lite → Notion Agent](https://www.notion.so/rcolinkennedy/PACER-Lite-extends-into-a-Notion-Agent-32ec1a400ce6801bb499e781f08b1582) — extending into ambient AI

## License

MIT
