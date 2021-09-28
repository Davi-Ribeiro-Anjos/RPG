from Class.Classes import Warrior
from Enemy.basic_enemy import FirstEnemy

from .level_template import LevelTemplate

class CombatTemplate:

    @staticmethod
    def battle(personage: Warrior, enemy: FirstEnemy) -> None:
        atual_level = personage.level
        round_personage, round_enemy = 0, 0
        speed_personage, speed_enemy = 0, 0

        while personage.is_live == True and enemy.is_live == True:
            speed_personage += personage.speed
            speed_enemy += enemy.speed

            if speed_personage >= 1000:
                round_personage += 1
                speed_personage -= 1000

                damage_recived = enemy.calculate_damage(personage.damage)

                if damage_recived <= 0:
                    damage_recived = 0

                input(f"""
    Você deu {damage_recived} de dano no inimigo!
    Agora ele está com {enemy.life} de vida!""")

            if speed_enemy >= 1000:
                round_enemy += 1
                speed_enemy -= 1000

                damage_recived = personage.calculate_damage(enemy.damage)

                if damage_recived <= 0:
                    damage_recived = 0
                    
                input(f"""
    Você recebeu {damage_recived} de dano no inimigo!
    Agora você está com {personage.life} de vida!""")
        
        if enemy.is_live == False:
            personage.upgrade_level(enemy.xp)

        if atual_level < personage.level:
            LevelTemplate.level_up(personage)
