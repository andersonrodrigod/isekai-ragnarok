import json
import os

# Caminho para o arquivo JSON
caminho_arquivo = './historia/itens/valor_itens.json'

# Função para carregar os itens do arquivo JSON
def carregar_itens():
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    else:
        # Se o arquivo não existir, retorna um dicionário vazio
        return {}

# Função para salvar os itens no arquivo JSON (cria o arquivo se ele não existir)
def salvar_itens(itens):
    # Garante que o diretório existe, cria o arquivo se não existir
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
    
    with open(caminho_arquivo, 'w') as arquivo:
        json.dump(itens, arquivo, indent=4)

# Função para adicionar um item à loja
def adicionar_item():
    nome_item = input("Digite o nome do item: ")
    valor_item = float(input("Digite o valor do item: "))

    # Carregar os itens existentes
    itens = carregar_itens()

    # Adicionar o novo item
    itens[nome_item] = valor_item

    # Salvar os itens no arquivo JSON
    salvar_itens(itens)

    # Calcular e exibir o valor com lucro de 15%
    lucro = valor_item * 0.15
    valor_com_lucro = valor_item + lucro

    print(f"Item: {nome_item}")
    print(f"Valor original: R$ {valor_item:.2f}")
    print(f"{valor_com_lucro:.2f}")

# Programa principal
adicionar_item()
