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

def adicionar_capitulo(dados, capitulo, novos_itens, novos_equipamentos):
    """Adiciona um novo capítulo com a soma dos itens e equipamentos do último capítulo e novos dados."""
    if dados['capitulos']:
        ultimo_capitulo = dados['capitulos'][-1]

        # Criar um dicionário para armazenar a soma dos itens
        itens_totais = ultimo_capitulo.get('itens', {}).copy()
        equipamentos_totais = ultimo_capitulo.get('equipamentos', {}).copy()

        # Soma os novos itens ao total
        for item, quantidade in novos_itens.items():
            if item in itens_totais:
                itens_totais[item] += quantidade
            else:
                itens_totais[item] = quantidade

        # Soma os novos equipamentos ao total
        for equipamento, quantidade in novos_equipamentos.items():
            if equipamento in equipamentos_totais:
                equipamentos_totais[equipamento] += quantidade
            else:
                equipamentos_totais[equipamento] = quantidade

        # Adiciona um novo capítulo com os itens e equipamentos totais
        novo_capitulo = {
            "capitulo": capitulo,
            "itens": itens_totais,
            "equipamentos": equipamentos_totais
        }
        dados['capitulos'].append(novo_capitulo)
    else:
        # Primeiro capítulo
        novo_capitulo = {
            "capitulo": capitulo,
            "itens": novos_itens,
            "equipamentos": novos_equipamentos
        }
        dados['capitulos'].append(novo_capitulo)

def main():
    arquivo = './historia/inventario/itens.json'
    dados = carregar_dados(arquivo)

    # Exemplo de novos itens e equipamentos a adicionar no capítulo 8
    novos_itens = {
        "Cenoura Arco-Íris": 2,
        
    }

    novos_equipamentos = {
        "Clava [3]": 1,
    }

    capitulo_atual = 8
    adicionar_capitulo(dados, capitulo_atual, novos_itens, novos_equipamentos)
    salvar_dados(arquivo, dados)

    print("Dados atualizados com sucesso!")
    
if __name__ == "__main__":
    main()
