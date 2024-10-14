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

def adicionar_capitulo(dados, capitulo, novos_atributos, novos_status):
    """Adiciona um novo capítulo com a soma dos atributos do último capítulo e os novos dados."""
    if dados['capitulos']:
        ultimo_capitulo = dados['capitulos'][-1]

        # Criar dicionário para armazenar a soma dos atributos
        atributos_totais = ultimo_capitulo.get('atributos', {
            "STR": 0,
            "AGI": 0,
            "VIT": 0,
            "INT": 0,
            "DEX": 0,
            "LUK": 0
        }).copy()

        # Soma os novos atributos ao total
        for atributo, pontos in novos_atributos.items():
            if atributo in atributos_totais:
                atributos_totais[atributo] += pontos
            else:
                atributos_totais[atributo] = pontos

        # Atualiza o status geral (HP, MP, nível, etc.)
        status_geral = ultimo_capitulo.get('status_geral', {
            "HP": 0,
            "MP": 0,
            "nivel": 1,
            "nivel_classe": 1
        }).copy()

        for status, valor in novos_status.items():
            status_geral[status] = valor

        # Adiciona um novo capítulo com os atributos e status gerais
        novo_capitulo = {
            "capitulo": capitulo,
            "atributos": atributos_totais,
            "status_geral": status_geral
        }
        dados['capitulos'].append(novo_capitulo)
    else:
        # Primeiro capítulo
        novo_capitulo = {
            "capitulo": capitulo,
            "atributos": {
                "STR": novos_atributos.get("STR", 0),
                "AGI": novos_atributos.get("AGI", 0),
                "VIT": novos_atributos.get("VIT", 0),
                "INT": novos_atributos.get("INT", 0),
                "DEX": novos_atributos.get("DEX", 0),
                "LUK": novos_atributos.get("LUK", 0)
            },
            "status_geral": {
                "HP": novos_status.get("HP", 100),
                "MP": novos_status.get("MP", 50),
                "nivel": novos_status.get("nivel", 1),
                "nivel_classe": novos_status.get("nivel_classe", 1)
            }
        }
        dados['capitulos'].append(novo_capitulo)

def main():
    arquivo = './historia/inventario/atributos.json'
    dados = carregar_dados(arquivo)

    # Exemplo de novos atributos a adicionar no capítulo 9
    novos_atributos = {
        "STR": 0,
        "AGI": 1,
        "VIT": 0,
        "INT": 0,
        "DEX": 0,
        "LUK": 0
    }

    # Exemplo de novos status gerais a adicionar no capítulo 9
    novos_status = {
        "HP": 120,
        "MP": 60,
        "nivel": 5,
        "nivel_classe": 2
    }

    capitulo_atual = 9
    adicionar_capitulo(dados, capitulo_atual, novos_atributos, novos_status)
    salvar_dados(arquivo, dados)

    print("Atributos e status atualizados com sucesso!")
    
if __name__ == "__main__":
    main()
