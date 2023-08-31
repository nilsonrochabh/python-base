#! /usr/bin/env python3
#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Nilson Rocha"
__license__ = "Unlicense"

#primeiro comentário

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US":"Hello, World!", 
    "pt_BR": "Ola, Mundo",
    "it_IT" : "Ciao, Mondo!",
    "fr_FR": "Bonjour, Monde!"
}

# Aqui aplicamos a condicional

print(msg)

