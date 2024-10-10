import os

# Função para contar a frequência da palavra em um arquivo
def contar_ocorrencias_palavra(arquivo, palavra):
    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read().lower()  # Converter para minúsculas para garantir contagem sem diferenciar maiúsculas/minúsculas
    return conteudo.count(palavra.lower())  # Contar as ocorrências da palavra

# Função para pesquisar a palavra em todos os arquivos .txt em uma pasta
def pesquisar_palavra_na_pasta(pasta, palavra):
    resultados = []
    
    # Percorrer todos os arquivos na pasta
    for arquivo_nome in os.listdir(pasta):
        if arquivo_nome.endswith('.txt'):  # Verificar se é um arquivo .txt
            caminho_arquivo = os.path.join(pasta, arquivo_nome)
            ocorrencias = contar_ocorrencias_palavra(caminho_arquivo, palavra)
            if ocorrencias > 0:
                resultados.append((arquivo_nome, ocorrencias))
    
    # Ordenar os arquivos pela frequência de ocorrência da palavra
    resultados.sort(key=lambda x: x[1], reverse=True)
    
    return resultados

# Caminho da pasta onde estão os arquivos .txt
pasta_arquivos = './capitulos_pt'

# Palavra a ser pesquisada
palavra_procurada = 'Rox'

# Chamar a função para pesquisar a palavra em todos os arquivos da pasta
resultados = pesquisar_palavra_na_pasta(pasta_arquivos, palavra_procurada)

# Exibir os resultados
print(f"Resultados da pesquisa pela palavra '{palavra_procurada}':")
for arquivo, ocorrencias in resultados:
    print(f"Arquivo: {arquivo} | Ocorrências: {ocorrencias}")
