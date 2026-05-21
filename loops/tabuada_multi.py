# --- Leitura e validação da primeira tabuada ---
str_ntab_ini = input("Digite valor da primeira tabuada: ")
while not str_ntab_ini.isdigit():  # Repete enquanto a string NÃO conter apenas dígitos
    str_ntab_ini = input("Entrada inválida! Digite apenas números inteiros: ")
ntab_ini = int(str_ntab_ini)

# --- Leitura e validação da última tabuada ---
str_ntab_fim = input("Digite valor da última tabuada: ")
while not str_ntab_fim.isdigit():
    str_ntab_fim = input("Entrada inválida! Digite apenas números inteiros: ")
ntab_fim = int(str_ntab_fim)

# --- Geração das tabuadas usando loops for aninhados ---
for ntab in range(ntab_ini, ntab_fim + 1):
    print(f"\nTabuada do {ntab}:")
    for multi in range(2, 10):
        print(f"{ntab} x {multi} = {ntab * multi}")