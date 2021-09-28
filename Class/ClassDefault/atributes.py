class AtributeClass:

    def __init__(self, name, sex) -> None:
        self.name = name
        self.sex = sex

        self.level = 1
        self.total_xp = 0
        self.max_xp = 100
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

        self.gold = 100
        self.bag = {'food': 5}
        self.equipament = {
            'primary_weapon': None,
            'secundary_weapon': None,
            'armor': None
        }