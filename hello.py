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
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language=="es_SP":
    msg = "Hola, Mundo!"
elif current_language =="fr_FR":
    msg = "Bonjour, Monde"

print(msg) 
