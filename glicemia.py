#Define a função diagnosticar_diabetes com 2 parâmetros glicemia_em_jejum, glicemia_pos_prandial
def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial):

    #Grande estrutura condicional que realiza o diagnóstico com base nos valores cedidos pelo usuário, quando cumprida a condição ela retorna o valor para a função
    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200:
        return "Diabetes"
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:
        return "Pré-diabetes"
    else:
        return "Normal"

#Pede ao usuário para que digite as 2 variáveis necessária para a execução da função
glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))

#A variável resultado é o valor que a função retornar
resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)
print(f"O diagnóstico é: {resultado}")