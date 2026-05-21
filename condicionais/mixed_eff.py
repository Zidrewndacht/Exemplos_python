# EXERCÍCIO: Comparador de Custo de Trajeto (Combustão vs EV)
# OBJETIVO:
# Calcular e comparar o custo energético de um trajeto entre
# um veículo a combustão e um elétrico, usando métricas reais.
#
# DADOS DE ENTRADA:
# • Distância do trajeto (km)
# • Combustão: Consumo (km/L) e Preço do combustível (R$/L)
# • Elétrico: Consumo (MJ/km - unidade INMETRO) e Tarifa de energia (R$/kWh)
#
# INSTRUÇÕES:
# 1. Leia a distância.
# 2. Para cada tipo de veículo, peça os dois dados necessários.
#    - Se o usuário deixar um campo em branco (apenas Enter),
#      considere que ele NÃO quer calcular para aquele tipo.
#    - Use condicionais simples (if string:) para decidir o cálculo.
# 3. Mantenha TODOS os cálculos na base "por km". Evite normalizações
#    arbitrárias (como /100km) no meio do processamento.
#    - Para o EV, converta MJ/km → kWh/km usando a constante 3.6.
# 4. Calcule o custo total e o custo por km apenas se os dados foram fornecidos.
# 5. Se AMBOS os tipos tiverem dados, exiba a diferença absoluta de custo.
# 6. Inicialize variáveis de resultado com None antes dos ifs para evitar NameError.
#
# RESTRIÇÕES:
# • Não use loops, funções ou tratamento de erros (try/except).
# • Máximo de 2 níveis de indentação.
# • Saída apenas com print() e f-strings básicas.
# ============================================================

# 1. ENTRADA COMUM
distancia = float(input("Distância do trajeto (km): "))

# 2. ENTRADAS OPCIONAIS (Combustão)
print("\n--- Veículo a Combustão (deixe em branco para pular) ---")
km_l_str = input("Consumo (km/L): ").strip()
preco_litro_str = input("Preço do combustível (R$/L): ").strip()

# 3. ENTRADAS OPCIONAIS (Elétrico)
print("\n--- Veículo Elétrico (deixe em branco para pular) ---")
mj_km_str = input("Consumo (MJ/km): ").strip()
preco_kwh_str = input("Tarifa de energia (R$/kWh): ").strip()

# 4. INICIALIZAÇÃO DE SENTINELS (Evita NameError em ramos não executados)
custo_comb_total = None
custo_comb_km = None
custo_ele_total = None
custo_ele_km = None

# 5. PROCESSAMENTO: COMBUSTÃO
if km_l_str and preco_litro_str:
    km_l = float(km_l_str)
    preco_litro = float(preco_litro_str)
    
    # Base por km: L/km = 1 / (km/L)
    litros_por_km = 1 / km_l
    custo_comb_km = litros_por_km * preco_litro
    custo_comb_total = custo_comb_km * distancia
    
    print(f"\n[Combustão] Custo total: R$ {custo_comb_total:.2f}")
    print(f"[Combustão] Custo por km: R$ {custo_comb_km:.4f}")

# 6. PROCESSAMENTO: ELÉTRICO
if mj_km_str and preco_kwh_str:
    mj_km = float(mj_km_str)
    preco_kwh = float(preco_kwh_str)
    
    # Conversão dimensional: 1 kWh = 3.6 MJ
    kwh_por_km = mj_km / 3.6
    custo_ele_km = kwh_por_km * preco_kwh
    custo_ele_total = custo_ele_km * distancia
    
    print(f"\n[Elétrico] Custo total: R$ {custo_ele_total:.2f}")
    print(f"[Elétrico] Custo por km: R$ {custo_ele_km:.4f}")

# 7. COMPARAÇÃO (Apenas se ambos os ramos foram executados)
if custo_comb_total is not None and custo_ele_total is not None:
    diferenca = custo_comb_total - custo_ele_total
    print(f"\n=== Comparação ===")
    print(f"Diferença absoluta: R$ {abs(diferenca):2f}")
    # Ternário simples para indicar o mais econômico
    print(f"{'Combustão' if diferenca < 0 else 'Elétrico'} é mais econômico para este trajeto.")