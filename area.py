#Define a função calcular_area_comodos
def calcular_area_comodos():
    #Seta a area total para 0
    total_area = 0
    
    #Inicia uma estrutura de repetição que se mantem ate que seja retornado o valor False
    while True:
        
        #Define as variáveis largura e comprimento e pede ao usuário esses valores
        largura = float(input("Digite a largura do cômodo (em metros): "))
        comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

        #Calcula a area do comodo e printa ao usuário
        area_comodo = largura * comprimento
        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.")

        #Acrescenta a area total a area do ultimo comodo calculado
        total_area += area_comodo

        #Questiona ao usuário se gostaria de calcular a área de mais cômodos, define uma variável de valor booleano
        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()#função strip tira os espaços antes e depois de uma String, e função lower transforma tudo em minúsculo.
        #Se o usuário digitar que não quer mais cômodos o laço é interrompido
        if mais_comodos != 's':
            break
    return total_area
#A variável area_total recebe o valor retornado da variável total_area   
area_total = calcular_area_comodos()
#Printa a área total da casa.
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")