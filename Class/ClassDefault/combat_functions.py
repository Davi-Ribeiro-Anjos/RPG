from .atributes_functions import AtributeFunctionClass

class CombatFunctionClass(AtributeFunctionClass):

    def __init__(self, name, sex) -> None:
        super().__init__(name, sex)
    
    def calculate_damage(self, damage: int) -> int:
        if damage > self.armor:
            self.life -= damage - self.armor

        self.is_dead()

        return damage - self.armor

    def is_dead(self) -> None:
        if self.life <= 0:
            self.is_live = False
            self.xp = 0
            self.gold = 0