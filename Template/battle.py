from Personage.Group.warrior import Warrior

def battle(personage: Warrior) -> None:
    atual_level = personage.level

    personage.upgrade_level(100)

    if atual_level != personage.level:
        
        print(f"""
    Parabéns você subiu para o nível {personage.level}!
    Falta {personage.max_xp - personage.xp} para o próximo nível.
    """)

        input(f"""
    Você tem {personage.atributes_points} pontos disponíveis
        
        
        """)
