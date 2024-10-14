import json
import os

def carregar_dados(arquivo):
    """Carrega os dados do arquivo JSON, ou cria uma nova estrutura se o arquivo não existir."""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    else:
        return {"capitulos": []}

def carregar_ultimo_capitulo(arquivo):
    """Carrega os dados do último capítulo do arquivo JSON."""
    dados = carregar_dados(arquivo)
    if dados['capitulos']:
        return dados['capitulos'][-1]['atributos']
    return {}

def carregar_equipamentos_equipados(arquivo):
    """Carrega os atributos totais do arquivo de equipamentos equipados."""
    dados = carregar_dados(arquivo)
    if dados['capitulos']:
        return dados['capitulos'][-1]['atributos_totais']
    return {}

def carregar_buffs(arquivo):
    """Carrega os buffs do arquivo de buffs."""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f).get('buffs', [])
    return []

def somar_atributos_base(atributos1, atributos2):
    """Soma os atributos base STR, AGI, VIT, INT, DEX, LUK e os efeitos passivo e ativo."""
    atributos_totais = {
        "STR": 0,
        "AGI": 0,
        "VIT": 0,
        "INT": 0,
        "DEX": 0,
        "LUK": 0,
        "efeito_passivo": "",
        "efeito_ativo": ""
    }
    
    # Somar os valores dos dois dicionários de atributos base
    for key in atributos_totais.keys():
        if key in ['efeito_passivo', 'efeito_ativo']:
            # Concatenar os efeitos passivos e ativos, se houver
            atributos_totais[key] = f"{atributos1.get(key, '')} {atributos2.get(key, '')}".strip()
        else:
            atributos_totais[key] = atributos1.get(key, 0) + atributos2.get(key, 0)
    
    return atributos_totais

def aplicar_buffs(atributos_base, buffs):
    """Aplica os buffs aos atributos base, somando os valores."""
    for buff in buffs:
        atributos_buff = buff['atributos']
        for key in atributos_base.keys():
            if key in ['efeito_passivo', 'efeito_ativo']:
                # Concatenar os efeitos passivos e ativos dos buffs
                atributos_base[key] = f"{atributos_base.get(key, '')} {atributos_buff.get(key, '')}".strip()
            else:
                atributos_base[key] += atributos_buff.get(key, 0)
    return atributos_base

def calcular_atributos_derivados(atributos_base, ultimo_capitulo):
    """Calcula os atributos derivados (ATQ, MATQ, HIT, Critical, DEF, MDEF, flee) baseados no Ragnarok Online."""
    ATQ = atributos_base['STR'] * 1 + ultimo_capitulo.get('ATQ', 0)
    MATQ = atributos_base['INT'] * 1.5 + ultimo_capitulo.get('MATQ', 0)
    HIT = atributos_base['DEX'] * 2 + ultimo_capitulo.get('HIT', 0)
    Critical = atributos_base['LUK'] / 3 + ultimo_capitulo.get('Critical', 0)
    DEF = atributos_base['VIT'] / 2 + ultimo_capitulo.get('DEF', 0)
    MDEF = atributos_base['INT'] / 2 + ultimo_capitulo.get('MDEF', 0)
    flee = atributos_base['AGI'] * 1.5 + ultimo_capitulo.get('flee', 0)
    
    return {
        "ATQ": ATQ,
        "MATQ": MATQ,
        "HIT": HIT,
        "Critical": Critical,
        "DEF": DEF,
        "MDEF": MDEF,
        "flee": flee
    }

def main():
    arquivo_atributos = './historia/inventario/atributos.json'
    arquivo_equipamentos = './historia/inventario/equipamentos_equipados.json'
    arquivo_buffs = './historia/inventario/buffs.json'

    # Carregar os dados do último capítulo, dos equipamentos equipados e dos buffs
    ultimo_capitulo = carregar_ultimo_capitulo(arquivo_atributos)
    equipamentos_equipados = carregar_equipamentos_equipados(arquivo_equipamentos)
    buffs = carregar_buffs(arquivo_buffs)

    # Somar os atributos base dos dois conjuntos de dados (último capítulo + equipamentos)
    atributos_base = somar_atributos_base(ultimo_capitulo, equipamentos_equipados)

    # Aplicar os buffs aos atributos base
    atributos_base_com_buffs = aplicar_buffs(atributos_base, buffs)

    # Calcular os atributos derivados
    atributos_derivados = calcular_atributos_derivados(atributos_base_com_buffs, ultimo_capitulo)

    # Exibir os resultados totais
    print("Atributos Base (com Buffs) (STR, AGI, VIT, INT, DEX, LUK, Efeito Passivo, Efeito Ativo):")
    print(atributos_base_com_buffs)
    print("\nAtributos Derivados (com Buffs) (ATQ, MATQ, HIT, Critical, DEF, MDEF, flee):")
    print(atributos_derivados)

    # Criar ou atualizar o arquivo JSON com os atributos totais atuais
    dados_finais = {
        "atributos_base": atributos_base_com_buffs,
        "atributos_derivados": atributos_derivados
    }
    
    with open('./historia/inventario/atributos_totais.json', 'w') as f:
        json.dump(dados_finais, f, indent=4)

    print("\nAtributos totais (com buffs) salvos com sucesso no arquivo 'atributos_totais.json'.")

if __name__ == "__main__":
    main()
