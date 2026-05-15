# PACER

**Personalized Agent Context Engineering Repository** — a file-based memory and context system that gives any AI assistant persistent memory and a consistent identity across tools and sessions.

PACER is for people who use AI regularly and want personalization without standing up a custom agentic system. Plain markdown files, no code, no database, no package — the maintenance stays on the AI tool providers; you just keep the files.

It's not a deep agentic framework like [OpenClaw](https://github.com/openclaw/openclaw) or [Hermes](https://github.com/hermes-agi/hermes). Those give you autonomous tool-using agents. PACER gives you personalization and memory, with no maintenance headaches or runaway costs.

```
PACER/
├── AGENTS.md          ← the one file every AI reads at startup
├── BOOTSTRAP.md       ← first-run setup that self-deletes (interviews user, generates system files)
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
│   ├── glossary.md    ← shorthand, acronyms, codenames
│   ├── daily/         ← raw session logs, one per day
│   ├── projects/
│   ├── people/
│   └── topics/
├── TASKS.md           ← cross-session task tracking (AI-maintained, gitignored)
├── context/           ← scratch work (session-scoped, gitignored)
├── skills/            ← reference skills, loaded on demand
└── Outputs/           ← finished work (gitignored)
```

## What it looks like

PACER is for everyday work, wherever that happens. Claude on your phone, ChatGPT on your desktop, Cursor in your editor — the AI knows who you are, how you work, and what happened yesterday across all of them.

**Session 1** — Clone the repo, open it in your AI tool, and bootstrap runs. The AI interviews you — who you are, what you do, how you like to work — then generates your identity files and sets up the memory system. Ten minutes, once.

**Session 10** — You open a new conversation. The AI already knows your name, your role, your communication style, your active projects, and last week's decisions. No preamble. It picks up where you left off.

## Why this

- **Platform-independent.** One instruction file (`AGENTS.md`) works with Claude, GPT, Gemini, or anything that reads files. Add a one-line redirector for your tool (`CLAUDE.md`, etc.).
- **Your data stays yours.** All personal files are gitignored. The repo is scaffolding — clone it, fill it in, nothing personal touches GitHub.
- **Two-tier memory.** Raw daily logs plus a curated long-term memory file (≤100 lines). The AI maintains both.
- **Hybrid loading.** Identity and preferences load every session. Voice, values, goals, and skills load on demand — keeps token costs low.
- **Goes mobile.** PACER-Lite compresses the system into a cloud layer (Notion, etc.) for use from any device. Same identity, same memory, different surface.

## Get started

```bash
git clone https://github.com/rcolinkennedy/PACER-Simple-AI-Personalization.git
cd PACER-Simple-AI-Personalization
```

Open the folder in your AI tool (CoWork, Cursor, Windsurf, or anything that reads local files). Before first run, review `BOOTSTRAP.md` — you can customize the AI's name, your profile defaults, or the conversation's focus before it kicks off. Then let the AI read `AGENTS.md` and run bootstrap. This is mandatory — it interviews you, generates the `user/` and `memory/` files the system needs, then deletes itself.

After that, just use it. The AI loads your context at session start and captures memory at session end.

## Usage

**First run (bootstrap)**

```
# AI reads BOOTSTRAP.md and runs first-time setup:
# "Hey. I just came online. Who am I? Who are you?"
# Interviews you, generates user/ and memory/ files.
# Bootstrap deletes itself when done. The system is ready.
```

**Every session after**

```
# Session start: AI loads identity + preferences + memory automatically.
# Work normally. The AI knows who you are.

# Session end:
> "we're done"            # → auto: saves daily log + updates memory
> "what did you learn?"   # → review: shows draft first, you approve
```

**How wrap works**

When a session ends, `WRAP.md` tells the AI what to capture: a distilled daily log entry, task list updates (completions, new items, status changes), long-term memory updates if something significant happened, and entity file updates for projects, people, or topics that moved forward. It also flags any suggested changes to `user/` files — but never writes them without your approval.

The only thing the user needs to do is signal the end of the session. Say "we're done" for auto mode (the AI just saves everything) or "what did you learn?" for review mode (the AI shows you a draft and waits for your OK before writing). Everything else is handled by the AI.

**Going mobile with PACER-Lite**

Compress your identity and active context into a cloud layer (e.g. three Notion pages), write a static instruction file for a Claude Project or Notion Agent, and connect via MCP. See the [PACER-Lite writeup](https://www.notion.so/rcolinkennedy/PACER-Lite-Making-a-Personalized-AI-System-Portable-32dc1a400ce680429589fca6031c15d5) for details.

## Key files

| File | What it does |
|------|-------------|
| `AGENTS.md` | Master instruction file. The only file the AI needs to find everything else. |
| `BOOTSTRAP.md` | First-run setup. Interviews user, generates system files, self-deletes. Required. |
| `WRAP.md` | Session-end ritual. Captures daily log, updates tasks and memory, flags suggestions. |
| `TASKS.md` | Cross-session task tracking. AI-maintained — updated during wrap. |
| `CLAUDE.md` | One-line redirector for Claude-based tools. Add similar for other platforms. |
| `skills/` | Reference skills from [Agent Skills for Context Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering). Loaded on demand. |

## Related

- [Agent Skills for Context Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) — memory systems and context skills this builds on
- [OpenClaw](https://github.com/openclaw/openclaw) — session management patterns adapted here
- [Personalized Agent: PACER](https://www.notion.so/rcolinkennedy/Personalized-AI-PACER-32cc1a400ce680408e3ae68150ffe6b9) — original writeup
- [PACER-Lite](https://www.notion.so/rcolinkennedy/PACER-Lite-Making-a-Personalized-AI-System-Portable-32dc1a400ce680429589fca6031c15d5) — making it portable
- [PACER-Lite → Notion Agent](https://www.notion.so/rcolinkennedy/PACER-Lite-extends-into-a-Notion-Agent-32ec1a400ce6801bb499e781f08b1582) — extending into ambient AI

## License

MIT
