import random

# Definição dos itens que o Fabre pode dropar e suas respectivas taxas de drop
itens_fabre = [
    {"id": 914, "nome": "Felpa", "drop": 70},
    {"id": 949, "nome": "Pluma", "drop": 10},
    {"id": 1502, "nome": "Clava [4]", "drop": 0.8},
    {"id": 601, "nome": "Asa de Mosca", "drop": 5},
    {"id": 511, "nome": "Erva Verde", "drop": 30},
    {"id": 705, "nome": "Trevo", "drop": 10},
    {"id": 1501, "nome": "Clava [3]", "drop": 2},
    {"id": 4002, "nome": "Carta Fabre", "drop": 0.2}
]

# Função para simular o drop de um item com base na taxa de drop
def simular_drop_fabre():
    drops = []  # Lista para armazenar os itens dropados nessa tentativa

    # Verifica cada item individualmente
    for item in itens_fabre:
        # Gera um número aleatório entre 0 e 100 para determinar se o item será dropado
        chance = random.uniform(0, 100)
        if chance <= item["drop"]:
            drops.append(item["nome"])

    return drops

# Função para simular matar N Fabres e coletar os itens
def matar_fabres(quantidade):
    itens_dropados = {}
    
    # Simula a morte de 'quantidade' Fabres
    for _ in range(quantidade):
        items = simular_drop_fabre()  # Obtém a lista de itens dropados nessa tentativa
        for item in items:
            if item in itens_dropados:
                itens_dropados[item] += 1
            else:
                itens_dropados[item] = 1
                
    return itens_dropados

# Programa principal
if __name__ == "__main__":
    # Entrada do usuário: quantos Fabres ele quer matar
    vezes = int(input("How many Fabres do you want to kill? "))

    # Simula matar os Fabres e armazenar os drops
    resultado = matar_fabres(vezes)

    # Exibe os itens que foram dropados e suas quantidades
    if resultado:
        print("\nYou have obtained the following items:")
        for item, quantidade in resultado.items():
            print(f"{item}: {quantidade}x")
    else:
        print("\nVocê não conseguiu nenhum item.")
