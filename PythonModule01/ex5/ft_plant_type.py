class Plant:
    DEFAULT_HEIGHT = 0
    DEFAULT_AGE = 0

    def __init__(self, name, height, age):
        self.name = name
        self._height = self.DEFAULT_HEIGHT
        self.set_height(height)
        self._plant_age = self.DEFAULT_AGE
        self.set_age(age)

    def show(self) -> None:
        print(
                f'{self.name}: {round(self.get_height(), 1)}cm, '
                f'{self.get_age()} days old'
                )

    def grow(self):
        self._height = self._height + self.growth_rate

    def age(self):
        self._plant_age = self._plant_age + 1

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
            self._plant_age = value

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> float:
        return self._plant_age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.in_bloom = False

    def show(self) -> None:
        super().show()
        print(f' Color: {self.color}')
        if self.in_bloom:
            print(f' {self.name} is blooming beautifully!')
        else:
            print(f' {self.name} has not bloomed yet')

    def bloom(self) -> None:
        print('[asking the rose to bloom]')
        self.in_bloom = True


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f' Trunk diameter: {self.trunk_diameter}cm')

    def produce_shade(self) -> None:
        print('[asking the oak to produce shade]')
        print(f'Tree Oak now produces a shade of {self._height}cm long and '
              f'{round(self.trunk_diameter, 1)}cm wide')


class Vegetable(Plant):
    growth_rate = 2.1

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f' Harvest season: {self.harvest_season}')
        print(f' Nutritional value {self.nutritional_value}')

    def grow(self) -> None:
        super().grow()
        self.nutritional_value = self.nutritional_value + 1


if __name__ == '__main__':
    print('=== Garden Plant Types ===')
    print('=== Flower')
    rose = Flower('Rose', 15, 10, 'red')
    rose.show()
    rose.bloom()
    rose.show()
    print('')

    print('=== Tree')
    oak = Tree('Oak', 200, 365, 5)
    oak.show()
    oak.produce_shade()
    print('')

    print('=== Vegetable')
    tomato = Vegetable('Tomato', 5, 10, 'April', 0)
    tomato.show()
    print('[make tomato grow and age for 20 days]')
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
