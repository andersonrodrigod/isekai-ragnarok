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

    # Reescrever o arquivo com o conteúdo alterado
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        file.write(conteudo_alterado)

    print("Alterações realizadas com sucesso!")

# Caminho para o arquivo .txt
caminho_do_arquivo = "chapter_4"
alterar_palavra_no_txt(caminho_do_arquivo)
