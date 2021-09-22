from Service import LevelServices

from Personage.Group import Warrior

class LevelTemplate:

    @staticmethod
    def level_up(personage: Warrior) -> str:
        try:
            points = input(f"""
    Parabéns você está no nível {personage.level}!
    Você tem {personage.atributes_points} pontos disponíveis.
    Você pode escolher entre 3 categorias para distribuir os pontos:

        1. Vitalidade: + 25 vida, + 5 armadura;
        2. Poder: + 10 dano, + 5 mana;
        3. Agilidade: + 0.5% de crítico, + 5 velocidade.
        
             V,P,A 
    Exemplo: 0,3,2      (caso tenha 5 pontos disponíveis) 
    Como deseja distribuir os pontos? : """)

            LevelServices.add_atributes(personage, points)

        except SyntaxError:
            input("""
    Escolha os atributos com base no exemplo.""")

            LevelTemplate.level_up(personage)
        
        except ValueError as e:
            input(f"""
    Você tentou adicionar {e.args[0] - e.args[1]} pontos além do disponível.""")

            LevelTemplate.level_up(personage)

    @staticmethod
    def current_level(personage: Warrior) -> str:
        print(f"""
    Você está no nível {personage.level}!
    Sua quantidade total de xp é de {personage.total_xp}...
    Quantidade de xp atual é de {personage.xp}, falta {personage.max_xp - personage.xp} para o próximo nível.
    """)