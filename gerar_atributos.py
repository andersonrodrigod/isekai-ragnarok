import json
import os

# Caminhos dos arquivos
atributos_path = './historia/inventario/atributos.json'
status_equipamentos_path = './historia/inventario/status_equipamentos.json'
atributos_totais_path = './historia/inventario/atributos_totais.json'
atributos_finais_path = './historia/inventario/atributos_finais.json'

# Função para calcular atributos finais
def calcular_atributos_finais():
    # Lê os atributos do arquivo de status de equipamentos
    with open(status_equipamentos_path, 'r') as f:
        status_equipamentos = json.load(f)

    # Lê os atributos do arquivo de atributos
    with open(atributos_path, 'r') as f:
        atributos_data = json.load(f)

    # Obtém os atributos do último capítulo
    ultimo_capitulo = atributos_data['capitulos'][-1]['atributos']

    # Lê os atributos totais
    with open(atributos_totais_path, 'r') as f:
        atributos_totais = json.load(f)

    # Inicializa um dicionário para os atributos finais
    atributos_finais = {
        "STR": 0,
        "AGI": 0,
        "VIT": 0,
        "INT": 0,
        "DEX": 0,
        "LUK": 0,
        "ATQ": 0,
        "MATQ": 0,
        "HIT": 0,
        "Critical": 0,
        "DEF": 0,
        "MDEF": 0,
        "flee": 0,
        "aspd": 0,
        "HP": 0,
        "MP": 0
    }

    # Soma os atributos do arquivo de status de equipamentos com os atributos do último capítulo
    for key in atributos_finais.keys():
        if key in status_equipamentos['atributos_totais']:
            atributos_finais[key] += status_equipamentos['atributos_totais'][key]
        if key in ultimo_capitulo:
            atributos_finais[key] += ultimo_capitulo[key]

    # Soma os atributos derivados totais
    for key in atributos_finais.keys():
        if key in status_equipamentos['atributos_derivados_totais']:
            atributos_finais[key] += status_equipamentos['atributos_derivados_totais'][key]
        if key in atributos_totais:
            atributos_finais[key] += atributos_totais[key]

    return atributos_finais

# Calcula os atributos finais
atributos_finais = calcular_atributos_finais()

# Cria o arquivo se não existir
if not os.path.exists(atributos_finais_path):
    with open(atributos_finais_path, 'w') as f:
        json.dump({}, f, indent=4)  # Cria um arquivo vazio

# Salva os resultados no novo arquivo
with open(atributos_finais_path, 'w') as f:
    json.dump(atributos_finais, f, indent=4)

print(f"Arquivo '{atributos_finais_path}' criado/atualizado com os atributos finais calculados.")
