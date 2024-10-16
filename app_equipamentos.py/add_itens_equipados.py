import json
import os

def load_json(filename, default_data):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    else:
        with open(filename, 'w') as f:
            json.dump(default_data, f, indent=4)
        return default_data

# Caminhos dos arquivos
equipamentos_path = './historia/equipamentos/equipamentos.json'
cartas_path = './historia/inventario/cartas.json'
equipados_path = './historia/equipamentos/equipados.json'

# Carregar equipamentos e cartas
equipamentos = load_json(equipamentos_path, {"equipamentos": []})  # Ajustado para retornar uma estrutura padrão
cartas = load_json(cartas_path, {"cartas": []})  # Ajustado para retornar uma estrutura padrão

# Função para pegar os dados dos equipamentos
def get_dados_equipamentos(equipamentos):
    return [
        {
            "nome": equipamento['nome'],
            "atributos": equipamento['atributos'],
            "atributos_derivados": equipamento['atributos_derivados']
        }
        for equipamento in equipamentos['equipamentos']
    ]

# Função para pegar os dados das cartas
def get_dados_cartas(cartas):
    return [
        {
            "nome": carta['nome'],
            "atributos": carta['atributos'],
            "atributos_derivados": carta['atributos_derivados']
        }
        for carta in cartas['cartas']
    ]

# Função para adicionar um item ao arquivo equipados.json
def adicionar_item(nome_item, tipo):
    if tipo == "equipamento":
        for equipamento in dados_equipamentos:
            if equipamento['nome'] == nome_item:
                return equipamento
    elif tipo == "carta":
        for carta in dados_cartas:
            if carta['nome'] == nome_item:
                return carta
    return None

# Exibir dados dos equipamentos e cartas
dados_equipamentos = get_dados_equipamentos(equipamentos)
dados_cartas = get_dados_cartas(cartas)

print("Dados dos Equipamentos:")
for equipamento in dados_equipamentos:
    print(f"Nome: {equipamento['nome']}, Atributos: {equipamento['atributos']}, Atributos Derivados: {equipamento['atributos_derivados']}")

print("\nDados das Cartas:")
for carta in dados_cartas:
    print(f"Nome: {carta['nome']}, Atributos: {carta['atributos']}, Atributos Derivados: {carta['atributos_derivados']}")

# Solicitar ao usuário para adicionar um item
tipo_item = input("\nVocê deseja adicionar um 'equipamento' ou uma 'carta'? ").strip().lower()
nome_item = input("Digite o nome do item que você deseja adicionar: ").strip()

# Adicionar item ao arquivo equipados.json
item_adicionado = adicionar_item(nome_item, tipo_item)

if item_adicionado:
    # Criar ou atualizar o arquivo equipados.json
    if os.path.exists(equipados_path):
        with open(equipados_path, 'r') as f:
            equipados_data = json.load(f)
    else:
        equipados_data = {"equipamentos": [], "cartas": []}

    if tipo_item == "equipamento":
        equipados_data["equipamentos"].append(item_adicionado)
    elif tipo_item == "carta":
        equipados_data["cartas"].append(item_adicionado)

    with open(equipados_path, 'w') as f:
        json.dump(equipados_data, f, indent=4)

    print(f"Item '{nome_item}' adicionado ao arquivo '{equipados_path}'.")
else:
    print(f"O item '{nome_item}' não foi encontrado nos arquivos de {tipo_item}s.")
