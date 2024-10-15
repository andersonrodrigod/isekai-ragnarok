import json

def calcular_hp_sp(nivel):
    # Valores base
    hp_base = 100  # HP base do mercador
    hp_por_nivel = 10  # HP por nível do mercador
    sp_base = 10  # SP base do mercador
    sp_por_nivel = 5  # SP por nível do mercador

    # Cálculo do HP e SP
    hp = hp_base + (nivel * hp_por_nivel)
    sp = sp_base + (nivel * sp_por_nivel)

    return hp, sp

def atualizar_arquivo_json(caminho_arquivo, nivel):
    # Abre o arquivo JSON
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        dados = json.load(file)

    # Calcula HP e SP com base no nível
    hp, sp = calcular_hp_sp(nivel)

    # Atualiza os valores no JSON
    for capitulo in dados['capitulos']:
        capitulo['status_geral']['HP'] = hp
        capitulo['status_geral']['MP'] = sp

    # Salva as alterações de volta no arquivo JSON
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print(f"Valores atualizados: HP = {hp}, SP = {sp}")

# Solicita o nível do protagonista
nivel = int(input("Digite o nível do protagonista: "))

# Atualiza o arquivo JSON
atualizar_arquivo_json('./historia/inventario/atributos.json', nivel)
