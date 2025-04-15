# checknet

Uma biblioteca simples para verificar conectividade com a internet via socket TCP.

## Instalação

```bash
pip install checknet
```

## Uso

```python
from checknet import is_connected

if is_connected():
    print("Online")
else:
    print("Offline")
```
