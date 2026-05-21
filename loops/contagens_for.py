# contagem_simples_for.py
x = int(input("Início (x): "))
y = int(input("Fim (y): "))

for atual in range(x, y + 1):
    print(atual)


############################
# contagem_passo_for.py
x = int(input("Início: "))
y = int(input("Fim: "))
z = int(input("Passo: "))

for atual in range(x, y + 1, z):
    print(atual)


############################
# contagem_reversa_for.py
y = int(input("Início (y): "))
x = int(input("Fim (x): "))

for atual in range(y, x - 1, -1):
    print(atual)


############################
# contagem_reversa_passo_for.py
y = int(input("Início: "))
x = int(input("Fim: "))
z = int(input("Decremento: "))

for atual in range(y, x - 1, -z):
    print(atual)


############################
# contagem_auto_direcao_for.py
x = int(input("Início: "))
y = int(input("Fim: "))

passo = 1 if x <= y else -1
# range() exclui o valor de stop. Somamos/subtraímos 1 para incluir y.
stop = y + passo

for atual in range(x, stop, passo):
    print(atual)


############################
# contagem_auto_passo_for.py
x = int(input("Início: "))
y = int(input("Fim: "))
z = abs(int(input("Magnitude do passo: ")))

passo = z if x <= y else -z
stop = y + passo

for atual in range(x, stop, passo):
    print(atual)
