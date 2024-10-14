import json
import os

def carregar_dados(arquivo):
    """Carrega os dados do arquivo JSON, ou cria uma nova estrutura se o arquivo não existir."""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    else:
        return {"equipamentos": []}

def salvar_dados(arquivo, dados):
    """Salva os dados no arquivo JSON."""
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def adicionar_equipamento(dados, nome_equipamento, atributos):
    """Adiciona um novo equipamento com seus atributos."""
    novo_equipamento = {
        "nome": nome_equipamento,
        "atributos": atributos
    }
    dados['equipamentos'].append(novo_equipamento)

def main():
    arquivo = './historia/inventario/equipamentos.json'
    dados = carregar_dados(arquivo)

    # Definindo o nome do equipamento e os atributos diretamente
    nome_equipamento = "Clava [3]"  # Exemplo de nome de equipamento

    # Definindo os atributos do equipamento
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

    adicionar_equipamento(dados, nome_equipamento, atributos)
    salvar_dados(arquivo, dados)

    print("Equipamento adicionado com sucesso!")

if __name__ == "__main__":
    main()
