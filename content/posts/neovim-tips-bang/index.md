---
title: "Vim: Comando Bang!"
date: 2024-03-10
draft: false
categories: ["programming"]
labels: ["vim", "neovim", "spanish"]
---

## El comando bang!

Esta joya de vim te permite acceder a todo el poder que tiene tus sitema,
todas CLIs o programas que puedes acceder/usar desde tu terminal puedes tambien
usarlas desde (neo)vim.

```vim
:help !
```


Abre neovim y ejecuta estos ejemplos con los que puedes ir viendo un poco como
funciona, pruebalos, modificalos:

> NOTA:
> Se asume que esta en norma mode, por lo que `:` es ir a la line de comando de
> (Neo)vim.


```vim
:.!echo "hola, mundo!"
:.!ls /tmp/*.md
:.!find . -name "README.md" -type f
:.!python -c "print('hola, python!')"
```

Aqui un ejemplo mas intersante:

```vim
:.!curl https://api.github.com/users/mmngreco
```

Aquí, tu buffer tendrá el siguiente contenido a partir de la línea actual:


```json
{
  "login": "mmngreco",
  "id": 6231413,
  "node_id": "MDQ6VXNlcjYyMzE0MTM=",
  "avatar_url": "https://avatars.githubusercontent.com/u/6231413?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/mmngreco",
  "html_url": "https://github.com/mmngreco",
  "followers_url": "https://api.github.com/users/mmngreco/followers",
  "following_url": "https://api.github.com/users/mmngreco/following{/other_user}",
  "gists_url": "https://api.github.com/users/mmngreco/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/mmngreco/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/mmngreco/subscriptions",
  "organizations_url": "https://api.github.com/users/mmngreco/orgs",
  "repos_url": "https://api.github.com/users/mmngreco/repos",
  "events_url": "https://api.github.com/users/mmngreco/events{/privacy}",
  "received_events_url": "https://api.github.com/users/mmngreco/received_events",
  "type": "User",
  "site_admin": false,
  "name": "Maximiliano Greco",
  "company": "@seedtag",
  "blog": "mmngreco.github.io",
  "location": "Madrid",
  "email": null,
  "hireable": true,
  "bio": "I'm just an economist who learned to program in Python.",
  "twitter_username": null,
  "public_repos": 203,
  "public_gists": 167,
  "followers": 83,
  "following": 75,
  "created_at": "2013-12-20T15:14:19Z",
  "updated_at": "2024-02-20T09:11:32Z"
}
```


Piensa "out of the box", tu imaginacion es el limite:

```vim
:.!curl https://api.github.com/users/mmngreco | jq '.type, .url'
```


