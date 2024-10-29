import json
import os

def carregar_dados(arquivo):
    """Carrega os dados do arquivo JSON, ou cria uma nova estrutura se o arquivo não existir."""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    else:
        return {"capitulos": []}

def salvar_dados(arquivo, dados):
    """Salva os dados no arquivo JSON."""
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def calcular_hp(nivel, vit):
    """Calcula o HP com base no nível e VIT."""
    hp_inicial = 100
    hp_por_nivel = 15
    hp_total = hp_inicial + (nivel * hp_por_nivel) * (1 + (vit * 0.01))  # 1% a mais para cada ponto de VIT
    return int(hp_total)

def calcular_mp(nivel, int_):
    """Calcula o MP com base no nível e INT."""
    mp_inicial = 50
    mp_total = mp_inicial + int_ + (nivel * 3)
    return int(mp_total)

def adicionar_capitulo(dados, capitulo, novos_atributos):
    """Adiciona um novo capítulo com os novos dados de atributos e status."""
    # Cálculo de HP e MP
    hp = calcular_hp(novos_atributos.get('nivel', 1), novos_atributos.get('VIT', 0))
    mp = calcular_mp(novos_atributos.get('nivel', 1), novos_atributos.get('INT', 0))

    # Adiciona um novo capítulo com os atributos e status
    novo_capitulo = {
        "capitulo": capitulo,
        "atributos": {
            "STR": novos_atributos.get("STR", 0),
            "AGI": novos_atributos.get("AGI", 0),
            "VIT": novos_atributos.get("VIT", 0),
            "INT": novos_atributos.get("INT", 0),
            "DEX": novos_atributos.get("DEX", 0),
            "LUK": novos_atributos.get("LUK", 0)
        },
        "status_geral": {
            "HP": hp,  # HP calculado corretamente
            "MP": mp,  # MP calculado corretamente
            "nivel": novos_atributos.get("nivel", 1),
            "nivel_classe": novos_atributos.get("nivel_classe", 1)
        }
    }
    
    dados['capitulos'].append(novo_capitulo)

def main():
    arquivo = './historia/atributos/atributos.json'
    dados = carregar_dados(arquivo)

    # Exemplo de novos atributos a adicionar no capítulo 9
    novos_atributos = {
        "STR": 26,
        "AGI": 12,
        "VIT": 12,
        "INT": 0,  
        "DEX": 10,
        "LUK": 6,
        "nivel": 18,
        "nivel_classe": 12
    }

    capitulo_atual = 14
    adicionar_capitulo(dados, capitulo_atual, novos_atributos)
    salvar_dados(arquivo, dados)

    print("Atributos e status atualizados com sucesso!")
    
if __name__ == "__main__":
    main()
