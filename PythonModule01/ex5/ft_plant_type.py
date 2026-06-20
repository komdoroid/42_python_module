class Plant:
    DEFAULT_HEIGHT = 0
    DEFAULT_AGE = 0

    def __init__(self, name, height, age):
        self.name = name
        self._height = self.DEFAULT_HEIGHT
        self.set_height(height)
        self._age = self.DEFAULT_AGE
        self.set_age(age)

    def show(self) -> None:
        print(
                f'{self.name}: {self.get_height():.1f}cm, '
                f'{self.get_age()} days old'
                )

    def set_height(self, value: float) -> None:
        if 0 > value:
            print(f'{self.name}: Error, height can\'t be negative')
            print('Height update rejected')
        else:
            self._height = value

    def set_age(self, value: float) -> None:
        if 0 > value:
            print(f'{self.name}: Error, age can\'t be negative')
            print('Age update rejected')
        else:
            self._age = value

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> float:
        return self._age


class Flower(Plant):
    def super().__init__(self, name, height, age, color):
        self.coloer = coler

    def bloom():


class Tree(Plant):
    def super().__init__(self, name, height, age, trunk_diameter):
        self.trunk_diameter = trunk_diameter

    def produce_shade():


class Vegetable(Plant):
    def super().__init__(self, name, height, age):
        self.harvest_season = hearvest_season
        self.nutritional_value = nutritional_value


if __name__ == '__main__':
    print('=== Garden Security System ===')
    rose = Plant('Rose', 15, 10)
    print('Plant created: ', end="")
    rose.show()
    print('')

    rose.set_height(25)
    rose.set_age(30)
    print('')

    rose.set_height(-25)
    rose.set_age(-30)
    print('')

    print('Current state: ', end="")
    rose.show()
