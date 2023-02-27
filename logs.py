#!/usr/bin/env python3
import os
import logging

# BOILERPLATE
# TODO: usar funcao
# TODO: usar lib (loguru)

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# nossa instancia
log = logging.Logger("luiz", log_level) # main -- programa principal

# level
ch = logging.StreamHandler()    # heandlers -- indicacao do caminho para salvar 
ch.setLevel(log_level)

# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s' 
    'l:%(lineno)d f:%(filename)s: %(message)s'
    )
ch.setFormatter(fmt)

# destino
log.addHandler(ch)

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
    
