from Personage.Group import Warrior

from .level import LevelTemplate

class BattleTemplate:

    @staticmethod
    def battle(personage: Warrior) -> None:
        atual_level = personage.level
        personage.upgrade_level(500)

        if atual_level < personage.level:
            LevelTemplate.level_up(personage)
