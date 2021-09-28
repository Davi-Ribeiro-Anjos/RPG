from .atributes import AtributeClass


class AtributeFunctionClass(AtributeClass):

    def __init__(self, name, sex) -> None:
        super().__init__(name, sex)

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