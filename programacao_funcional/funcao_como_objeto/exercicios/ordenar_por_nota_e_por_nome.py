'''
Construa uma função de ordenação que ordene os alunos por nota.
 Se houver empate em nota, o nome deve definir a ordem.
 #>>> alunos= [('Renzo',0),('Luciano',10),('Renzo Santos',10),('Renzo Nuccitelli',10)]
 #>>> alunos.sort(key=ordenar_por_nota_e_nome)
# >>> alunos
[('Renzo',0),('Luciano',10),('Renzo Santos',10),('Renzo Nuccitelli',10)]
'''

alunos = [('Renzo', 0), ('Luciano', 20), ('Renzo Santos', 20), ('Renzo Nuccitelli', 10)]

# def ordenar_por_nota_e_nome(aluno):
#     nome, nota = aluno
#     return nota, nome
#
#
# alunos.sort(key=ordenar_por_nota_e_nome)
#
# for key in alunos:
#     print(key, ';')

import operator

alunos = [('Renzo', 0), ('Luciano', 20),
          ('Renzo Santos', 20), ('Renzo Nuccitelli', 10)]


ordernar_nota_nome = operator.itemgetter(1, 0)
alunos.sort(key=ordernar_nota_nome)

print(alunos)
