import json
import os

# Definindo a estrutura de uma habilidade
class Habilidade:
    def __init__(self, nome, tipo, percentual_aumento, descricao):
        self.nome = nome
        self.tipo = tipo  # 'ATQ' ou 'MATQ'
        self.percentual_aumento = percentual_aumento
        self.descricao = descricao
        self.efeitos = {}

    def adicionar_efeito(self, nome_efeito, chance_acerto, percentual_dano):
        self.efeitos[nome_efeito] = {
            "chance_acerto": chance_acerto,
            "percentual_dano": percentual_dano
        }

    def to_dict(self):
        return {
            "nome": self.nome,
            "tipo": self.tipo,
            "percentual_aumento": self.percentual_aumento,
            "descricao": self.descricao,
            "efeitos": self.efeitos
        }

# Função para salvar habilidades em um arquivo JSON
def salvar_habilidades(habilidades, caminho='./historia/habilidades/skills.json'):
    if not os.path.exists(os.path.dirname(caminho)):
        os.makedirs(os.path.dirname(caminho))
    
    with open(caminho, 'w') as f:
        json.dump([habilidade.to_dict() for habilidade in habilidades], f, indent=4)

# Função principal
def main():
    habilidades = []
    
    while True:
        nome = input("Digite o nome da habilidade: ")
        tipo = input("Digite o tipo da habilidade (ATQ ou MATQ): ").upper()
        percentual_aumento = float(input("Digite o percentual de aumento: "))
        descricao = input("Digite a descrição da habilidade: ")
        
        habilidade = Habilidade(nome, tipo, percentual_aumento, descricao)
        
        while True:
            nome_efeito = input("Digite o nome do efeito (ou 'sair' para finalizar): ")
            if nome_efeito.lower() == 'sair':
                break
            
            chance_acerto = float(input("Digite a chance de acerto do efeito (0-100): "))
            percentual_dano = float(input("Digite o percentual de dano adicional se o efeito acertar: "))
            
            habilidade.adicionar_efeito(nome_efeito, chance_acerto, percentual_dano)
        
        habilidades.append(habilidade)
        
        continuar = input("Deseja adicionar outra habilidade? (s/n): ").lower()
        if continuar != 's':
            break

    salvar_habilidades(habilidades)
    print("Habilidades salvas com sucesso!")

if __name__ == "__main__":
    main()
