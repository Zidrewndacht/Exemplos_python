# tipagem.py
# 1. Concatenação vs Adição
x = 1
y = 2
print(f"{x} + {y} = {x + y}")  # 3

a = "4"
b = "5"
print(f"'{a}' + '{b}' = '{a + b}'")  # "45"

# 2. Conversão explícita necessária quando tipos diferem:
resultado_correto = int(a) + x  # ✅ 2
print(f"int('{a}') + {x} = {resultado_correto}")




# 3. Tipagem dinâmica: mesma variável, tipos diferentes:
valor = 100          # int
print(f"Tipo inicial: {type(valor).__name__}")  # int

valor = 100.5        # agora float
print(f"Tipo após atribuição: {type(valor).__name__}")  # float

valor = "cem"        # agora str
print(f"Tipo final: {type(valor).__name__}")  # str