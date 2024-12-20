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

def adicionar_equipamento(dados, nome_equipamento, atributos, atributos_derivados):
    """Adiciona um novo equipamento com seus atributos e atributos derivados."""
    novo_equipamento = {
        "nome": nome_equipamento,
        "atributos": atributos,
        "atributos_derivados": atributos_derivados
    }
    dados['equipamentos'].append(novo_equipamento)

def main():
    arquivo = './historia/equipamentos/equipamentos.json'
    dados = carregar_dados(arquivo)

    # Definindo o nome do equipamento
    nome_equipamento = "Clava [4]"  # Exemplo de nome de equipamento

    # Definindo os atributos do equipamento
    atributos = {
        "STR": 1,
        "AGI": 0,
        "VIT": 0,
        "INT": 0,
        "DEX": 0,
        "LUK": 0,
    }

    # Definindo os atributos derivados do equipamento
    atributos_derivados = {
        "ATQ": 23,
        "MATQ": 0,
        "HIT": 0,
        "Critical": 0,
        "DEF": 0,
        "MDEF": 0,
        "flee": 0,
        "aspd": 0,
        "peso": 70,  # Adicionando o peso
        "efeito_passivo": "",
        "efeito_ativo": "",
        "descricao": "Um porrete robusto e pesado. "
    }

    adicionar_equipamento(dados, nome_equipamento, atributos, atributos_derivados)
    salvar_dados(arquivo, dados)

    print("Equipamento adicionado com sucesso!")

if __name__ == "__main__":
    main()
