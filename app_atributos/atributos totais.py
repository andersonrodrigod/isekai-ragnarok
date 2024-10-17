import json
import os

# Caminho do arquivo de atributos
atributos_path = './historia/atributos/atributos.json'
# Caminho do novo arquivo de atributos totais
atributos_totais_path = './historia/atributos/atributos_totais.json'

# Função para calcular atributos totais
def calcular_atributos_totais(capitulo):
    atributos = capitulo['atributos']
    status_geral = capitulo['status_geral']

    # Inicializa os valores de atributos
    atributos_totais = {
        "ATQ": 0,
        "MATQ": 0,
        "HIT": 0,
        "Critical": 0,
        "DEF": 0,
        "MDEF": 0,
        "flee": 0,
        "aspd": 100,
        "HP": status_geral["HP"],  # Usa o HP já calculado
        "MP": status_geral["MP"]   # Usa o MP já calculado
    }

    # Cálculos baseados nos atributos
    atributos_totais["ATQ"] += atributos.get("STR", 0) * 1  # A cada ponto em STR = ATQ +1
    atributos_totais["flee"] += atributos.get("AGI", 0) * 1  # A cada ponto em AGI = flee + 1
    atributos_totais["MDEF"] += atributos.get("AGI", 0) // 5  # A cada 5 pontos de AGI = MDEF + 1

    vits = atributos.get("VIT", 0)
    atributos_totais["DEF"] += vits // 2  # A cada 2 pontos em VIT = DEF + 1
    atributos_totais["MDEF"] += vits // 5  # A cada 5 pontos em VIT = MDEF + 1
    atributos_totais["aspd"] += atributos.get("AGI", 0) * 1  # A cada ponto em AGI = aspd + 1
   

    atributos_totais["MATQ"] += atributos.get("INT", 0) * 1.5  # A cada ponto em INT = MATQ + 1,5
    atributos_totais["MDEF"] += atributos.get("INT", 0) // 2  # A cada 2 pontos em INT = MDEF + 1

    atributos_totais["MATQ"] += atributos.get("DEX", 0) * 1  # A cada ponto em DEX = MATQ + 1
    atributos_totais["HIT"] += atributos.get("DEX", 0) * 1  # A cada ponto em DEX = HIT + 1
    atributos_totais["MATQ"] += atributos.get("DEX", 0) // 5  # A cada 5 pontos em DEX = MATQ +1
    atributos_totais["MDEF"] += atributos.get("DEX", 0) // 5  # A cada 5 pontos em DEX = MDEF +1

    atributos_totais["Critical"] += atributos.get("LUK", 0) // 3  # A cada 3 pontos em LUK = Critical + 1
    atributos_totais["ATQ"] += atributos.get("LUK", 0) // 3  # A cada 3 pontos em LUK = ATQ + 1
    atributos_totais["MATQ"] += atributos.get("LUK", 0) // 3  # A cada 3 pontos em LUK = MATQ + 1
    atributos_totais["HIT"] += atributos.get("LUK", 0) // 3  # A cada 3 pontos em LUK = HIT +1
    atributos_totais["aspd"] += atributos.get("LUK", 0) // 5  # A cada 5 pontos em LUK = aspd +1

    return atributos_totais

# Verifica se o arquivo de atributos existe
if os.path.exists(atributos_path):
    with open(atributos_path, 'r') as f:
        atributos_data = json.load(f)

    # Obtém o último capítulo
    ultimo_capitulo = atributos_data['capitulos'][-1]

    # Calcula os atributos totais
    atributos_totais = calcular_atributos_totais(ultimo_capitulo)

    # Cria o arquivo se não existir
    if not os.path.exists(atributos_totais_path):
        with open(atributos_totais_path, 'w') as f:
            json.dump({}, f, indent=4)  # Cria um arquivo vazio

    # Salva os resultados no novo arquivo
    with open(atributos_totais_path, 'w') as f:
        json.dump(atributos_totais, f, indent=4)

    print(f"Arquivo '{atributos_totais_path}' criado/atualizado com os atributos totais calculados.")
else:
    print(f"O arquivo '{atributos_path}' não foi encontrado.")
