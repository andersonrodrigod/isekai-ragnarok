import json
import os

def carregar_dados(arquivo):
    """Carrega os dados do arquivo JSON, ou cria uma nova estrutura se o arquivo não existir."""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    else:
        return {"buffs": []}

def salvar_dados(arquivo, dados):
    """Salva os dados no arquivo JSON."""
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def adicionar_buff(dados, nome_buff, atributos):
    """Adiciona um novo buff com seus atributos."""
    novo_buff = {
        "nome": nome_buff,
        "atributos": atributos
    }
    dados['buffs'].append(novo_buff)

def main():
    arquivo = './historia/inventario/buffs.json'
    dados = carregar_dados(arquivo)

    # Definindo o nome do buff e os atributos diretamente
    nome_buff = "Buff da Força"  # Exemplo de nome de buff

    # Definindo os atributos do buff
    atributos = {
        "ATQ": 5,
        "MATQ": 0,
        "HIT": 3,
        "Critical": 2,
        "DEF": 0,
        "MDEF": 0,
        "flee": 0,
        "aspd": 0,
        "STR": 3,
        "AGI": 0,
        "VIT": 0,
        "INT": 0,
        "DEX": 2,
        "LUK": 0,
        "efeito_passivo": "Aumenta o ataque em 10%",
        "efeito_ativo": "Aumenta a força temporariamente",
    }

    adicionar_buff(dados, nome_buff, atributos)
    salvar_dados(arquivo, dados)

    print("Buff adicionado com sucesso!")

if __name__ == "__main__":
    main()
