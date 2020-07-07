alunos = [("Val", 10), ("Renzo", 5), ("Ada", 17)]
alunos.sort(key=lambda aluno: aluno[1])
print(alunos)


def por_nome(aluno):
    return aluno[0]


print(sorted(alunos, key=por_nome))
