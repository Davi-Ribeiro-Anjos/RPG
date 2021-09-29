from .combat_functions import CombatFunctionClass

class LevelFunctionClass(CombatFunctionClass):

    def __init__(self, name, sex) -> None:
        super().__init__(name, sex)

    def upgrade_level(self, received_xp: int) -> None:
        if (received_xp + self.xp) >= self.max_xp:
            self.xp = received_xp + self.xp - self.max_xp
            self.atributes_points += 3
            self.max_xp += 100
            self.total_xp += received_xp
            self.level += 1

            self.regen_life_mana()
            self.upgrade_level(0)
    
    def update_atributes(self):
        self.max_life = self.base_life + self.distribute_points('vitality', 'life')
        self.armor = self.base_armor + self.distribute_points('vitality', 'armor')
        self.max_mana = self.base_mana + self.distribute_points('power', 'mana')
        self.damage = self.base_damage + self.distribute_points('power', 'damage')
        self.chance_critic = self.base_critic + self.distribute_points('agility', 'chance_critic')
        self.speed = self.base_speed + self.distribute_points('agility', 'speed')

    
    def regen_life_mana(self):
        self.life += self.max_life * 0.2
        self.mana += self.max_mana * 0.2

        self.verify_life_mana()
        
    def eat(self) -> None:
        self.life += 25
        self.mana += 10
        self.bag['food'] -= 1

        self.verify_life_mana()

    def verify_life_mana(self):
        if self.life > self.max_life:
            self.life = self.max_life

        if self.mana > self.max_mana:
            self.mana = self.max_mana