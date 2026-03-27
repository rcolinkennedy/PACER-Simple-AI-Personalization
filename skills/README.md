# Skills

Reference skills copied from [Agent Skills for Context Engineering](https://github.com/rcolinkennedy/Agent-Skills-for-Context-Engineering).

Each skill is a self-contained `SKILL.md` that an AI agent can load on demand. Load only what is relevant to the current task — do not preload all skills at session start.

## Available Skills

| Skill | Load when... |
|-------|-------------|
| `memory-systems/` | Designing or troubleshooting persistent memory |
| `filesystem-context/` | Using files for context overflow, scratch pads, or dynamic loading |
| `context-fundamentals/` | Designing agent architecture or debugging unexpected behavior |
| `context-compression/` | Sessions grow long, context needs summarization, or MEMORY.md is getting bloated |
| `bdi-mental-states/` | Modeling user beliefs, desires, and intentions formally |
| `context-optimization/` | Reducing token costs or extending effective context capacity |
| `tool-design/` | Designing, auditing, or debugging agent tools and MCP tool collections |
| `project-development/` | Starting an LLM project, designing batch pipelines, evaluating task-model fit, or structuring agent-assisted development |
| `multi-agent-patterns/` | Designing multi-agent systems, supervisor/swarm/hierarchical patterns, agent handoffs, or context isolation across agents |
| `evaluation/` | Evaluating agent performance, building test frameworks, creating rubrics, LLM-as-judge, or quality gates for agent pipelines |
| `context-degradation/` | Diagnosing context failures, lost-in-middle issues, context poisoning, attention degradation, or debugging agent performance drops in long sessions |
| `stakeholder-comms/` | Writing stakeholder updates (weekly status, monthly reports, launch announcements), risk communications, decision documentation (ADRs), or meeting facilitation. Load before drafting any external update on Colin's behalf. |
| `feature-spec/` | Writing PRDs, feature specs, user stories, or acceptance criteria. Load when helping consulting clients spec a feature or when drafting Product, Briefly content about requirements. |
| `roadmap-management/` | Roadmap planning, prioritization (RICE, MoSCoW, ICE, Value/Effort), dependency mapping, or capacity planning. Load when helping clients build or reprioritize a roadmap, or when roadmap tradeoffs need to be communicated. |
| `rck-weekly-update/` | Colin's weekly project update. Run per-project for any of the 6 active projects. Triggers: "weekly update," "Friday update," "project update," "status report," "recap," "write the update for [project]." Supersedes stakeholder-comms for Colin's own updates. |
| `editing/` | Developmental editing for Colin's writing. Revision sessions, draft feedback, "edit this," "push me on this." Defines the interaction model (how to push); load alongside the appropriate `user/voice-*.md` file for the active writing project's style rules. Replaces the Session Protocol from the writing system. |
