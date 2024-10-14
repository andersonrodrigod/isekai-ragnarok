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

def adicionar_capitulo(dados, capitulo, novos_atributos):
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

        # Adiciona um novo capítulo com os atributos totais
        novo_capitulo = {
            "capitulo": capitulo,
            "atributos": atributos_totais
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
            }
        }
        dados['capitulos'].append(novo_capitulo)

def main():
    arquivo = './historia/inventario/atributos.json'
    dados = carregar_dados(arquivo)

    # Exemplo de novos atributos a adicionar no capítulo 8
    novos_atributos = {
        "STR": 0,
        "AGI": 1,
        "VIT": 0,
        "INT": 0,
        "DEX": 0,
        "LUK": 0
    }

    capitulo_atual = 9
    adicionar_capitulo(dados, capitulo_atual, novos_atributos)
    salvar_dados(arquivo, dados)

    print("Atributos atualizados com sucesso!")
    
if __name__ == "__main__":
    main()
