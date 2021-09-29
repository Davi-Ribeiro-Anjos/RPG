from ..ClassDefault import DefaultClass

class Warrior(DefaultClass):
    
    def __init__(self, name, sex) -> None:
        super().__init__(name, sex) 
        self.base_life = 1000
        self.life = self.base_life
        self.base_armor = 100
        self.base_mana = 200
        self.mana = self.base_mana
        self.base_damage = 150
        self.base_critic = 0
        self.base_speed = 100