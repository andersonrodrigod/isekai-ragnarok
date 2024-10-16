import random

# Definição dos itens que o Rocker pode dropar e suas respectivas taxas de drop
itens_rocker = [
    {"id": 940, "nome_pt": "Perna de Gafanhoto", "nome_en": "Grasshopper's Leg", "drop": 80.0},
    {"id": 1916, "nome_pt": "Violão da Mãe Terra", "nome_en": "Mother Earth's Guitar", "drop": 0.05},
    {"id": 2298, "nome_pt": "Antenas Verdes", "nome_en": "Green Antennas", "drop": 0.05},
    {"id": 1402, "nome_pt": "Azagaia [4]", "nome_en": "Javelin [4]", "drop": 0.8},
    {"id": 601, "nome_pt": "Asa de Mosca", "nome_en": "Fly Wing", "drop": 5.0},
    {"id": 752, "nome_pt": "Boneco de Rocker", "nome_en": "Rocker Doll", "drop": 0.1},
    {"id": 703, "nome_pt": "Hinalle", "nome_en": "Hinalle", "drop": 0.1},
    {"id": 4021, "nome_pt": "Carta Rocker", "nome_en": "Rocker Card", "drop": 0.01}
]

# Função para simular o drop de um item com base na taxa de drop
def simular_drop_rocker():
    drops = []  # Lista para armazenar os itens dropados nessa tentativa

    # Verifica cada item individualmente
    for item in itens_rocker:
        # Gera um número aleatório entre 0 e 100 para determinar se o item será dropado
        chance = random.uniform(0, 100)
        if chance <= item["drop"]:
            drops.append((item["nome_pt"], item["nome_en"]))

    return drops

# Função para simular matar N Rockers e coletar os itens
def matar_rockers(quantidade):
    itens_dropados = {}
    
    # Simula a morte de 'quantidade' Rockers
    for _ in range(quantidade):
        items = simular_drop_rocker()  # Obtém a lista de itens dropados nessa tentativa
        for item_pt, item_en in items:
            if item_pt in itens_dropados:
                itens_dropados[item_pt]["quantidade"] += 1
            else:
                itens_dropados[item_pt] = {"quantidade": 1, "nome_en": item_en}
                
    return itens_dropados

# Programa principal
if __name__ == "__main__":
    # Entrada do usuário: quantos Rockers ele quer matar
    vezes = int(input("How many Rockers do you want to kill? "))

    # Simula matar os Rockers e armazenar os drops
    resultado = matar_rockers(vezes)

    # Exibe os itens que foram dropados em inglês
    if resultado:
        print("\nYou have obtained the following items (English):")
        for item_pt, dados in resultado.items():
            print(f"{dados['nome_en']}: {dados['quantidade']}x")

        # Exibe os itens que foram dropados em português
        print("\nVocê obteve os seguintes itens (Português):")
        for item_pt, dados in resultado.items():
            print(f"{item_pt}: {dados['quantidade']}x")
    else:
        print("\nVocê não conseguiu nenhum item.")
