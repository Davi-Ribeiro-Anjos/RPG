from .level_functions import LevelFunctionClass

class DefaultClass(LevelFunctionClass):

    def __init__(self, name, sex) -> None:
        super().__init__(name, sex)

        