from Personage.Group import Warrior

class LevelServices:

    @staticmethod
    def add_atributes(personage: Warrior, points: str) -> list:
        list_points = []

        for point in points.split(','):
            if bool(point) is False:
                list_points.append(0)
            else:
                list_points.append(int(point))
        
        personage.add_quantity_atribute(list_points)
        personage.update_atributes()
        personage.regen_life_mana()