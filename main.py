from Personage.basic_functions import PersonageFunction

# is_user = input("""
# Criar personagem?
# 1. Sim
# 2. Não

# Escolha uma opção: """)

# main_menu = input("""
# Menu principal:

# 1. Batalhar
# 2. Ver atributos
# 3. Ver equipamentos
# 4. Ver inventário
# 5. Sair

# Escolha uma opção: """)

personage = PersonageFunction('Davi', 'Masculino')

damage = 110
personage.calculate_damage(damage)
# print(f'Você perdeu {damage - personage.armor} de vida, lhe resta {personage.life}!')

personage.eat()
personage.is_upgrade(2000)

