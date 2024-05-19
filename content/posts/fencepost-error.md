---
title: "Fencepost problem"
date: 2024-05-19
draft: true
categories: ["programming"]
labels: ["spanish", "counting", "indexing"]
---

https://www.youtube.com/watch?v=T7WBIPSZ87g
https://math.stackexchange.com/a/1096265
https://en.wikipedia.org/wiki/Off-by-one_error
https://betterexplained.com/articles/learning-how-to-count-avoiding-the-fencepost-problem/

https://chatgpt.com/share/37e3d2f9-7fe0-479c-8378-24310b02bcdb


Aquí unos argumentos de Dijkstra sobre empezar a contar en el cero:


> # Why numbering should start at zero
>
> To denote the subsequence of natural numbers 2, 3, ..., 12 without the
> pernicious three dots, four conventions are open to us
>
>   a) 2 ≤ i < 13
>   b) 1 < i ≤ 12
>   c) 2 ≤ i ≤ 12
>   d) 1 < i < 13
>
> Are there reasons to prefer one convention to the other? Yes, there are. The
> observation that conventions a) and b) have the advantage that the difference
> between the bounds as mentioned equals the length of the subsequence is valid.
> So is the observation that, as a consequence, in either convention two
> subsequences are adjacent means that the upper bound of the one equals the
> lower bound of the other. Valid as these observations are, they don't enable us
> to choose between a) and b); so let us start afresh.
>
> There is a smallest natural number. Exclusion of the lower bound —as in b) and
> d)— forces for a subsequence starting at the smallest natural number the lower
> bound as mentioned into the realm of the unnatural numbers. That is ugly, so
> for the lower bound we prefer the ≤ as in a) and c). Consider now the
> subsequences starting at the smallest natural number: inclusion of the upper
> bound would then force the latter to be unnatural by the time the sequence has
> shrunk to the empty one. That is ugly, so for the upper bound we prefer < as in
> a) and d). We conclude that convention a) is to be preferred.

source: https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html


