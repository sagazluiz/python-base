#! /user/bin/env python
"""Imprime a mensagem de um e-mail

NAO MANDE SPAM!!!
"""

__version__ = "0.1.0"

import sys
import os
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]
if not arguments:
    print("informa o nome do arquivo de e-mails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]
    
path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)


with smtplib.SMTP(host="localhost", port=8025) as server:
    for line in open(filepath):
        # TODO: Substituir por list comprehension
        name, email= line.split(",")
        text = (
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

        from_ = "bruno@rocha.com"
        to_ = ",".join([email])
        message = MIMEText(text)
        message["Subject"]="Compre mais"
        message["From"] = from_
        message["To"] = to_

        server.sendmail(from_, to_, message.as_string())
