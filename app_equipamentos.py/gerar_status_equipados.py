import json
import os

# Caminho do arquivo equipados
equipados_path = './historia/equipamentos/equipados.json'
# Caminho do novo arquivo de status
status_equipamentos_path = './historia/equipamentos/status_equipamentos.json'

# Função para somar atributos e atributos derivados
def somar_atributos(equipados):
    # Inicializa dicionários para os totais
    total_atributos = {
        "STR": 0,
        "AGI": 0,
        "VIT": 0,
        "INT": 0,
        "DEX": 0,
        "LUK": 0
    }
    
    total_atributos_derivados = {
        "ATQ": 0,
        "MATQ": 0,
        "HIT": 0,
        "Critical": 0,
        "DEF": 0,
        "MDEF": 0,
        "flee": 0,
        "aspd": 0
    }

    # Itera sobre os equipamentos e cartas
    for equipamento in equipados.get("equipamentos", []):
        for atributo, valor in equipamento['atributos'].items():
            total_atributos[atributo] += valor
        for atributo_derivado, valor in equipamento['atributos_derivados'].items():
            if atributo_derivado in total_atributos_derivados:
                total_atributos_derivados[atributo_derivado] += valor

    for carta in equipados.get("cartas", []):
        for atributo, valor in carta['atributos'].items():
            total_atributos[atributo] += valor
        for atributo_derivado, valor in carta['atributos_derivados'].items():
            if atributo_derivado in total_atributos_derivados:
                total_atributos_derivados[atributo_derivado] += valor

    return {
        "atributos_totais": total_atributos,
        "atributos_derivados_totais": total_atributos_derivados
    }

# Verifica se o arquivo equipados existe
if os.path.exists(equipados_path):
    with open(equipados_path, 'r') as f:
        equipados_data = json.load(f)

    # Soma os atributos
    status_equipamentos = somar_atributos(equipados_data)

    # Cria o arquivo se não existir
    if not os.path.exists(status_equipamentos_path):
        with open(status_equipamentos_path, 'w') as f:
            json.dump({}, f, indent=4)  # Cria um arquivo vazio

    # Salva os resultados no novo arquivo
    with open(status_equipamentos_path, 'w') as f:
        json.dump(status_equipamentos, f, indent=4)

    print(f"Arquivo '{status_equipamentos_path}' criado/atualizado com os resultados dos atributos dos itens equipados.")
else:
    print(f"O arquivo '{equipados_path}' não foi encontrado.")
