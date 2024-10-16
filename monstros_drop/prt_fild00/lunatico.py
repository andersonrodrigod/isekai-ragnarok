import random

# Definição dos itens que o Lunático pode dropar e suas taxas de drop
itens_lunatico = [
    {"id": 705, "nome": "Trevo", "drop": 70},
    {"id": 949, "nome": "Pluma", "drop": 30},
    {"id": 2262, "nome": "Nariz de Palhaço", "drop": 0.04},
    {"id": 1102, "nome": "Espada [4]", "drop": 1},
    {"id": 601, "nome": "Asa de Mosca", "drop": 5},
    {"id": 515, "nome": "Cenoura", "drop": 30},
    {"id": 622, "nome": "Cenoura Arco-Íris", "drop": 0.2},
    {"id": 4006, "nome": "Carta Lunático", "drop": 0.2}
]

# Função para simular o drop de um item com base na taxa de drop
def simular_drop_lunatico():
    drops = []  # Lista para armazenar os itens dropados dessa tentativa

    # Verifica cada item individualmente com base na sua taxa de drop
    for item in itens_lunatico:
        chance = random.uniform(0, 100)  # Gera um número aleatório entre 0 e 100
        if chance <= item["drop"]:  # Se a chance for menor ou igual à taxa de drop, o item é dropado
            drops.append(item["nome"])  # Adiciona o item à lista de drops

    return drops  # Retorna a lista com os itens que foram dropados

# Função para simular matar N Lunáticos e coletar os itens
def matar_lunaticos(quantidade):
    itens_dropados = {}  # Dicionário para armazenar os itens e quantidades

    # Simula matar 'quantidade' Lunáticos
    for _ in range(quantidade):
        itens = simular_drop_lunatico()  # Obtém os itens dropados nessa tentativa
        for item in itens:
            if item in itens_dropados:
                itens_dropados[item] += 1  # Se o item já foi dropado, incrementa a quantidade
            else:
                itens_dropados[item] = 1  # Se o item ainda não foi dropado, adiciona no dicionário com quantidade 1

    return itens_dropados  # Retorna o dicionário com todos os itens dropados e suas quantidades

# Programa principal
if __name__ == "__main__":
    # Entrada do usuário: quantos Lunáticos ele quer matar
    vezes = int(input("How many Lunatics do you want to kill? "))

    # Simula matar os Lunáticos e armazenar os drops
    resultado = matar_lunaticos(vezes)

    # Exibe os itens que foram dropados e suas quantidades
    if resultado:
        print("\nYou have obtained the following items:")
        for item, quantidade in resultado.items():
            print(f"{item}: {quantidade}x")
    else:
        print("\nVocê não conseguiu nenhum item.")
