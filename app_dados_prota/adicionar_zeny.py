import json
import os

def carregar_dados(arquivo):
    """Carrega os dados do arquivo JSON, ou cria uma nova estrutura se o arquivo não existir."""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    else:
        # Se o arquivo não existe, cria a estrutura inicial com saldo 0
        return {"capitulos": [{"capitulo": 0, "saldo": 0}]}

def salvar_dados(arquivo, dados):
    """Salva os dados no arquivo JSON."""
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def adicionar_capitulo(dados, ganhos, gastos):
    """Adiciona um novo capítulo com o saldo de zeny atualizado."""
    # Pega o saldo do último capítulo
    ultimo_capitulo = dados['capitulos'][-1]
    saldo_atual = ultimo_capitulo['saldo']

    # Calcula o novo saldo
    novo_saldo = saldo_atual + ganhos - gastos

    # Determina o número do novo capítulo com base no último
    novo_capitulo_numero = ultimo_capitulo['capitulo'] + 1

    # Cria um novo capítulo com o saldo atualizado
    novo_capitulo = {
        "capitulo": novo_capitulo_numero,
        "ganhos": ganhos,
        "gastos": gastos,
        "saldo": novo_saldo
    }

    # Adiciona o novo capítulo à lista de capítulos
    dados['capitulos'].append(novo_capitulo)

def main():
    arquivo = './historia/inventario/zeny.json'
    dados = carregar_dados(arquivo)

    # Exemplo de valores para o novo capítulo
    ganhos = float(input("Digite quanto o personagem ganhou: "))
    gastos = float(input("Digite quanto o personagem gastou: "))

    adicionar_capitulo(dados, ganhos, gastos)
    salvar_dados(arquivo, dados)

    # Pega o último capítulo adicionado e exibe as informações
    ultimo_capitulo = dados['capitulos'][-1]
    print(f"Capítulo {ultimo_capitulo['capitulo']} adicionado com sucesso!")
    print(f"Saldo atualizado: {ultimo_capitulo['saldo']} zeny")

if __name__ == "__main__":
    main()
