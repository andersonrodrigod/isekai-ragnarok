import random

# Definição dos itens que o Bebê Selvagem pode dropar e suas respectivas taxas de drop
itens_bebe_selvagem = [
    {"id": 919, "nome_pt": "Couro de Animal", "nome_en": "Animal Hide", "drop": 45.0},
    {"id": 1302, "nome_pt": "Machado [4]", "nome_en": "Axe [4]", "drop": 0.5},
    {"id": 517, "nome_pt": "Carne", "nome_en": "Meat", "drop": 2.5},
    {"id": 601, "nome_pt": "Asa de Mosca", "nome_en": "Fly Wing", "drop": 5.0},
    {"id": 949, "nome_pt": "Pluma", "nome_en": "Feather", "drop": 4.25},
    {"id": 1010, "nome_pt": "Fracon", "nome_en": "Fracon", "drop": 0.4},
    {"id": 627, "nome_pt": "Leite Doce", "nome_en": "Sweet Milk", "drop": 0.2},
    {"id": 4017, "nome_pt": "Carta Bebê Selvagem", "nome_en": "Savage Babe Card", "drop": 0.01}
]

# Função para simular o drop de um item com base na taxa de drop
def simular_drop_bebe_selvagem():
    drops = []  # Lista para armazenar os itens dropados nessa tentativa

    # Verifica cada item individualmente
    for item in itens_bebe_selvagem:
        # Gera um número aleatório entre 0 e 100 para determinar se o item será dropado
        chance = random.uniform(0, 100)
        if chance <= item["drop"]:
            drops.append((item["nome_pt"], item["nome_en"]))

    return drops

# Função para simular matar N Bebês Selvagens e coletar os itens
def matar_bebes_selvagens(quantidade):
    itens_dropados = {}
    
    # Simula a morte de 'quantidade' Bebês Selvagens
    for _ in range(quantidade):
        items = simular_drop_bebe_selvagem()  # Obtém a lista de itens dropados nessa tentativa
        for item_pt, item_en in items:
            if item_pt in itens_dropados:
                itens_dropados[item_pt]["quantidade"] += 1
            else:
                itens_dropados[item_pt] = {"quantidade": 1, "nome_en": item_en}
                
    return itens_dropados

# Programa principal
if __name__ == "__main__":
    # Entrada do usuário: quantos Bebês Selvagens ele quer matar
    vezes = int(input("How many Savage Babies do you want to kill? "))

    # Simula matar os Bebês Selvagens e armazenar os drops
    resultado = matar_bebes_selvagens(vezes)

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
