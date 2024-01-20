---
title: "I don't like macos for programming"
date: 2024-01-20
draft: True
categories: ["programming"]
labels: ["OS", "macos", "thoughts"]
---


`conda` and `autoenv` don't seem to function properly on macOS, though I'm
unclear about the exact cause. My experience has been that whenever I create an
autoenv file with `conda activate /home/max/project/venv/`, it fails every time
I open a terminal on that directory. However, once the prompt appears,
everything appears to function as expected, despite the error message showing
up before the prompt line.

`pipx` doesn't work at all. There's a particularly frustrating issue where
apparently 'brew' installs an additional Python binary for `pipx`, which cannot
be changed. As a result, I have to manually create environments and link the
executable.

For some reason, `sed` behaves differently on macOS compared to Linux. I'm not
sure why this is the case. This **only** makes me write complex scripts to check if
the user is on **macOS** or **Linux**.

As for `docker`, I won't get into the details of how poorly it works on macOS
compared to Linux.
