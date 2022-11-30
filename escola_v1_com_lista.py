#!/usr/bin/env/ python3
"""Exibe relatório de crianças por atividade.

IMprimr a lista de crianças agrupadas por sala que frequentam cada uma 
das atividades.
"""
__version__ ="0.1.0"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maria", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
("Ingles", aula_ingles),
("Muisica",  aula_musica),
 ("Danca",  aula_danca),
]

#Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    atividade_sala1 = []
    atividade_sala2 = []
    
    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
    print("sala1", atividade_sala1)
    print("sala2", atividade_sala2)
    print("-" * 30)

    print()
    print("#" * 40)






