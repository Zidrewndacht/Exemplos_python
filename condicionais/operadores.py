# logicos.py
# 1. Operadores lógicos com condicionais
nota = float(input("Nota (0-10): "))
frequencia = float(input("Frequência (%): "))

# Aprovação: nota >= 7 E frequência >= 75%
if nota >= 7 and frequencia >= 75:
    situacao = "Aprovado"
elif nota < 5 or frequencia < 50:
    situacao = "Reprovado"
else:
    situacao = "Recuperação"

print(f"Situação: {situacao}")

# 2. Condicional ternário (expressão inline)
# formato: valor_se_verdadeiro if condicao else valor_se_falso
conceito = "A" if nota >= 9 else "B" if nota >= 7 else "C" if nota >= 5 else "D"
print(f"Conceito: {conceito}")

# 3. Exemplo prático: desconto com múltiplas condições
idade = int(input("Idade: "))
valor_compra = float(input("Valor da compra (R$): "))

# Desconto se: idoso (>=65) OU criança (<12) E compra > 100
desconto_elegivel = (idade >= 65 or idade < 12) and valor_compra > 100
valor_final = valor_compra * 0.9 if desconto_elegivel else valor_compra

print(f"Desconto aplicado: {'Sim' if desconto_elegivel else 'Não'}")
print(f"Total a pagar: R$ {valor_final:.2f}")