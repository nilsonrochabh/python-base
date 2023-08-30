#!/usr/bin/env python3
"""Relatorio de criancas por atividades
Imprimi a lista de crianças por sala que frequenta cada das atividades
"""
__version__ = "0.1.1"

sala1=["Erik", "Maria", "joão", "Gustavo", "Pedro", "sofia", "Joana"]
sala2= ["jose", "Carlos", "Maria", "Antonio", "Isadora"]

aula_ingles=["Erik", "Maria", "Joana", "Carlos", "Antonio"]
aula_musica=["Erik", "Carlos", "Maria"]
aula_danca=["Gustavo","Sofia", "Joana", "Antonio"]

atividades = [
    ("Ingles", aula_ingles), 
    ("Música", aula_musica), 
    ("Dança",aula_danca),
]
for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade {nome_atividade}\n")
    print("-"*50)
    
    atividade_sala1 =set(sala1) & set(atividade)
    atividade_sala2=set(sala2) & set(atividade)

    # for aluno in atividade:
    #     if aluno in sala1:
    #         atividade_sala1.append(aluno)
    #     elif aluno in sala2:
    #         atividade_sala2.append(aluno)
    print ("sala 1 ", atividade_sala1)
    print ("sala 2 ", atividade_sala2)
    print("#" * 50)