import random

# Definição dos itens que o Vocal pode dropar e suas respectivas taxas de drop
itens_vocal = [
    {"id": 2247, "nome_pt": "Chapéu Romântico", "nome_en": "Romantic Hat", "drop": 0.25},
    {"id": 940, "nome_pt": "Perna de Gafanhoto", "nome_en": "Grasshopper's Leg", "drop": 40.0},
    {"id": 721, "nome_pt": "Esmeralda", "nome_en": "Emerald", "drop": 5.0},
    {"id": 752, "nome_pt": "Boneco de Rocker", "nome_en": "Rocker Doll", "drop": 7.5},
    {"id": 2420, "nome_pt": "Reencarnação do Anjo [1]", "nome_en": "Angel's Rebirth [1]", "drop": 5.0},
    {"id": 7938, "nome_pt": "Partículas de Luz", "nome_en": "Light Particles", "drop": 2.5},
    {"id": 1917, "nome_pt": "Violão da Brisa Gentil", "nome_en": "Gentle Breeze Guitar", "drop": 0.05},
    {"id": 4211, "nome_pt": "Carta Vocal", "nome_en": "Vocal Card", "drop": 0.01}
]

# Função para simular o drop de um item com base na taxa de drop
def simular_drop_vocal():
    drops = []  # Lista para armazenar os itens dropados nessa tentativa

    # Verifica cada item individualmente
    for item in itens_vocal:
        # Gera um número aleatório entre 0 e 100 para determinar se o item será dropado
        chance = random.uniform(0, 100)
        if chance <= item["drop"]:
            drops.append((item["nome_pt"], item["nome_en"]))

    return drops

# Função para simular matar N Vocais e coletar os itens
def matar_vocais(quantidade):
    itens_dropados = {}
    
    # Simula a morte de 'quantidade' Vocais
    for _ in range(quantidade):
        items = simular_drop_vocal()  # Obtém a lista de itens dropados nessa tentativa
        for item_pt, item_en in items:
            if item_pt in itens_dropados:
                itens_dropados[item_pt]["quantidade"] += 1
            else:
                itens_dropados[item_pt] = {"quantidade": 1, "nome_en": item_en}
                
    return itens_dropados

# Programa principal
if __name__ == "__main__":
    # Entrada do usuário: quantos Vocais ele quer matar
    vezes = int(input("How many Vocals do you want to kill? "))

    # Simula matar os Vocais e armazenar os drops
    resultado = matar_vocais(vezes)

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
