# Recebe uma idade entre 0 e 120.
# Repete até valor válido ser entregue:

idade_valida = False #indica se a idade é válida ou não

# while: repete enquanto a condição for verdadeira:
while not idade_valida: #enquanto a idade não for válida:
    entrada = input("Informe a idade (0 a 120): ").strip()

    #Verifica se é numérico e está no intervalo:
    if entrada.isdigit():
        idade = int(entrada)
        print(f"Idade digitada: {idade}.")
        if 0 <= idade <= 120: # alternativa: idade>=0 and idade<=120
            print("Idade válida")
            idade_valida = True
        else:
            print("Idade fora da faixa permitida (precisa ser 0 a 120)")
    else:
        print("Entrada inválida. Tente novamente")

print("Entrada válida. Finalizando programa.")

# Como validar o intervalo? Tente novamente se for menor que zero ou maior que 120.
# Onde atualizar idade_valida para True?