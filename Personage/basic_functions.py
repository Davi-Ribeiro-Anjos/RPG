from .atributes import PersonageAtributes

class PersonageFunction(PersonageAtributes):

    def __init__(self, name, sex) -> None:
        super().__init__(name, sex)

    def upgrade_level(self, received_xp: int) -> None:
        if (received_xp + self.xp) > self.max_xp:
            self.xp = received_xp + self.xp - self.max_xp
            self.atributes_points += 5
            self.max_xp += 50
            self.level += 1

            # self.life += self.max_life * 0.2
            # if self.life > self.max_life:
            #     self.life = self.max_life

            # self.mana += self.max_mana * 0.2
            # if self.mana > self.max_mana:
            #     self.mana = self.max_mana

            self.upgrade_level(0)

    def is_dead(self) -> None:
        if self.life <= 0:
            self.is_live = False
            self.xp = 0
            self.gold = 0
    
    def calculate_damage(self, damage: int) -> None:
        self.life -= damage - self.armor
        
    def eat(self) -> None:
        self.life += 25
        self.bag['food'] -= 1

        if self.life > self.max_life:
            self.life = self.max_life