#!/usr/bin/env python3
"""Calculadora infix.


Funcionamento:

[operacao] [n1] [n2]

operações:

sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2 
7

$ infixcalc.py mul 10 5
50

infixcalc.py 
operacao: sum
n1: 5
n2: 4
9

Os resultados serão salvos em infixcalc.log
"""

__version__ = "0.0.1"

import sys
import os
from datetime import datetime

arguments = sys.argv[1:]

if not arguments:
	operation = input("operacao:")
	n1 = input("n1:")
	n2 = input("n2:")
	arguments = [operation, n1, n2]
elif len(arguments) != 3:
	print("Número de argumentos inválidos")
	print("soma 5 5")
	sys.exit(1)	

try:
    operation, *nums = arguments
except Exception as e:
    print(str(e))
    print("Número de argumentos inválidos")
    print("ex: `sum 5 5`")
    sys.exit(1)
    
valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
	print("Operação inválida")
	print(valid_operations)
	sys.exit()

validated_nums = []
for num in nums:
	if not num.replace(".", "").isdigit():
		print(f"Número inválido {num}")
		sys.exit(1)
	if "." in num:
		num = float(num)
	else:
		num = int(num)
	validated_nums.append(num)

try:
    n1, n2 = validated_nums
except ValueError as e:
    print(str(e))
    sys.exit(1)

if operation =="sum":
	result = n1 + n2
elif operation == "sub":
	result = n1 - n2
elif operation == "mul":
	result = n1 * n2
elif operation == "div":
	result = n1 / n2

path = "/"
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

print(f"O resultado é {result}")


try: 
    with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {user} -  {operation}, {n1}, {n2} = {result}\n")
except PermissionError as e:
# TODO: logging
    print(str(e))
    sys.exit(1)


