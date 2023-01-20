#!/user/bin/env/python
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia

$ notes.py read --tag=tech


"""
__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

cmds = ["read", "new"]

arguments = sys.argv[1:]
if not arguments:
	print("Invalid usage")
	print(f"You must specify a subcommand{cmds}")
	sys.exit(1)

if arguments[0] not in cmds:
	print(f"Invalid command (arguments[0])")

if arguments[0]== "read":
	# leitura de notas
	for line in open(filepath):
		title, tag, texto = line.split("\t")
		if tag.lower() == arguments[1].lower():
			print(f"title: {title}")
			print(f"text: {text}")
			print("-"*30)
			print()
		

if arguments[0]=="new":
	titulo = arguments[1]
	#TODO: Tratar como exception
	text = [
		f"title",
		input("tag:").strip(),  # elimina caracteres em branco
		input("text:\n").strip(),
		]
	# \t - tsv
	with open(filepath, "a") as file_:
		file_.write("\t".join(text) + "\n")
