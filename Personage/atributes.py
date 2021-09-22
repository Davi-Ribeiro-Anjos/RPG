class PersonageAtributes:

    def __init__(self, name, sex) -> None:
        self.name = name
        self.sex = sex
        self.level = 1
        self.total_xp = 0
        self.max_xp = 50
        self.xp = 0
        self.atributes_points = 0
        self.quantity = {
            'vitality': 0,
            'power': 0,
            'agility': 0
        }
        self.max_life = 0
        self.life = self.max_life
        self.is_live = True
        self.max_mana = 0
        self.mana = self.max_mana
        self.damage = 0
        self.damage_critic = 2
        self.chance_critic = 0
        self.armor = 0
        self.speed = 0
        self.life_steal = 0
        self.gold = 0
        self.bag = {'food': 5}
        self.equipament = {
            'primary_weapon': None,
            'secundary_weapon': None,
            'armor': None
        }
    
    def distribute_points(self, type: str, atribute: str) -> int:
        atributes = {
            'vitality': {'life': 25, 'armor': 5},
            'power': {'damage': 10, 'mana': 5},
            'agility': {'chance_critic': 0.005, 'speed': 5}
        }

        return atributes[type][atribute] * self.quantity[type]
    
    def add_quantity_atribute(self, list_quantity: list) -> None:
        total_points = 0

        for quantity in list_quantity:
            total_points += quantity

        if total_points <= self.atributes_points:
            self.atributes_points -= total_points
            self.quantity['vitality'] += list_quantity[0]
            self.quantity['power'] += list_quantity[1]
            self.quantity['agility'] += list_quantity[2]
        else:
            raise ValueError(total_points, self.atributes_points)