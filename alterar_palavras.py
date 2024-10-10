import re

def alterar_palavra_no_txt(caminho_arquivo):
    # Abrir o arquivo em modo leitura
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    # Substituir todas as variações de "status board" por "Status Plate"
    conteudo_alterado = re.sub(r'(?i)status\s*board', 'Status Plate', conteudo)

    # Substituir "guesthouse" por "inn"
    conteudo_alterado = conteudo_alterado.replace("guesthouse", "inn")
    
    # Substituir "guesthouses" por "inns"
    conteudo_alterado = conteudo_alterado.replace("guesthouses", "inns")
    
    # Substituir "zeny" por "Zeny"
    conteudo_alterado = conteudo_alterado.replace("zeny", "Zeny")

    # Numerar linhas que contêm espaçamento pela tecla Enter
    linhas = conteudo_alterado.split('\n')
    linhas_numeradas = []
    numero = 1
    for linha in linhas:
        if linha.strip() != '' and not re.match(r'^\d+\.', linha.strip()):  # Verifica se a linha não está numerada
            linhas_numeradas.append(f"{numero}. {linha.strip()}")
            numero += 1
        else:
            linhas_numeradas.append(linha.strip())

    # Reunir todas as linhas alteradas em uma string final
    conteudo_final = '\n'.join(linhas_numeradas)

    # Gravar as alterações no arquivo
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        file.write(conteudo_final)

    print("Alterações realizadas com sucesso!")

# Caminho para o arquivo .txt
caminho_do_arquivo = "./capitulos_pt/5.txt"
alterar_palavra_no_txt(caminho_do_arquivo)