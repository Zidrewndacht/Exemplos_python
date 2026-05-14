# Use Divisão inteira e resto (módulo):

# Receba um número de segundos do usuário
# Calcule horas, minutos e segundos usando // e %
# Exiba no formato HH:MM:SS, use var:02d para formato.

entrada_segundos = int(input("Digite tempo em segundos: "))

horas = entrada_segundos // 3600
segundos_restantes = entrada_segundos % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60


print(f"Resultado: {horas:02d}:{minutos:02d}:{segundos:02d}")

#  Instruções próximo exercício:

# Receba três valores: distância percorrida (km), km/L, preço do litro (R$).
# Calcule pelo menos duas das métricas abaixo:
#     Custo total da viagem;
#     Custo por km;
# Exiba cada métrica calculada em uma linha separada.
# Liberdade: Você decide a ordem dos cálculos, quais variáveis intermediárias 
# criar e quais métricas priorizar na saída.

# O que fazer com carro elétrico?
# "preço do litro" equivale a qual métrica relevante?
# Adapte a calculadora.


















# valor1 = 7
# valor2 = 3

# div = valor1 / valor2
# divint = valor1 // valor2
# mod = valor1 % valor2

# print(f"Divisão: {valor1} / {valor2}={div}")
# print(f"Divisão inteira: {valor1} // {valor2}={divint}")
# print(f"Resto da Divisão inteira: {valor1} % {valor2}={mod}")
