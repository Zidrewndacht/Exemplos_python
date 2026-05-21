# Imprime a tabuada de um número solicitado usando loop for:

ntab = int(input("Digite valor da tabuada a gerar: "))

for multi in range(2, 10):
    print(f"{ntab} x {multi} = {ntab * multi}")

# como validar se a entrada é um número? Tente novamente se inválida
# como gerar a tabuada de todos os números de a (solicitado) até b (solicitado)?
#   Separe uma tabuada da outra por um espaço adicional
# por que não aparece 2x10?