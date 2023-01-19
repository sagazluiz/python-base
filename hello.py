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
__version__= "0.0.3"
__author__= "Fabio Araujo"
__license__= "Unlicensed"

import os
import sys


arguments = {"lang": None,"count":1}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value= value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value

# Dunder

#  This program prints  Hello World
current_language = arguments["lang"]
if current_language is None:
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")
        
current_language = current_language[:5]

msg = {
"en_US": "Hello, World!",
"pt_BR": "Olá!",
"it_IT": "Ciao, Mundo!",
"es_SP": "Hola, Mondo!",
"fr_FR": "Bonjour, Monde!",
}

# O(1)

print(msg[current_language] * int(arguments["count"]))
