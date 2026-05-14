#Calculadora de IMC:
#solicita peso e altura, entrega IMC (numérico)

#input: imprime texto, coleta um dado e o armazena na variável:
peso_str = input("Peso (kg): ")
altura_str = input("Altura (m): ")

#float: converte texto (string) para número com vírgula:
peso = float(peso_str)
altura = float(altura_str)

print(f"Peso digitado: {peso}")
print(f"Altura digitada: {altura}")
# Fórmula: peso / (altura ** 2) # parêntese opcional nesse caso, para legibilidade.
imc = peso / (altura**2)
print(f"IMC calculado: {imc:.2f}")