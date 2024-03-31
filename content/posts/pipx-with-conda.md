---
title: "Implementando pipx con conda en macOS"
date: 2024-03-30
draft: false
categories: ["programming" ]
labels: ["spanish", "python", "pipx", "conda", "macos" ]
---

## Contexto

Soy un gran fan y usuario de `pipx`, pero por alguna razón, no funciona tan
bien en macOS como en Linux.

La cosa es que uso `conda` (instalacion manual) y `pipx` (brew) muchas veces
cuando tengo un entorno virual activado `pipx` se hace un lio y usa el entorno
virtual incorrecto haciendo que el comando falle.


Uno de los cambios que hice fue instalar `pipx` en un entorno conda en lugar de
con `brew` y crear un alias para el binario, así ya no hay inconvenientes de
entornos y variables. En general, funciona mejor; me permite controlar la
versión de Python que usa `pipx` fácilmente (La variable de entorno
`PIPX_DEFAULT_PYTHON` también me causa problemas en MacOS).
Usando `brew` instala la última versión de Python, la cual algunos CLIs no
soportan (como `duckdb`).

Sin embargo, la situación no se limita a esto. Recientemente, me enfrenté al
siguiente desafío:


```bash
$ pipx install visidata
  installed package visidata 3.0.2, installed using Python 3.11.5
  These apps are now globally available
    - vd
    - vd2to3.vdx
    - visidata
  These manual pages are now globally available
    - man1/vd.1
    - man1/visidata.1
done! ✨ 🌟 ✨
$ vd
zsh: /Users/mgreco/.local/bin/vd: bad interpreter: /Users/mgreco/Library/Application: no such file or directory
```

En este punto ya me he dado por vencido y no quiero seguir creando soluciones
provisionales para esto, siendo que debería funcionar de inmediato (supongo que
alguna implementación inusual de macOS, impide que funcione correctamente).

## Solución

Se me ocurrio replica lo que hago cuando quiero instalar un dependencia que
`pipx` en MacOS falla y que consiste en usar `conda` para gestionar los
entornos y `pip` para instalar dependencias. Es replicar la funcionalidad de
`pipx install`, pero usando conda. Esto tiene alguna ventaja extra como que te
permite controlar la versión de Python que deseas usar para cada entorno.

Lo primero que hice fue definir cómo quiero usarlo, que es fácil si ya conoces
`pipx`:

```bash
cx install black
cx install black -p 3.11
cx install git+https://github.com/psf/black
```


> Nota: `cx` es como he llamado al comando `conda` + `pipx`.

El proceso para crear un entorno sería algo como lo siguiente:

1. Crear un entorno utilizando la versión deseada de Python.
1. Instalar el paquete requerido en el entorno creado.
1. Realizar la creación de un enlace simbólico a la Interfaz de Línea de
   Comandos (CLI) en `~/.local/bin`.


## Iteracion 0

Lo que traducido en bash, resultaría en algo similar a esto:

```bash
dep=$1
conda create -p ~/.cx/venvs/$dep/ python=3.11 -y
~/.cx/venvs/$dep/bin/pip install $dep
ln -s ~/.cx/venvs/$dep/bin/$dep ~/.local/bin/$dep
```


Rápidamente verás varios problemas con esta implementación:

1. Usar `dep` como nombre del entorno es raro y poco conveniente. `dep` podría
   ser una URL.
2. Necesito parametrizar la versión de Python.
3. ¿Qué sucede si el binario no tiene el mismo nombre que el paquete?

Por tanto, he cambiado a un script en python que te da un control más detallado
de lo que deseas hacer.

## Iteracion 1


```python
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("dep", help="can be a URL or a package name")
parser.add_argument("-p", "--pyver", help="python version to use", default="3.11")

args = parser.parse_args()

dep = args.dep
pyver = args.pyver


# extract name from dep
name = dep.split('/')[-1].split('.')[0]

conda_cmd = f"conda create -p ~/.cx/venvs/{name} python={pyver} -y"
pip_cmd = f"~/.cx/venvs/{name}/bin/pip install -q {dep} "

subprocess.call(conda_cmd, shell=True)
subprocess.call(pip_cmd, shell=True)
```

