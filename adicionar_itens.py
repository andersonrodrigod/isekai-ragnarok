import json
import os

def ler_inventario(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        return []  # Retorna uma lista vazia se o arquivo não existir

    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data.get("capitulos", [])  # Retorna a lista de capítulos

def atualizar_inventario(capitulos, novos_itens, novo_capitulo):
    # Cria um novo dicionário para os itens do novo capítulo
    itens_novo_capitulo = {}

    # Atualiza os itens do Capítulo 6
    for capitulo in capitulos:
        if capitulo['capitulo'] == 6:
            for item, quantidade in novos_itens.items():
                if item in capitulo['itens']:
                    capitulo['itens'][item] += quantidade  # Soma as quantidades
                else:
                    capitulo['itens'][item] = quantidade  # Adiciona o novo item
            itens_novo_capitulo.update(capitulo['itens'])  # Atualiza os itens do Capítulo 6
            break  # Sai do loop após atualizar o Capítulo 6

    # Adiciona os itens do novo capítulo (Capítulo 7)
    capitulos.append({
        "capitulo": novo_capitulo,
        "itens": itens_novo_capitulo
    })
    
    return capitulos

def salvar_inventario(caminho_arquivo, capitulos):
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        json.dump({"capitulos": capitulos}, file, indent=4)  # Escreve o dicionário no formato JSON

def main():
    caminho_arquivo = './historia/inventario/itens.json'  # Altere para o caminho do seu arquivo JSON
    capitulos = ler_inventario(caminho_arquivo)

    # Novos itens a serem adicionados ou atualizados no Capítulo 6
    novos_itens = {
        'Felpa': 1,
        'Trevo': 8,
        'Jelopy': 1,
        'Erva Verde': 1,
        'Asa de Mosca': 3
    }

    # Atualiza o inventário e adiciona o Capítulo 7
    capitulos = atualizar_inventario(capitulos, novos_itens, 7)
    # Salva o inventário atualizado
    salvar_inventario(caminho_arquivo, capitulos)

    print("Inventário atualizado com sucesso!")

if __name__ == "__main__":
    main()
