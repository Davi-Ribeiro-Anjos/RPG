from ..basic_functions import PersonageFunction

class Mage(PersonageFunction):

    def __init__(self, name, sex) -> None:
        super().__init__(name, sex)
        self.max_life = 100 + self.distribute_points('vitality', 'life')
        self.life = self.max_life
        self.armor = 0 + self.distribute_points('vitality', 'armor')
        self.max_mana = 0 + self.distribute_points('power', 'mana')
        self.mana = self.max_mana
        self.damage = 0 + self.distribute_points('power', 'damage')
        self.critic_damage = 2
        self.chance_critic = 0 + self.distribute_points('critic', 'chance_critic')
        self.speed = 0 + self.distribute_points('critic', 'speed')
        self.life_steal = 0