Esta solucion ya hace lo que quiero, solo falta incluir el symlink y alguna
otras mejoras:


- incluir el comando explicito `cs install`
- añadir verbosidad
- gestionar los binarios nuevos


## Iteracion 2


```python
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("dep", help="can be a URL or a package name")
parser.add_argument("-p", "--pyver", help="python version to use", default="3.11")

args = parser.parse_args()

dep = args.dep
pyver = args.pyver


# extract name from dep
name = dep.split('/')[-1].split('.')[0]
print(name)

conda_cmd = f"conda create -p ~/.cx/venvs/{name} python={pyver} -y -q > /dev/null"
pip_cmd = f"~/.cx/venvs/{name}/bin/pip install -q {dep} "

from pathlib import Path

subprocess.call(conda_cmd, shell=True)
pre_binaries = set(Path(f"~/.cx/venvs/{name}/bin/").glob('*'))
subprocess.call(pip_cmd, shell=True)
post_binaries = set(Path(f"~/.cx/venvs/{name}/bin/").glob('*'))

new_binaries = post_binaries - pre_binaries
print(new_binaries)
```


En esta iteracion he incluido una forma de determinar qué binarios incluir en
`~/.local/bin` es bastante facil y funciona bien para lo que necesito pero
tiene margen para mejorar, por ejemplo, seguramente este incluyendo binarios de
las dependencias de los proyectos que estoy instalando.

El **problema** con esta solución es que la salida de `new_binaries` es un conjunto
vacío.

Sucede que MacOS devuelve `False` en
`Path(f"~/.cx/venvs/{name}/bin/").exists()`, pero si haces
`Path(f"~/.cx/venvs/{name}/bin/").expanduser().exists()`, devuelve `True`.

Por lo tanto, una vez resuelto el problema, ya tengo `black` y `blackd` en
`new_binaries`.

## Iteracion 3


```python
import subprocess
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument(
    "cmd",
    help="can be a URL or a package name",
    default="install",
    choices=["install", "inject", "run"],
)
parser.add_argument("dep", help="can be a URL or a package name")
parser.add_argument("-p", "--pyver", help="python version to use", default="3.11")
parser.add_argument("-f", "--force", help="Force", action="store_true")
parser.add_argument("-v", "--verbose", help="Verbose", action="store_true")
args = parser.parse_args()

dep = args.dep
pyver = args.pyver
force = args.force
cmd = args.cmd
verbose = args.verbose

# extract vname from dep
vname = dep.split("/")[-1].split(".")[0]

# define variables
VENV = Path(f"~/.cx/venvs/{vname}").expanduser()
BIN = Path(f"~/.cx/venvs/{vname}/bin").expanduser()
PIP = Path(f"{BIN}/pip").expanduser()

if verbose:
    print(f"{VENV = }")
    print(f"{BIN = }")
    print(f"{PIP = }")

if cmd != "install":
    raise NotImplementedError

# create venv
venv_cmd = f"conda create -p {VENV} python={pyver} -y -q > /dev/null"

if verbose:
    print(f"{venv_cmd = }")

subprocess.call(venv_cmd, shell=True)
pre_binaries = set(BIN.glob("*"))

# install dep
pip_cmd = f"{PIP} install -q {dep}"

if verbose:
    print(f"{pip_cmd = }")

subprocess.call(pip_cmd, shell=True)
post_binaries = set(BIN.glob("*"))

# find new binaries
new_binaries = post_binaries - pre_binaries

# create symlink in ~/.local/bin
f = "-f" if force else ""
for p in new_binaries:
    link_cmd = f"ln {f} -s {p} ~/.local/bin"

    if verbose:
        print(f"{link_cmd = }")

    subprocess.call(link_cmd, shell=True)
```


Esta es la solución final.


Tiene varias mejoras:

1. Incluye un parametro `force` para forzar el symlink
1. Crea un alias para el binario
1. Incluye un parametro `verbose` para mostrar el comando ejecutado

Lo he juntado todo en un proyecto de GitHub, podria ser usado con `pipx run`
pero en mi caso tengo el script en mi `~/.local/bin/cx`.

Repo: https://github.com/mmngreco/cx


## Demo


{{< youtube faE4_IDbcP0 >}}
