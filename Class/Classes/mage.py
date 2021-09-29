from ..ClassDefault import DefaultClass

class Mage(DefaultClass):

    def __init__(self, name, sex) -> None:
        super().__init__(name, sex)
        self.life = 150
        self.mana = 100
    
    def update_atributes(self):
        self.max_life = 400 + self.distribute_points('vitality', 'life')
        self.armor = 50 + self.distribute_points('vitality', 'armor')
        self.max_mana = 50 + self.distribute_points('power', 'mana')
        self.damage = 75 + self.distribute_points('power', 'damage')
        self.chance_critic = 0 + self.distribute_points('agility', 'chance_critic')
        self.speed = 100 + self.distribute_points('agility', 'speed')