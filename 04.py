alunos=int(input("quantos alunos tem na sala?"))
i=1
notas=0
soma=0
while i <=alunos:
    notas=float(input("qual foi a nota dos aluno?"))
    soma+=notas
    i = i + 1
media=soma/alunos
print(media)