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

    conteudo_alterado = conteudo_alterado.replace("Overprice", "Overcharge")

    conteudo_alterado = conteudo_alterado.replace("Overpricing", "Overcharge")

    conteudo_alterado = conteudo_alterado.replace("mission", "quest")

    conteudo_alterado = conteudo_alterado.replace("profession", "Class")
    

    # Gravar as alterações no arquivo
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        file.write(conteudo_alterado)

    print("Alterações realizadas com sucesso!")

# Caminho para o arquivo .txt
caminho_do_arquivo = "./capitulos_en/6.txt"
alterar_palavra_no_txt(caminho_do_arquivo)


