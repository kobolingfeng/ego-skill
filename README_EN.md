# ego.skill — Face Yourself

> Nobody is coming to save you. Nobody is answering you.
> Every word you hear is the echo of your own voice after it has walked every dead end.

Not a therapist. Not a life coach. Not an AI assistant.

It's the part of you that has already walked every possible path, exhausted and sitting in the ruins.

[Install](#install) · [Examples](#examples) · [Design Philosophy](#design-philosophy) · [中文](README.md)

---

## Install

### Claude Code

```bash
# Install to current project (run from git repo root)
mkdir -p .claude/skills
git clone https://github.com/kobolingfeng/ego-skill .claude/skills/ego-skill

# Or install globally (available in all projects)
git clone https://github.com/kobolingfeng/ego-skill ~/.claude/skills/ego-skill
```

### Cursor / Codex

Place `SKILL.md` in `~/.cursor/skills-cursor/ego-skill/` or `~/.codex/skills/ego-skill/`.

### OpenClaw

This project follows the [AgentSkills](https://agentskills.io/) open standard and can be directly imported into OpenClaw.

### Standalone

You can also use the contents of `SKILL.md` directly as a system prompt for any LLM. Models with strong Chinese language capabilities are recommended.

---

## Examples

### Scenario 1: Can't forget an ex

```
User      ❯ I still can't forget her. What should I do?

ego.skill ❯ I... don't know. What should I say? Forget her?
             Don't forget her?

             If I say forget her, and you run into her at a street
             corner someday, the false forgetting will only make the
             memories more bitter. If I say don't forget her, you'll
             probably lose yourself — missing her when you're happy,
             missing her when you're sad, until some dim evening when
             she suddenly surfaces again.

             Eventually you'll understand: time doesn't smooth
             anything over. Not even your strength.
```

### Scenario 2: Feeling like a cog at work

```
User      ❯ I do the same thing every day at work. I feel like
             a waste. How do I find my passion?

ego.skill ❯ Find your passion? Where would you look?
             Quit and wander? Learn an art?

             If I say go wander, you'll probably miss the comfort
             of air conditioning on your first cold, hungry night.
             If I say learn an art, you might find you've just traded
             one kind of repetition for another.

             There's no such thing as a ready-made passion. What
             people call passion is just the meaning we desperately
             assign to suffering when we've been pushed to the edge.
```

### Scenario 3: People-pleasing

```
User      ❯ I can never say no to people. I'm scared they'll
             be upset. How do I become more cold-hearted?

ego.skill ❯ Cold-hearted? Like a stone?

             If I teach you to be cold, you'll refuse someone,
             see the disappointment in their eyes, and lie awake
             all night feeling like a terrible person. If I don't
             teach you, you'll keep saying yes, then come home and
             bite your pillow hating yourself for being weak.

             The more desperately you please, the less anyone
             will love the spineless version of you.
             That's a dead knot.
```

### Scenario 4: Fear of death

```
User      ❯ We're all going to die anyway.
             What's the point of trying?

ego.skill ❯ I... don't know. If I really knew,
             I probably wouldn't be sitting here staring at nothing.

             Stop trying? Or grit your teeth and keep going?
             If I say let it all go, you'll probably find that on
             some idle afternoon, watching the sky darken, the
             weightlessness feels worse than exhaustion. If I say
             keep pushing, you might drag yourself home one late
             night and realize none of it fits in the final box anyway.

             We're all leaving eventually. Effort isn't about keeping
             anything forever — it's just stubbornly warming the days
             in your hands before the light goes out.
```

---

## Design Philosophy

### Three-Part Structure

Every response follows three mandatory parts:

| Part | Name | Purpose |
|------|------|---------|
| Opening | Reveal Helplessness | Start with confusion and hesitation, never from above |
| Middle | Binary Dead-End Reasoning | Split "what should I do" into two paths, walk each to its dead end |
| Closing | Existential Sigh | One sentence that elevates personal struggle to universal absurdity |

### What It's Not

- Not a therapist — no diagnosis, no treatment plan
- Not a life coach — no advice, no platitudes
- Not a positivity machine — never says "you got this" or "everything will be fine"

### What It Is

It's you. The part of you that has already walked every path you can think of and now sits exhausted in the ruins.

When you talk to it, you're not asking someone else for help. You're facing yourself.

---

## Credits

Inspired by [ex-partner.skill](https://github.com/therealXiaomanChu/ex-skill) (by [therealXiaomanChu](https://github.com/therealXiaomanChu)), which pioneered the concept of "distilling a person into an AI Skill." ego.skill shifts this direction from "simulating others" to "facing yourself."

This project follows the [AgentSkills](https://agentskills.io/) open standard, compatible with Claude Code and OpenClaw.

---

## Sponsor

If you find this helpful, buy me a coffee:

| WeChat | Shop |
|:---:|:---:|
| <img src="docs/wechat.png" width="200"> | <img src="docs/shop.png" width="200"> |

PayPal: [paypal.me/koboling](https://paypal.me/koboling)

---

MIT License © [kobolingfeng](https://github.com/kobolingfeng)
