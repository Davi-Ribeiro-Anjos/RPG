from Service.verify_options import verify_options

from Template import CombatTemplate, LevelTemplate

from Class.Classes import Warrior
from Enemy.basic_enemy import FirstEnemy


personage = Warrior('Davi', 'Masculino')
personage.update_atributes()

def main_menu():

    option = input("""
    Menu principal:

    1. Batalhar
    2. Ver atributos
    3. Distribuir atributos
    4. Ver inventário
    5. Configuração
    6. Sair e Salvar

    Escolha uma opção: """)

    if verify_options(option, 6):
        options = {
            '1': lambda : CombatTemplate.battle(personage, FirstEnemy('Lobo')),
            '2': lambda : LevelTemplate.view_atributes(personage),
            '3': lambda : LevelTemplate.distribution_points(personage),
            '4': 0,
            '5': 0,
            '6': 0
        }

        options[option]()

        main_menu()

    else:
        input('\n    Escolha uma opção válida...')
        main_menu()

main_menu()
