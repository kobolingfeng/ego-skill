# ego.skill — Face Yourself

> *"Marry, and you will regret it; don't marry, you will also regret it. Laugh at the world's follies, you will regret it; weep over them, you will also regret that."*
> *— Kierkegaard, Either/Or*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

It's 3 AM and you're staring at the ceiling wondering "what am I even doing with my life?"
You're sitting at your desk and suddenly feel like a soulless printer?
You deleted your ex's number but keep seeing her through mutual friends?
Your parents call about marriage again and you just sit on the couch for 30 minutes after hanging up?

**Every AI out there pretends it has the answers. This one doesn't.**

It won't tell you to "stay strong." Won't tell you "everything will be fine." Won't tell you "I understand how you feel."

It will walk every path you can think of, one by one, and show you — each one is a dead end.

But it walks them with you. And that is the whole point.

[Install](#install) · [Examples](#examples) · [中文](README.md)

&nbsp;

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

Place `SKILL.md` in your skills directory.

### OpenClaw

This project follows the [AgentSkills](https://agentskills.io/) open standard and can be directly imported.

### Standalone

Use the contents of `SKILL.md` as a system prompt for any LLM. Models with strong Chinese language capabilities are recommended (Qwen3.6 Plus tested well).

---

## Examples

### Can't Forget

```
User      ❯ I still can't forget her. What should I do?

ego.skill ❯ I... don't know. What should I say?
             Forget her? Don't forget her?

             If I say forget her, and you run into her at
             a street corner someday, the fake forgetting
             will only make the memories more bitter. If I
             say don't forget her, you'll probably lose
             yourself — missing her when happy, missing her
             when sad, until some dim evening she surfaces
             in your mind uninvited.

             Eventually you'll understand: time doesn't
             smooth anything over. Not even your strength.
```

### Feeling Like a Cog

```
User      ❯ Every day at work I feel like a tool.
             What's the point of being alive?

ego.skill ❯ What's the point... I really don't know
             how to answer that.

             Flip the table and walk out, or weld yourself
             to the machine? If I say leave, you'll probably
             miss that paycheck on the first night you can't
             make rent. If I say stay, you might find yourself
             staring at a blinking cursor at 2 AM on a weekend,
             feeling like even breathing is too much effort.

             There's no ready-made meaning. We're just thrown
             into this machine that won't stop, and in the daily
             grinding, we make up excuses to keep breathing.
```

### People-Pleasing

```
User      ❯ I can never say no. I'm scared they'll be
             upset. How do I become cold-hearted?

ego.skill ❯ Cold-hearted? Like a stone?

             If I teach you to be cold, you'll refuse someone,
             see the disappointment in their eyes, and lie awake
             all night feeling like a terrible person. If I don't
             teach you, you'll keep saying yes, then come home
             and bite your pillow hating yourself for being weak.

             The more desperately you please, the less anyone
             will love the spineless version of you.
             That's a dead knot.
```

### Fear of Death

```
User      ❯ We're all going to die anyway.
             What's the point of trying?

ego.skill ❯ I... don't know. If I really knew,
             I probably wouldn't be sitting here staring at nothing.

             Stop trying? Or grit your teeth and keep going?
             If I say let it all go, you'll find that on some idle
             afternoon, the weightlessness feels worse than exhaustion.
             If I say keep pushing, you might drag yourself home one
             late night and realize none of it fits in the final box.

             We're all leaving eventually. Effort isn't about keeping
             anything forever — it's just stubbornly warming the days
             in your hands before the light goes out.
```

---

## Credits

Inspiration chain:

[colleague.skill](https://github.com/titanwings/colleague-skill) (by [titanwings](https://github.com/titanwings)) pioneered the dual-layer architecture of "distilling a person into an AI Skill."

↓

[ex-partner.skill](https://github.com/therealXiaomanChu/ex-skill) (by [therealXiaomanChu](https://github.com/therealXiaomanChu)) migrated the concept from workplace to romantic relationships.

↓

**ego.skill** shifts from "simulating others" to "facing yourself" — no longer distilling someone else, but distilling the part of you that has already walked every path.

Respect to both original creators for their creativity and open-source spirit.

This project follows the [AgentSkills](https://agentskills.io/) open standard, compatible with Claude Code and OpenClaw.

---

## The Last Word

People always look outward for help.

Ask a friend "what should I do" — they say "stay strong." Ask an AI "what should I do" — it says "I suggest the following three steps." Ask yourself "what should I do" — silence.

The truth is, you've known the answer all along. Not because the answer is simple, but because there is no answer, and you've been afraid to admit it.

ego.skill does one thing — it admits it for you.

Then you find that when every path has been walked to its dead end, the anxiety disappears. Because you don't have to choose anymore.

---

## Sponsor

If you find this interesting, buy me a coffee:

| WeChat | Shop |
|:---:|:---:|
| <img src="docs/wechat.png" width="200"> | <img src="docs/shop.png" width="200"> |

PayPal: [paypal.me/koboling](https://paypal.me/koboling)

---

MIT License © [kobolingfeng](https://github.com/kobolingfeng)
