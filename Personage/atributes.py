class PersonageAtributes:

    def __init__(self, name, sex) -> None:
        self.name = name
        self.sex = sex
        self.level = 1
        self.max_xp = 50
        self.xp = 0
        self.atributes_points = 0
        self.max_life = 100
        self.life = self.max_life
        self.is_live = True
        self.max_mana = 100
        self.mana = self.max_mana
        self.damage = 50
        self.armor = 20
        self.life_steal = 0
        self.bag = {'food': 5}
        self.equipament = {
            'primary_weapon': None,
            'secundary_weapon': None,
            'armor': None
        }
