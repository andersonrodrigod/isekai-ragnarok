import string

# Função para contar palavras, caracteres e letras em um arquivo
def contar_elementos_arquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # Contar o número total de caracteres
    num_caracteres = len(conteudo)
    
    # Contar o número total de palavras (considerando espaços como delimitadores)
    palavras = conteudo.split()
    num_palavras = len(palavras)

    # Contar o número de letras (ignorando pontuações e espaços)
    num_letras = sum(c.isalpha() for c in conteudo)

    # Contar a frequência de cada letra
    letra_frequencia = {letra: conteudo.lower().count(letra) for letra in string.ascii_lowercase}

    return num_caracteres, num_palavras, num_letras, letra_frequencia

# Caminho do arquivo
caminho_arquivo = './capitulos_pt/15.txt'

# Chamar a função para contar os elementos
num_caracteres, num_palavras, num_letras, letra_frequencia = contar_elementos_arquivo(caminho_arquivo)

# Exibir resultados
print(f"Número total de caracteres (incluindo espaços e pontuações): {num_caracteres}")
print(f"Número total de palavras: {num_palavras}")
print(f"Número total de letras: {num_letras}")
print("\nFrequência de cada letra:")
