#  Instruções próximo exercício:
# Receba três valores: distância percorrida (km), km/L, preço do litro (R$).
# Calcule pelo menos duas das métricas abaixo:
#     Custo total da viagem;
#     Custo por km;
# Exiba cada métrica calculada em uma linha separada.

dist =      float(input("Distância do trajeto (km): "))
kml =       float(input("Consumo do veículo (km/L): "))
custo_l =   float(input("Custo do litro de combustível (R$/L): "))

litros_necessarios = dist / kml
print(f"Litros usados: {litros_necessarios:.2f}")

custo_total = custo_l * litros_necessarios
print(f"Custo do trajeto: R$ {custo_total:.2f}")

custo_km = custo_total / dist
print(f"Custo por km: R$ {custo_km:.2f}")
