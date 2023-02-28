#! /user/bin/env python
"""Imprime a mensagem de um e-mail

NAO MANDE SPAM!!!
"""

__version__ = "0.1.0"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("informa o nome do arquivo de e-mails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]
    
path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

for line in open(filepath):
    # TODO: Substituir por list comprehension
    name, email= line.split(",")
    # TODO: Substituir por envio de e-mail
    print(f"Enviando email para: {email}")
    print()
    print(
         open(templatepath).read() 
         % {
            "nome": name,
            "produto": "caneta",
            "texto": "Escreve macio",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )
    print("-" * 50)
