import json

# Caminho do arquivo JSON
caminho_arquivo = './historia/equipamentos/equipados.json'

# Função para verificar se um valor é válido (não 0 ou string vazia)
def valor_valido(valor):
    return valor != 0 and valor != ""

# Função para exibir informações dos equipamentos
def exibir_equipamentos():
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        
        # Percorre a lista de equipamentos
        for equipamento in dados['equipamentos']:
            nome = equipamento['nome']
            atributos = equipamento['atributos']
            atributos_derivados = equipamento['atributos_derivados']
            descricao = atributos_derivados.get('descricao', 'Sem descrição')
            
            # Exibe o nome do equipamento
            print(f"\n{nome}")

            # Filtra e exibe os atributos que são válidos, excluindo a descrição
            atributos_exibidos = [
                f"{chave}: {valor}" 
                for chave, valor in {**atributos, **atributos_derivados}.items() 
                if valor_valido(valor) and chave != 'descricao'
            ]

            # Exibe os atributos se houver algum válido, sem colchetes
            if atributos_exibidos:
                print(", ".join(atributos_exibidos))  # Use join para evitar colchetes
            
            # Exibe a descrição do item
            print(f"Descrição: {descricao}")

            # Espera o usuário pressionar Enter para continuar
            input("\nPressione Enter para continuar para o próximo item...")

# Executa a função
exibir_equipamentos()
