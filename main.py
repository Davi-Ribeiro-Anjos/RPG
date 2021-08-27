from Service.verify_options import verify_options
from Personage.Group import Warrior
from Template import BattleTemplate

# is_user = input("""
# Criar personagem?
# 1. Sim
# 2. Não

# Escolha uma opção: """)

personage = Warrior('Davi', 'Masculino')

def main_menu():

    option = input("""
    Menu principal:

    1. Batalhar
    2. Ver atributos
    3. Ver equipamentos
    4. Ver inventário
    5. Configuração
    6. Sair e Salvar

    Escolha uma opção: """)

    if verify_options(option, 6):
        options = {
            '1': BattleTemplate.battle(personage),
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0
        }

        options[option]

        main_menu()

    else:
        print('\n\n    Escolha uma opção válida...\n')
        main_menu()

main_menu()
