#Define a função que realiza o cálculo do IMC com base nos parâmetros peso e altura
def calcular_imc(peso, altura):

    imc = peso / (altura ** 2)
    return imc

#Define a classificação da pessoa com base no valor do imc retornado pela 1ª função
def classificar_imc(imc):
    
    #Uma série de estruturas condicionais que retornam o "diagnóstico" do usuário
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

#Com base no valor retornado pela função classificar_imc o programa retorna uma recomendação
def sugestao_atividade_fisica(classificacao_imc):

    #Estruturas condicionais que utilizam do valor recebido da 2ª função para realizar a condicional
    if classificacao_imc == "Abaixo do peso":
        return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em proteínas e calorias."
    elif classificacao_imc == "Peso normal":
        return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e natação, junto a um treino de força moderado."
    elif classificacao_imc == "Sobrepeso":
        return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além de exercícios de resistência."
    elif classificacao_imc == "Obesidade grau 1":
        return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um programa de reeducação alimentar."
    elif classificacao_imc == "Obesidade grau 2":
        return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e acompanhamento nutricional."
    else:
        return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica, fisioterapia, e consultas regulares com um nutricionista."

#Requisita ao usuário seu peso e altura
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em centímetros): "))

#Recebe os valores retornados das funções
imc = calcular_imc(peso, altura)
classificacao_imc = classificar_imc(imc)
sugestao = sugestao_atividade_fisica(classificacao_imc)

#Printa os valores
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao_imc}")
print(f"Sugestão de atividade física: {sugestao}")