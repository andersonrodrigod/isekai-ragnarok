import os
import re

# Função para contar a frequência da palavra em um arquivo e extrair os parágrafos onde aparece
def contar_ocorrencias_palavra(arquivo, palavra):
    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read().lower()  # Converter para minúsculas para garantir contagem sem diferenciar maiúsculas/minúsculas
    
    # Encontrar todos os parágrafos numerados
    paragrafo_pattern = re.compile(r'(\d+\..*?)(?=\n\d+\.|\n|$)', re.DOTALL)
    parágrafos = paragrafo_pattern.findall(conteudo)
    
    resultados_parágrafos = []
    palavra_lower = palavra.lower()
    
    # Verificar em quais parágrafos a palavra aparece
    for parágrafo in parágrafos:
        if palavra_lower in parágrafo:
            resultados_parágrafos.append(parágrafo.strip())
    
    return len(resultados_parágrafos), resultados_parágrafos

# Função para pesquisar a palavra em todos os arquivos .txt em uma pasta
def pesquisar_palavra_na_pasta(pasta, palavra):
    resultados = []
    
    # Percorrer todos os arquivos na pasta
    for arquivo_nome in os.listdir(pasta):
        if arquivo_nome.endswith('.txt'):  # Verificar se é um arquivo .txt
            caminho_arquivo = os.path.join(pasta, arquivo_nome)
            ocorrencias, parágrafos = contar_ocorrencias_palavra(caminho_arquivo, palavra)
            if ocorrencias > 0:
                resultados.append((arquivo_nome, ocorrencias, parágrafos))
    
    # Ordenar os arquivos pela frequência de ocorrência da palavra
    resultados.sort(key=lambda x: x[1], reverse=True)
    
    return resultados

# Caminho da pasta onde estão os arquivos .txt
pasta_arquivos = './capitulos_pt'

# Palavra a ser pesquisada
palavra_procurada = 'Cristal'

# Caminho da pasta de saída
pasta_pesquisa = 'pesquisar'

# Criar a pasta de pesquisa, se não existir
if not os.path.exists(pasta_pesquisa):
    os.makedirs(pasta_pesquisa)

# Chamar a função para pesquisar a palavra em todos os arquivos da pasta
resultados = pesquisar_palavra_na_pasta(pasta_arquivos, palavra_procurada)

# Nome do arquivo de saída baseado na palavra pesquisada
arquivo_saida = os.path.join(pasta_pesquisa, f'{palavra_procurada}.txt')

# Exibir os resultados e salvar os parágrafos em um arquivo
with open(arquivo_saida, 'w', encoding='utf-8') as f_out:
    f_out.write(f"Resultados da pesquisa pela palavra '{palavra_procurada}':\n\n")
    
    for arquivo, ocorrencias, parágrafos in resultados:
        f_out.write(f"Arquivo: {arquivo} | Ocorrências: {ocorrencias}\n")
        f_out.write("Parágrafos com a palavra:\n")
        for parágrafo in parágrafos:
            f_out.write(f"  - {parágrafo}\n")
        
        # Adicionar uma linha em branco entre arquivos
        f_out.write("\n")

# Exibir os nomes dos arquivos no terminal
print(f"Palavra '{palavra_procurada}' encontrada nos seguintes arquivos:")
for arquivo, _, _ in resultados:
    print(f"- {arquivo}")

print(f"\nOs resultados foram salvos em: {arquivo_saida}")
