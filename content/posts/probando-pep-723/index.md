---
title: "Probando pep-723 dependencias en un solo archivo"
date: 2024-03-10
draft: false
categories: ["programming"]
labels: ["python", "spanish", "pep"]
---

## PEP-723


En mi camino por abrazar el minimalismo, hoy he podido probar como funciona el
PEP-723 y mola bastante!


Prueba esto, crea un fichero python con el siguiente contenido:

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

a continuacion ejecuta:


```bash
pipx run /tmp/p.py
```


![demo](img/demo.png)


Mola eh!


