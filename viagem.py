#Define a função calculaer_custo_viagem que utiliza de 5 parâmetros
def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios, custo_pedagio):
    #Cálculos do custo de combustivel total, pedagio total e custo total
    custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel

    custo_pedagio_total = numero_pedagios * custo_pedagio

    custo_total = custo_combustivel_total + custo_pedagio_total
    #Retorna os 3 valores calculados na função
    return custo_total, custo_combustivel_total, custo_pedagio_total

#Requisita ao usuário as informações sobre a viagem
distancia = float(input("Digite a distância da viagem (em km): "))
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): "))
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): "))
numero_pedagios = int(input("Digite o número de pedágios no percurso: "))
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): "))

#Recebe os valores retornados das funções e printa ao usuário
custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia,custo_combustivel,consumo_veiculo, numero_pedagios,custo_pedagio)
print(f"Custo total da viagem: R${custo_total:.2f}")
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}")
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}")