"""Copyright marceloalvescl"""

class Game:
    """Classe para definir um jogo"""

    def __init__(self, owner, numbers):
        self.owner = owner
        self.numbers = numbers
        self.numbers_correct = 0
