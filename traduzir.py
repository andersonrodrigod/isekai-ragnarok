from googletrans import Translator

# Função para traduzir o texto
def traduzir_texto(texto, src_lang='pt', dest_lang='en'):
    tradutor = Translator()
    traducao = tradutor.translate(texto, src=src_lang, dest=dest_lang)
    return traducao.text

# Ler o arquivo em português
with open('./capitulos_pt/13.txt', 'r', encoding='utf-8') as arquivo:
    conteudo_portugues = arquivo.read()

# Traduzir o conteúdo para inglês
conteudo_traduzido = traduzir_texto(conteudo_portugues)

# Escrever o conteúdo traduzido em um novo arquivo
with open('./capitulos_en/13.txt', 'w', encoding='utf-8') as arquivo_traduzido:
    arquivo_traduzido.write(conteudo_traduzido)



print("Tradução concluída e salva em 'arquivo_ingles.txt'.")