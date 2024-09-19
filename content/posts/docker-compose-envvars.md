---
title: "Docker Compose Env Var Adventures"
date: 2024-09-19
draft: false
categories: ["programming"]
labels: ["english", "docker", "envvars"]
---

Let's dive into the world of Docker Compose and environment variables, where
hilarity ensues and variables come alive (or do they?).

We've all been there. Playing hide and seek with environment variables in
Docker Compose. Let's see how our dear friend `MYVAR` enjoys this grand game of
Peekaboo!

### Round 1: The Invisible Variable
You think you're smart. You declare it confidently...

```bash
services:
  test:
    image: alpine
    command: echo MYVAR=$MYVAR
    environment:
      MYVAR: "asfd"
MYVAR=
```
Well, MYVAR decided to stay invisible. Maybe it's hiding under a digital rock?

### Round 2: Double Dollar Dilemma
"Ah, I'll catch you with $$MYVAR!," you exclaim.

```bash
services:
  test:
    image: alpine
    command: echo MYVAR=$$MYVAR
    environment:
      MYVAR: "asfd"
MYVAR=$MYVAR
```
Wait, now we've just given MYVAR an identity crisis. It's still playing hard to
get!

### Round 3: Command-Wrapper Shenanigans
“I got this! Let’s add a `sh -c` wrapper…”

```bash
services:
  test:
    image: alpine
    command: sh -c 'echo MYVAR=$MYVAR'
    environment:
      MYVAR: "asfd"
MYVAR=
```
Nope. Still hiding. MYVAR seems to be a master of disguise.

### Round 4: The Grande Reveal
“$MYVAR, you can run but you can't hide from $$ and a `sh -c` wrapper!”

```bash
services:
  test:
    image: alpine
    command: sh -c 'echo MYVAR=$$MYVAR'
    environment:
      MYVAR: "asfd"
MYVAR=asfd
```

Victory at last! 🎉 The sneaky MYVAR is finally revealed!
