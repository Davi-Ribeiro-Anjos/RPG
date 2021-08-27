from ..basic_functions import PersonageFunction

class Mage(PersonageFunction):

    def __init__(self, name, sex) -> None:
        super().__init__(name, sex)
        self.life = 150
        self.mana = 100
    
    def update_atributes(self):
        self.max_life = 150 + self.distribute_points('vitality', 'life')
        self.armor = 35 + self.distribute_points('vitality', 'armor')
        self.max_mana = 100 + self.distribute_points('power', 'mana')
        self.damage = 100 + self.distribute_points('power', 'damage')
        self.critic_damage = 2
        self.life_steal = 0