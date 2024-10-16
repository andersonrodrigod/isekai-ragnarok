import random

# Definição dos itens que o Poring pode dropar e suas taxas de drop
itens_poring = [
    {"id": 909, "nome": "Jellopy", "drop": 70},
    {"id": 1202, "nome": "Faca [4]", "drop": 1},
    {"id": 938, "nome": "Muco Pegajoso", "drop": 4},
    {"id": 512, "nome": "Maçã", "drop": 10},
    {"id": 601, "nome": "Asa de Mosca", "drop": 5},
    {"id": 619, "nome": "Maçã Verde", "drop": 0.2},
    {"id": 4001, "nome": "Carta Poring", "drop": 0.2}
]

# Função para simular o drop de um item com base na taxa de drop
def simular_drop():
    drops = []  # Lista para armazenar os itens dropados dessa tentativa

    # Verifica cada item individualmente com base na sua taxa de drop
    for item in itens_poring:
        chance = random.uniform(0, 100)  # Gera um número aleatório entre 0 e 100
        if chance <= item["drop"]:  # Se a chance for menor ou igual à taxa de drop, o item é dropado
            drops.append(item["nome"])  # Adiciona o item à lista de drops

    return drops  # Retorna a lista com os itens que foram dropados

# Função para simular matar N Porings e coletar os itens
def matar_porings(quantidade):
    itens_dropados = {}  # Dicionário para armazenar os itens e quantidades

    # Simula matar 'quantidade' Porings
    for _ in range(quantidade):
        itens = simular_drop()  # Obtém os itens dropados nessa tentativa
        for item in itens:
            if item in itens_dropados:
                itens_dropados[item] += 1  # Se o item já foi dropado, incrementa a quantidade
            else:
                itens_dropados[item] = 1  # Se o item ainda não foi dropado, adiciona no dicionário com quantidade 1

    return itens_dropados  # Retorna o dicionário com todos os itens dropados e suas quantidades

# Programa principal
if __name__ == "__main__":
    # Entrada do usuário: quantos Porings ele quer matar
    vezes = int(input("How many Porings do you want to kill? "))

    # Simula matar os Porings e armazenar os drops
    resultado = matar_porings(vezes)

    # Exibe os itens que foram dropados e suas quantidades
    if resultado:
        print("\nYou have obtained the following items:")
        for item, quantidade in resultado.items():
            print(f"{item}: {quantidade}x")
    else:
        print("\nVocê não conseguiu nenhum item.")
