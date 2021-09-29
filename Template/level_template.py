from Service import LevelServices

from Class.ClassDefault import DefaultClass

class LevelTemplate:

    @staticmethod
    def level_up(personage: DefaultClass) -> None:
        try:
            print(f'\n    Parabéns você está no nível {personage.level}!')
            
            points = LevelTemplate.distribution_points(personage)

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
    def distribution_points(personage: DefaultClass) -> str:
        points = input(f"""
    Você tem {personage.atributes_points} pontos disponíveis.
    Você pode escolher entre 3 categorias para distribuir os pontos:

        1. Vitalidade: + 25 vida, + 5 armadura;
        2. Poder: + 10 dano, + 5 mana;
        3. Agilidade: + 0.5% de crítico, + 5 velocidade.
        
             V,P,A 
    Exemplo: 0,3,2      (caso tenha 5 pontos disponíveis) 
    Como deseja distribuir os pontos? : """)

        return points 

    @staticmethod
    def view_atributes(personage: DefaultClass) -> None:
        input(f"""
    Você está no nível {personage.level}!
    Quantidade de xp atual é de {personage.xp}, falta {personage.max_xp - personage.xp} para o próximo nível.
    Seus atributos:
    Vida Máxima: {personage.max_life}      Vida: {personage.life}      Armadura: {personage.armor}   
    Mana Máxima: {personage.max_mana}      Mana: {personage.mana}      Dano: {personage.damage}
    Velocidade: {personage.speed}
    """)