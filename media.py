#Define a função calcular_media_e_aprovacao com 2 parametros: notas e nota_minima_aprovacao
def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):
    #Seta a variável total_notas
    total_notas = 0
    num_alunos = len(notas) #Função len() retorna o número de itens em uma lista, calculando assim o n° de alunos
    #Seta 2 listas
    aprovados = []
    reprovados = []

    #Inicia um laço de repetição que para os alunos e as notas na lista "notas" soma no total_notas, calcula se o aluno vai reprovar ou não e o insere na lista correta.
    for aluno, nota in notas.items():
        total_notas += nota
        if nota >= nota_minima_aprovacao:
            aprovados.append(aluno)
        else:
            reprovados.append(aluno)
    #Cálculo da média das notas
    media_turma = total_notas / num_alunos

    #retorna as 2 listas e a média
    return media_turma, aprovados, reprovados

#Lista "notas"em que o laço irá passar, que contém os alunos e as suas notas. 
notas = {
    "Alice": 85,
    "Bruno": 72,
    "Carlos": 60,
    "Diana": 95,
    "Eduardo": 55
}

#Seta a nota mínima para aprovação
nota_minima_aprovacao = 70

#Faz a requisição das variáveis retornadas da função calcular_media_e_aprovacao e as printa em seguida
media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)
print(f"Média da turma: {media_turma:.2f}")
print(f"Alunos aprovados: {', '.join(aprovados)}")
print(f"Alunos reprovados: {', '.join(reprovados)}")