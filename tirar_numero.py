import re

def remover_numeracao(caminho_arquivo):
    # Abrir o arquivo em modo leitura
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    # Expressão regular para remover a numeração e o espaço subsequente
    conteudo_alterado = re.sub(r'^\d+\.\s*', '', conteudo, flags=re.M)

    # Gravar as alterações no arquivo
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        file.write(conteudo_alterado)

    print("Numeração removida com sucesso!")


caminho_do_arquivo = "./capitulos_pt/12.txt"
remover_numeracao(caminho_do_arquivo)