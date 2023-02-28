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
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("luiz", log_level) # main -- programa principal
ch = logging.StreamHandler()    # heandlers -- indicacao do caminho para salvar 
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s' 
    'l:%(lineno)d f:%(filename)s: %(message)s'
    )
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {"lang": None,"count":1}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
        "You need to use `=``, you passed %s, try --key=value: %s,", arg, str(e) 
        )
        sys.exit(1)
        
    key = key.lstrip("-").strip()
    value= value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
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
print(f"{current_language=}")
msg = {
"en_US": "Hello, World!",
"pt_BR": "Olá!",
"it_IT": "Ciao, Mundo!",
"es_SP": "Hola, Mondo!",
"fr_FR": "Bonjour, Monde!",
}

# O(1)
"""
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)        
"""

message = msg.get(current_language, msg["en_US"])

print(
    message * int(arguments["count"])
)
