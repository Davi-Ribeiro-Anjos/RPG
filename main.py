from Service.verify_options import verify_options
from Personage.Group.warrior import Warrior
from Template.battle import battle

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

    if verify_options(int(option), 6):
        options = {
            '1': battle(personage),
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
        }

        options[option]

main_menu()

personage.update_atributes()

personage.upgrade_level(2000)

personage.add_quantity_atribute([20, 5, 15])
personage.update_atributes()















# Vai ser usado pra distribuir atributos
# a = '1,   4 ,,7'
# ass = a.split(',')
# new = []
# for a in ass:
#     if bool(a) is False:
#         new.append(0)
#     else:
#         new.append(int(a))