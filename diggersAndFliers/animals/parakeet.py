from movements import Flying
from .animal import Animal

class Parakeet(Animal, Flying):
    def __init__(self, name):
        Animal.__init__(self, name)
        Flying.__init__(self)

    def __str__(self):
        return f'{self.name} the parakeet'

    def fly(self):
        print(f'{self.name} the parakeet flies')