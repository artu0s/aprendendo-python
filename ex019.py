# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome do escolhido.

import random

aluno1 = str(input("Nome do aluno um: "))
aluno2 = str(input("Nome do aluno dois: "))
aluno3 = str(input("Nome do aluno três: "))
aluno4 = str(input("Nome do aluno quatro: "))
lista = [aluno1, aluno2, aluno3, aluno4]
sortear = random.choice(lista)
print("O aluno sorteado foi o {}".format(sortear))