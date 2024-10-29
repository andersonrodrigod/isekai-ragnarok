from googletrans import Translator

# Função para traduzir o texto
def traduzir_texto(texto, src_lang='en', dest_lang='pt'):
    tradutor = Translator()
    traducao = tradutor.translate(texto, src=src_lang, dest=dest_lang)
    return traducao.text

# Ler o arquivo em inglês
with open('./capitulos_en/10.txt', 'r', encoding='utf-8') as arquivo:
    conteudo_ingles = arquivo.read()

# Traduzir o conteúdo para português
conteudo_traduzido = traduzir_texto(conteudo_ingles)

# Escrever o conteúdo traduzido em um novo arquivo
with open('./capitulos_pt/10.txt', 'w', encoding='utf-8') as arquivo_traduzido:
    arquivo_traduzido.write(conteudo_traduzido)

print("Tradução concluída e salva em './capitulos_pt/15.txt'.")