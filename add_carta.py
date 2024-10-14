import json
import os

def carregar_dados(arquivo):
    """Carrega os dados do arquivo JSON, ou cria uma nova estrutura se o arquivo não existir."""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    else:
        return {"cartas": []}

def salvar_dados(arquivo, dados):
    """Salva os dados no arquivo JSON."""
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def adicionar_carta(dados, nome_carta, atributos):
    """Adiciona uma nova carta com seus atributos."""
    nova_carta = {
        "nome": nome_carta,
        "atributos": atributos
    }
    dados['cartas'].append(nova_carta)

def main():
    arquivo = './historia/inventario/cartas.json'
    dados = carregar_dados(arquivo)

    # Definindo o nome da carta e os atributos diretamente
    nome_carta = "Carta do Dragão"  # Exemplo de nome de carta

    # Definindo os atributos da carta
    atributos = {
        "ATQ": 10,
        "MATQ": 5,
        "HIT": 2,
        "Critical": 3,
        "DEF": 0,
        "MDEF": 0,
        "flee": 1,
        "aspd": 0,
        "STR": 2,
        "AGI": 1,
        "VIT": 0,
        "INT": 0,
        "DEX": 3,
        "LUK": 0,
        "efeito_passivo": "Aumenta o dano de ataque em 15%",
        "efeito_ativo": "Causa um ataque de fogo",
    }

    adicionar_carta(dados, nome_carta, atributos)
    salvar_dados(arquivo, dados)

    print("Carta adicionada com sucesso!")

if __name__ == "__main__":
    main()
