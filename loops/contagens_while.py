# contagem_simples.py
x = int(input("Início (x): "))
y = int(input("Fim (y): "))

atual = x
while atual <= y:
    print(atual)
    atual += 1  # ⚠️ Atualização obrigatória para evitar loop infinito

############################
# contagem_passo.py
x = int(input("Início: "))
y = int(input("Fim: "))
z = int(input("Passo: "))

atual = x
while atual <= y:
    print(atual)
    atual += z

############################
# contagem_reversa.py
y = int(input("Início (y): "))
x = int(input("Fim (x): "))

atual = y
while atual >= x:
    print(atual)
    atual -= 1

############################
# contagem_reversa_passo.py
y = int(input("Início: "))
x = int(input("Fim: "))
z = int(input("Decremento: "))

atual = y
while atual >= x:
    print(atual)
    atual -= z

############################
# contagem_auto_direcao.py
x = int(input("Início: "))
y = int(input("Fim: "))

atual = x
passo = 1 if x <= y else -1

# Condição composta: verifica direção e limite simultaneamente
while (passo > 0 and atual <= y) or (passo < 0 and atual >= y):
    print(atual)
    atual += passo


############################
# contagem_auto_passo.py
x = int(input("Início: "))
y = int(input("Fim: "))
z = abs(int(input("Magnitude do passo: ")))  # Garante valor positivo

atual = x
passo = z if x <= y else -z

while (passo > 0 and atual <= y) or (passo < 0 and atual >= y):
    print(atual)
    atual += passo

