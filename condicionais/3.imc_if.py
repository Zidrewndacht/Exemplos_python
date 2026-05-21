# imc_classificador.py
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)

# Classificação baseada em faixas da OMS
if imc < 18.5:
    categoria = "Abaixo do peso"
    risco = "Baixo"
elif imc < 25:
    categoria = "Peso normal"
    risco = "Normal"
elif imc < 30:
    categoria = "Sobrepeso"
    risco = "Moderado"
elif imc < 35:
    categoria = "Obesidade grau 1"
    risco = "Alto"
else:
    categoria = "Obesidade grau 2+"
    risco = "Muito alto"

print(f"\nIMC: {imc:.2f}")
print(f"Categoria: {categoria}")
print(f"Risco estimado: {risco}")

# Bônus: ternário para mensagem personalizada
mensagem = "Consulte um profissional" if risco in ["Alto", "Muito alto"] else "Mantenha hábitos saudáveis"
print(f"Recomendação: {mensagem}")