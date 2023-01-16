#!/usr/bin/env python3
"""Hello World  mult languages

The program will show the message acording with the env language.

Usage:
It depends on the LANG variable correctly condfigurated:

    export LANG=pt_BR

Execução: 

    python hello.py
    ou
    ./hello.py

"""
__version__= "0.0.1"
__author__= "Fabio Araujo"
__license__= "Unlicensed"

import os

# Dunder

#  This program prints  Hello World

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
"en_US": "Hello, World!",
"pt_BR": "Olá!",
"it_IT": "Ciao, Mundo!",
"es_SP": "Hola, Mondo!",
"fr_FR": "Bonjour, Monde!",
}

# O(1)
print(msg[current_language])
