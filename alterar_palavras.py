import re

def alterar_palavra_no_txt(caminho_arquivo):
    # Abrir o arquivo em modo leitura
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    # Substituir "status board" por "status plate"
    conteudo_alterado = conteudo.replace("status board", "status plate")
    
    # Substituir "guesthouse" por "inn"
    conteudo_alterado = conteudo_alterado.replace("guesthouse", "inn")
    
    # Substituir "guesthouses" por "inns"
    conteudo_alterado = conteudo_alterado.replace("guesthouses", "inns")
    
    # Substituir "zeny" por "Zeny"
    conteudo_alterado = conteudo_alterado.replace("zeny", "Zeny")

    # Dividir o conteúdo em parágrafos
    parágrafos = conteudo_alterado.split('\n\n')

    # Função para verificar se o parágrafo já está numerado
    def já_numerado(parágrafo):
        # Verifica se o parágrafo já começa com um número seguido de ponto, ignorando aspas
        return bool(re.match(r'^\d+\.', parágrafo.strip()))

    # Numerar os parágrafos não numerados
    parágrafos_numerados = [
        f"{i+1}. {parágrafo.strip()}" if not já_numerado(parágrafo) else parágrafo.strip()
        for i, parágrafo in enumerate(parágrafos)
    ]

    # Reunir os parágrafos numerados em um único texto
    conteudo_final = '\n\n'.join(parágrafos_numerados)

    # Reescrever o arquivo com o conteúdo alterado e numerado
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        file.write(conteudo_final)

    print("Alterações realizadas com sucesso!")

# Caminho para o arquivo .txt
caminho_do_arquivo = "capítulo_5.txt"
alterar_palavra_no_txt(caminho_do_arquivo)
