
class FirstEnemy():

    def __init__(self, name) -> None:
        self.name = name
        self.xp = 5000
        self.max_life = 50
        self.life = self.max_life
        self.armor = 0
        self.damage = 150
        self.speed = 150
        self.is_live = True


    def calculate_damage(self, damage: int) -> int:
        if damage > self.armor:
            self.life -= damage - self.armor

        self.is_dead()

        return damage - self.armor
    
    def is_dead(self) -> None:
        if self.life <= 0:
            self.is_live = False