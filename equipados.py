import json
import os

def carregar_dados(arquivo):
    """Carrega os dados do arquivo JSON, ou cria uma nova estrutura se o arquivo não existir."""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    else:
        return {"capitulos": []}

def salvar_dados(arquivo, dados):
    """Salva os dados no arquivo JSON."""
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_equipamentos(arquivo):
    """Carrega os dados dos equipamentos do arquivo JSON."""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    else:
        return {"equipamentos": []}

def carregar_cartas(arquivo):
    """Carrega os dados das cartas do arquivo JSON."""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    else:
        return {"cartas": []}

def somar_atributos(equipamentos, cartas):
    """Soma os atributos de equipamentos e cartas."""
    atributos_totais = {
        "ATQ": 0,
        "MATQ": 0,
        "HIT": 0,
        "Critical": 0,
        "DEF": 0,
        "MDEF": 0,
        "flee": 0,
        "aspd": 0,
        "STR": 0,
        "AGI": 0,
        "VIT": 0,
        "INT": 0,
        "DEX": 0,
        "LUK": 0,
        "efeito_passivo": "",
        "efeito_ativo": ""
    }

    # Soma os atributos dos equipamentos
    for equipamento in equipamentos:
        for key, value in equipamento.get('atributos', {}).items():
            if key in atributos_totais:
                atributos_totais[key] += value

    # Soma os atributos das cartas
    for carta in cartas:
        for key, value in carta.get('atributos', {}).items():
            if key in atributos_totais:
                atributos_totais[key] += value

    return atributos_totais

def adicionar_equipamentos(dados, capitulo, equipamentos_equipados):
    """Adiciona os equipamentos e as cartas ao capítulo, somando os atributos."""
    novo_capitulo = {
        "capitulo": capitulo,
        "equipamentos": equipamentos_equipados,
        "atributos_totais": {}
    }

    # Carrega os equipamentos e cartas
    equipamentos_data = carregar_equipamentos('./historia/inventario/equipamentos.json')
    cartas_data = carregar_cartas('./historia/inventario/cartas.json')

    # Acessa as listas de equipamentos e cartas
    equipamentos = equipamentos_data.get('equipamentos', [])
    cartas = cartas_data.get('cartas', [])

    # Filtra os equipamentos e cartas equipados
    equipamentos_info = [equipamento for equipamento in equipamentos if equipamento['nome'] in equipamentos_equipados]
    cartas_info = [carta for carta in cartas if carta['nome'] in equipamentos_equipados]

    # Soma os atributos
    atributos_totais = somar_atributos(equipamentos_info, cartas_info)

    novo_capitulo["atributos_totais"] = atributos_totais
    dados['capitulos'].append(novo_capitulo)

def main():
    arquivo = './historia/inventario/equipamentos_equipados.json'
    dados = carregar_dados(arquivo)

    capitulo_atual = 8  # Defina o número do capítulo que está adicionando

    # Lista de equipamentos e cartas que deseja adicionar
    equipamentos_equipados = [
        "Clava [3]",
        "Carta do Dragao",  # Exemplo de carta que pode ser adicionada
        # Adicione mais equipamentos e cartas conforme necessário
    ]

    adicionar_equipamentos(dados, capitulo_atual, equipamentos_equipados)
    salvar_dados(arquivo, dados)

    print("Equipamentos e cartas adicionados com sucesso!")

if __name__ == "__main__":
    main()
