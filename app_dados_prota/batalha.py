class Personagem:
    def __init__(self, hp, mp, atk, defense, vit, aspd, hit, flee):
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.defense = defense  # Hard DEF (proveniente de equipamentos)
        self.vit = vit  # Soft DEF (proveniente da VIT)
        self.aspd = aspd
        self.hit = hit
        self.flee = flee

    def calcular_soft_def(self):
        # Fórmula simplificada para Soft DEF baseada na VIT
        return self.vit * 0.3  # 30% da VIT é considerada na soft DEF


class Monstro:
    def __init__(self, hp, atk, defense, aspd, req_hit, req_flee):
        self.hp = hp
        self.atk = atk
        self.defense = defense  # Hard DEF do monstro
        self.aspd = aspd
        self.req_hit = req_hit
        self.req_flee = req_flee


def calcular_dano(atk, soft_def, hard_def):
    # Fórmula que subtrai a defesa total (hard DEF + soft DEF) do ataque
    defense_total = soft_def + hard_def
    return max(0, atk - defense_total)


def calcular_ataques_por_segundo(aspd):
    return 1 / (200 - aspd)  # Fórmula simplificada para determinar ataques/segundo


def batalha(personagem, monstro, idioma):
    # Definindo mensagens com base no idioma
    mensagens = {
        "pt": {
            "dano_personagem": "Dano que o Azoth causa no monstro:",
            "dano_monstro": "Dano que o monstro causa no Azoth:",
            "resumo": "\n--- Resumo da Batalha ---",
            "ataques_personagem": "O Azoth deu",
            "ataques_monstro": "O monstro deu",
            "dano_total": "de dano total.",
            "hp_personagem": "HP final do Azoth:",
            "hp_monstro": "HP final do monstro:",
            "vitoria_personagem": "Resultado: O Azoth venceu a batalha!",
            "vitoria_monstro": "Resultado: O monstro venceu a batalha!",
            "empate": "Resultado: Ambos morreram simultaneamente!"
        },
        "en": {
            "dano_personagem": "Damage dealt by Azoth to the monster:",
            "dano_monstro": "Damage dealt by the monster to the Azoth:",
            "resumo": "\n--- Battle Summary ---",
            "ataques_personagem": "Azoth made",
            "ataques_monstro": "The monster made",
            "dano_total": "total damage.",
            "hp_personagem": "Final HP of the Azoth:",
            "hp_monstro": "Final HP of the monster:",
            "vitoria_personagem": "Result: Azoth won the battle!",
            "vitoria_monstro": "Result: The monster won the battle!",
            "empate": "Result: Both died simultaneously!"
        }
    }

    # Calcula Soft DEF (defesa da VIT)
    soft_def_personagem = personagem.calcular_soft_def()

    # Dano do personagem no monstro (monstro não tem soft DEF)
    dano_personagem = calcular_dano(personagem.atk, 0, monstro.defense)  
    print(f'{mensagens[idioma]["dano_personagem"]} {dano_personagem}')

    # Dano do monstro no personagem (levando em conta soft DEF e hard DEF)
    dano_monstro = calcular_dano(monstro.atk, soft_def_personagem, personagem.defense)
    print(f'{mensagens[idioma]["dano_monstro"]} {dano_monstro}')

    # Velocidade de ataque (ataques por segundo)
    ataques_personagem_por_segundo = calcular_ataques_por_segundo(personagem.aspd)
    ataques_monstro_por_segundo = calcular_ataques_por_segundo(monstro.aspd)

    # Quantos ataques o personagem precisa para matar o monstro
    ataques_ate_monstro_morrer = monstro.hp / dano_personagem if dano_personagem > 0 else float('inf')
    tempo_para_monstro_morrer = ataques_ate_monstro_morrer / ataques_personagem_por_segundo

    # Quantos ataques o monstro precisa para matar o personagem
    ataques_ate_personagem_morrer = personagem.hp / dano_monstro if dano_monstro > 0 else float('inf')
    tempo_para_personagem_morrer = ataques_ate_personagem_morrer / ataques_monstro_por_segundo

    # Quantos ataques o personagem e o monstro conseguem dar até um morrer
    ataques_personagem_dados = min(ataques_ate_monstro_morrer, tempo_para_personagem_morrer * ataques_personagem_por_segundo)
    ataques_monstro_dados = min(ataques_ate_personagem_morrer, tempo_para_monstro_morrer * ataques_monstro_por_segundo)

    # HP final após a batalha
    hp_final_personagem = max(0, personagem.hp - ataques_monstro_dados * dano_monstro)
    hp_final_monstro = max(0, monstro.hp - ataques_personagem_dados * dano_personagem)

    print(mensagens[idioma]["resumo"])
    print(f'{mensagens[idioma]["ataques_personagem"]} {ataques_personagem_dados:.0f} attacks, causing {ataques_personagem_dados * dano_personagem:.0f} {mensagens[idioma]["dano_total"]}')
    print(f'{mensagens[idioma]["ataques_monstro"]} {ataques_monstro_dados:.0f} attacks, causing {ataques_monstro_dados * dano_monstro:.0f} {mensagens[idioma]["dano_total"]}')
    print(f'{mensagens[idioma]["hp_personagem"]} {hp_final_personagem:.0f}')
    print(f'{mensagens[idioma]["hp_monstro"]} {hp_final_monstro:.0f}')

    # Ajuste da condição de vitória
    if hp_final_monstro == 0 and hp_final_personagem > 0:
        print(mensagens[idioma]["vitoria_personagem"])
    elif hp_final_personagem == 0 and hp_final_monstro > 0:
        print(mensagens[idioma]["vitoria_monstro"])
    elif hp_final_personagem == 0 and hp_final_monstro == 0:
        print(mensagens[idioma]["empate"])


# Input para escolha de idioma
idioma = input("Escolha o idioma (pt para português, en para inglês): ").lower()

# Exemplo de uso:
personagem = Personagem(hp=335, mp=92, atk=51, defense=80, vit=6, aspd=113, hit=12, flee=12)
monstro = Monstro(hp=127, atk=85, defense=22, aspd=100, req_hit=222, req_flee=205)

batalha(personagem, monstro, idioma)
