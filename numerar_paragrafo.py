import re

def numerar_linhas(caminho_arquivo):
    # Abrir o arquivo em modo leitura
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    # Dividir o conteúdo em linhas
    linhas = conteudo.split('\n')
    linhas_numeradas = []
    
    numero = 1  # Iniciar a numeração
    for linha in linhas:
        if linha.strip() != '':
            # Verificar se a linha já está numerada
            if re.match(r'^\d+\.', linha.strip()):
                # Se já estiver numerada, apenas adicionar a linha como está
                linhas_numeradas.append(linha.strip())
                numero += 1  # Avançar o número
            else:
                # Se não estiver numerada, numerar a linha
                linhas_numeradas.append(f"{numero}. {linha.strip()}")
                numero += 1
        else:
            # Linha em branco, não numerar
            linhas_numeradas.append('')

    # Reunir todas as linhas alteradas em uma string final
    conteudo_final = '\n'.join(linhas_numeradas)

    # Gravar as alterações no arquivo
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        file.write(conteudo_final)

    print("Linhas numeradas com sucesso!")

# Caminho para o arquivo .txt
caminho_do_arquivo = "./capitulos_pt/10.txt"
numerar_linhas(caminho_do_arquivo)