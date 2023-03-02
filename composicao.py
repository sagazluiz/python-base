#!/usr/bin/python3
""" Imprime nomes que começam com uma determinada letra"""

names = [
    "Bruno",
    "Joao",
    "Bernardo",
    "Barabara", 
    "Brian",
     ]

# estilo funcional
print("Estilo Funcional")
print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")

print("\n")
# estilo imperativo
print("Estilo Procedural")

def starts_with_b(text):
    """ Return bool if text starts with b"""
    return text[0].lower() == "b"

filtro = filter(starts_with_b, names)
filtro = list(filtro)
for name in filtro:
    print(name)
