import json
import os

def carregar_dados(arquivo):
    """Carrega os dados do arquivo JSON, ou cria uma nova estrutura se o arquivo não existir."""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    else:
        return {"capitulos": []}

def salvar_dados(arquivo, dados):
    """Salva os dados no arquivo JSON."""
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def adicionar_capitulo(dados, capitulo, novos_itens):
    """Adiciona um novo capítulo com a soma dos itens do último capítulo e novos itens."""
    if dados['capitulos']:
        ultimo_capitulo = dados['capitulos'][-1]

        # Criar um dicionário para armazenar a soma dos itens
        itens_totais = ultimo_capitulo['itens'].copy()

        # Soma os novos itens ao total
        for item, quantidade in novos_itens.items():
            if item in itens_totais:
                itens_totais[item] += quantidade
            else:
                itens_totais[item] = quantidade

        # Adiciona um novo capítulo com os itens totais
        novo_capitulo = {
            "capitulo": capitulo,
            "itens": itens_totais
        }
        dados['capitulos'].append(novo_capitulo)
    else:
        # Primeiro capítulo
        novo_capitulo = {
            "capitulo": capitulo,
            "itens": novos_itens
        }
        dados['capitulos'].append(novo_capitulo)

def main():
    arquivo = './historia/inventario/itens.json'
    dados = carregar_dados(arquivo)

    # Exemplo de novos itens a adicionar no capítulo 7
    novos_itens = {
        "Flor": 2,
        "Broto": 1,
        "Novo Item": 3
    }

    capitulo_atual = 7
    adicionar_capitulo(dados, capitulo_atual, novos_itens)
    salvar_dados(arquivo, dados)

    print("Dados atualizados com sucesso!")
    
if __name__ == "__main__":
    main()
