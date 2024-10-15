import json
import os

def carregar_dados(arquivo):
    """Carrega os dados do arquivo JSON ou cria uma nova estrutura se o arquivo não existir."""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    else:
        return {"capitulos": []}

def salvar_dados(arquivo, dados):
    """Salva os dados no arquivo JSON."""
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def calcular_dia_atual(dados):
    """Calcula o dia atual com base nos capítulos anteriores."""
    if not dados['capitulos']:
        return 1  # Se não houver capítulos, começamos no dia 1
    ultimo_capitulo = dados['capitulos'][-1]
    return ultimo_capitulo['dia_atual'] + ultimo_capitulo['dias_passados']

def adicionar_capitulo(arquivo, dias_passados):
    """Adiciona um novo capítulo com os dias passados e calcula o dia atual."""
    dados = carregar_dados(arquivo)

    # Obtém o número do próximo capítulo e o dia atual
    if dados['capitulos']:
        ultimo_capitulo = dados['capitulos'][-1]
        novo_capitulo_num = ultimo_capitulo['capitulo'] + 1
    else:
        novo_capitulo_num = 1

    dia_atual = calcular_dia_atual(dados)

    # Cria o novo capítulo com o número, dias passados e o dia atual
    novo_capitulo = {
        "capitulo": novo_capitulo_num,
        "dias_passados": dias_passados,
        "dia_atual": dia_atual
    }

    # Adiciona o novo capítulo aos dados e salva
    dados['capitulos'].append(novo_capitulo)
    salvar_dados(arquivo, dados)

    print(f"Capítulo {novo_capitulo_num} adicionado com {dias_passados} dias passados, no dia atual {dia_atual}.")

def calcular_total_dias(arquivo):
    """Calcula o total de dias passados em todos os capítulos."""
    dados = carregar_dados(arquivo)
    total_dias = sum(capitulo['dias_passados'] for capitulo in dados['capitulos'])
    return total_dias

def main():
    arquivo_json = './historia/dias.json'
    
    # Exemplo de adicionar dias para um novo capítulo
    dias_passados = int(input("Quantos dias passaram neste capítulo? "))
    
    adicionar_capitulo(arquivo_json, dias_passados)

    # Calcula o total de dias passados
    total_dias = calcular_total_dias(arquivo_json)
    print(f"Total de dias passados até o momento: {total_dias} dias.")

if __name__ == "__main__":
    main()
