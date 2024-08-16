#Define a função calcular juros que utiliza 3 parametros: valor_principal, taxa_juros_anual e dias_atraso
def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso):
    #Seta a taxa de juros diaria com base na anual e transofrma em porcentagem
    taxa_juros_diaria = taxa_juros_anual / 365 / 100
    #Calcula a taxa de juros
    juros = valor_principal * taxa_juros_diaria * dias_atraso
    #Calculo do valor final apos a manutenção dos juros
    valor_total = valor_principal + juros
    return valor_total, juros

valor_principal = 1000.00
taxa_juros_anual = 5.0
dias_atraso = 30
#Passa os 3 parametros necessários para a função calcular_juros_atraso
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)
#Mostra ao usuário o valor final a ser pago e quanto desse valor são juros
print(f"Valor total a ser pago: R${valor_total:.2f}")
print(f"Valor dos juros: R${juros:.2f}")