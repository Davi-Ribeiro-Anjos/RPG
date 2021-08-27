from .atributes import PersonageAtributes

class PersonageFunction(PersonageAtributes):

    def __init__(self, name, sex) -> None:
        super().__init__(name, sex)

    def is_upgrade(self, received_xp):
        if (received_xp + self.xp) > self.max_xp:
            self.xp = received_xp + self.xp - self.max_xp
            self.atributes_points += 5
            self.max_xp += 50
            self.level += 1

            self.is_upgrade(0)

    def is_dead(self):
        if self.life <= 0:
            self.is_live = False
    
    def calculate_damage(self, damage):
        self.life -= damage - self.armor
        
    def eat(self):
        self.life += 200
        self.bag['food'] -= 1

        if self.life > self.max_life:
            self.life = self.max_life