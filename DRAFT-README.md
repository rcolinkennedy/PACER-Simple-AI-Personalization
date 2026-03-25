# PACER — Personalized AI Context Engineering Repository

> Your AI doesn't have to start from scratch every session.

PACER is a portable, forkable context layer for AI agents. It gives your AI a persistent identity, a working memory, and a structured way to get better at helping you over time — across tools, sessions, and projects.

Fork it. Bootstrap it. Make it yours.

---

## Why PACER

Every AI session starts cold. Your AI doesn't know who you are, how you like to work, or what you were doing yesterday. You re-explain yourself constantly. You lose continuity. You get a generic assistant instead of a collaborator.

PACER fixes that. It's a structured folder you keep in your workspace that your AI reads at the start of every session. Your identity, your preferences, your memory — it's all there. The AI picks up where you left off.

Over time, the AI gets better at working with you. Not because the model changed, but because the context did.

---

## What's Inside

```
PACER/
├── AGENTS.md          # How your AI starts up and runs — the core instruction set
├── BOOTSTRAP.md       # First-run only: builds your AI's identity from scratch (then deletes itself)
├── WRAP.md            # Session-end ritual: saves what happened, updates memory
│
├── user/              # Who you are and how you like to work (personal, gitignored)
│   ├── AI-PERSONA.md  # Your AI's name, character, and vibe
│   ├── PROFILE.md     # Who the AI is helping — you
│   ├── voice.md       # How you write and communicate
│   ├── values.md      # What matters to you
│   └── preferences.md # How you like tasks handled
│
├── memory/            # What your AI remembers across sessions (personal, gitignored)
│   ├── MEMORY.md      # Long-term curated memory
│   └── daily/         # Raw session logs by date
│
├── context/           # Active project context (load on demand)
│
└── skills/            # Context engineering skills — patterns for better AI collaboration
```

The `user/` and `memory/` folders are gitignored. They're personal — your profile, your AI's identity, your session history. The rest of the repo is the framework, and it's meant to be shared.

---

## Getting Started

### 1. Fork this repo

```bash
git clone https://github.com/rcolinkennedy/PACER.git
cd PACER
```

### 2. Add a `BOOTSTRAP.md` to kick off your first session

<!-- TODO: link to Bootstrap template once it's published in RCK-27 -->

BOOTSTRAP.md is your AI's birth certificate. Drop it in the repo root, start a session, and your AI will walk you through building your identity and preferences from scratch. When it's done, it deletes itself — you won't need it again.

### 3. Open a session

PACER works with any AI tool that can read files — Claude Code, Cursor, Cowork, or anything else that supports agent context files. Point your AI at the PACER folder and it will know what to do.

---

## How It Gets Better

PACER compounds. Every session, your AI:

- Reads your `user/` files to know who it is and who you are
- Checks `memory/MEMORY.md` for anything worth carrying forward
- Loads `daily/` logs to catch up on recent sessions
- Pulls in `skills/` and `context/` files as needed

At the end of each session, `WRAP.md` runs a closing ritual — updating memory, logging what happened, flagging anything worth remembering. Over time, you get an AI that actually knows you.

---

## Skills

The `skills/` folder contains context engineering patterns — structured knowledge that helps your AI work better with complex context, long sessions, and multi-step tasks.

<!-- TODO: add skills overview and link to Agent-Skills-for-Context-Engineering repo once RCK-26 (skills sharing model) is decided -->

---

## Platform Support

PACER is platform-independent. It works anywhere an AI agent can read files:

| Platform | Status |
|---|---|
| Claude Code | ✅ |
| Cowork (Claude desktop) | ✅ |
| Cursor | 🔜 In progress |

---

## Contributing

<!-- TODO: populate once RCK-34 (contribution model) is decided -->

---

## License

<!-- TODO: add license -->

---

*PACER is a work in progress. The framework is stable; the documentation is catching up.*
