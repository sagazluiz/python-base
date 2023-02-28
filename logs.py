#!/usr/bin/env python3
import os
import logging
from logging import handlers

# BOILERPLATE
# TODO: usar funcao
# TODO: usar lib (loguru)

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("luiz", log_level) # main -- programa principal
#ch = logging.StreamHandler()   # Console / terminal # heandlers -- indicacao do caminho para salvar 
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log",
     maxBytes=100, # 10**6 
     backupCount=10,
     )
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s' 
    'l:%(lineno)d f:%(filename)s: %(message)s'
    )
#ch.setFormatter(fmt)
fh.setFormatter(fmt)

# destino
#log.addHandler(ch)
log.addHandler(fh)

"""
log.debug("Mensagem para o Dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral")
 # root logger 
"""

print("---")


try:
    1/0
except ZeroDivisionError as e:
    log.error("[ERRO] Deu erro %s", str(e)) # Não usar fstring pq ele tem avaliação imediata.
    #stdout
    #stderr
    
