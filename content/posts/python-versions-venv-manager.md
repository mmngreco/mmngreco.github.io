---
title: "Python versions and venv manager"
date: 2024-07-18T11:47:22+02:00
draft: false
categories: ["devlopment"]
labels: ["english", "python", "venv"]
---


Today, let's chat about something that has both delighted and frustrated me in equal measure: managing Python environments. You know how it is—sometimes you feel on top of the world, and other times, you want to launch your computer out the window. 🌍🚀💥

### The PIP_REQUIRE_VIRTUALENV Trick!

So, here's the deal: setting `PIP_REQUIRE_VIRTUALENV` prevents you from accidently polluting your global Python environment when installing packages. It's like having an overprotective parent guard your environment from bad influences. Nice, right?

But, here's the hiccup: It’s not compatible with `conda`. And guess what I was using? Yep, `conda`. Ugh! So I jumped on the `venv` bandwagon, setting up Python 3.10, 3.11, 3.12 environments. And guess what? It works like a charm. 🎉

Check out more about it here: [PIP Issue 7902](https://github.com/pypa/pip/issues/7902).

### Hello, Rye!

Then, I stumbled upon `rye`. It sounded perfect, a shiny new toy to replace `conda` as my virtualenv and Python version manager. I was like, “where have you been all my life?”

However… and there’s always a “however”… 😅 I hit a few bumps, like frustrating `ModuleNotFoundError: No module named 'setuptools'`. I mean, come on!

I’m still giving it a shot and testing it out. It’s got potential, but you know, new tools always come with a learning curve and their own set of quirks.

For those curious, here's the rye bug tracker keeping my sanity in check: [Rye Issues](https://github.com/astral-sh/rye/issues?q=ModuleNotFoundError%3A+No+module+named+%27setuptools%27).

### Wrapping Up!

So, that’s my tale of woe and wow with Python environments. Do you have similar stories? Love or hate for a tool? Drop your thoughts in the comments. Let’s laugh and groan together over our tech adventures.

Peace out and happy coding! ✌️👨‍💻👩‍💻
