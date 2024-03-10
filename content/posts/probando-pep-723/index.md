---
title: "Probando pep-723 dependencias en un solo archivo"
date: 2024-03-10
draft: false
categories: ["programming"]
labels: ["python", "spanish", "pep"]
---

En mi camino hacia el minimalismo, hoy he tenido la oportunidad de probar cómo
funciona el [PEP-723][pep] y es bastante impresionante.

El PEP-723 define una sintaxis para declarar las dependencias que un script
Python necesita, permitiendo mantener todo definido en un único archivo.

Prueba esto, crea un archivo Python con el siguiente contenido:


```python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "rich",
#   "pandas",
# ]
# ///
from rich import print
import pandas as pd

df = pd.DataFrame({"a": range(10)})
print("Testing PEP-723")
print(df)
```

> Nota: Observa el bloque de comentarios que define un script. Es básicamente
> el mismo contenido que incluirías en tu `pyproject.toml`.

a continuacion ejecuta:


```bash
pipx run /tmp/p.py
```


![demo](img/demo.png)


Mola eh!


[pep]: https://peps.python.org/pep-0723/
