class Plant:
    DEFAULT_HEIGHT: float = 0
    DEFAULT_AGE: int = 0

    class _Status:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def show_status(self) -> None:
            print(f'Status: {self._grow_count} grow, '
                  f'{self._age_count} age, {self._show_count} show')

    def __init__(self, name: str, height: float,
                 age: int, growth_rate: float) -> None:
        self._name = name
        self._height = self.DEFAULT_HEIGHT
        self.set_height(height)
        self._plant_age = self.DEFAULT_AGE
        self.set_age(age)
        self.growth_rate = growth_rate
        self._status = self._Status()

    def show(self) -> None:
        print(
                f'{self._name}: {self.get_height():.1f}cm, '
                f'{self.get_age()} days old'
                )
        self._status._show_count += 1

    def grow(self) -> None:
        self._height = self._height + self.growth_rate
        self._status._grow_count += 1

    def age(self) -> None:
        self._plant_age = self._plant_age + 20
        self._status._age_count += 1

    def set_height(self, value: float) -> None:
        if 0 > value:
            print(f'{self._name}: Error, height can\'t be negative')
            print('Height update rejected')
        else:
            self._height = value

    def set_age(self, value: int) -> None:
        if 0 > value:
            print(f'{self._name}: Error, age can\'t be negative')
            print('Age update rejected')
        else:
            self._plant_age = value

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> float:
        return self._plant_age

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        if age > 365:
            return True
        return False

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls(
                name='Unknown plant',
                height=cls.DEFAULT_HEIGHT,
                age=cls.DEFAULT_AGE,
                growth_rate=0
                )


class Flower(Plant):
    def __init__(self, name, height, age, growth_rate, color):
        super().__init__(name, height, age, growth_rate)
        self.color = color
        self.in_bloom = False

    def show(self) -> None:
        super().show()
        print(f' Color: {self.color}')
        if self.in_bloom:
            print(f' {self._name} is blooming beautifully!')
        else:
            print(f' {self._name} has not bloomed yet')

    def bloom(self) -> None:
        print('[asking the rose to bloom]')
        self.in_bloom = True


class Seed(Flower):
    DEFAULT_SEEDS = 0

    def __init__(self, name, height, age,
                 growth_rate, color, seed_num) -> None:
        super().__init__(name, height, age, growth_rate, color)
        self.seeds = seed_num

    def show(self) -> None:
        super().show()
        if self.in_bloom:
            print(f' Seeds: {self.seeds}')
        else:
            print(f' Seeds: {self.DEFAULT_SEEDS}')


class Tree(Plant):
    class _Status(Plant._Status):
        def __init__(self) -> None:
            super().__init__()
            self._produce_shade_count: int = 0

        def show_status(self) -> None:
            super().show_status()
            print(f' {self._produce_shade_count} shade')

    def __init__(self, name, height, age, growth_rate, trunk_diameter) -> None:
        super().__init__(name, height, age, growth_rate)
        self._status: Tree._Status = Tree._Status()
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f' Trunk diameter: {self.trunk_diameter:.1f}cm')

    def produce_shade(self) -> None:
        print('[asking the oak to produce shade]')
        print(f'Tree Oak now produces a shade of {self._height:.1f}cm long and '
              f'{self.trunk_diameter:.1f}cm wide')
        self._status._produce_shade_count += 1


class Vegetable(Plant):
    def __init__(
            self,
            name,
            height,
            age,
            growth_rate,
            harvest_season,
            nutritional_value
            ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f' Harvest season: {self.harvest_season}')
        print(f' Nutritional value {self.nutritional_value}')

    def grow(self) -> None:
        super().grow()
        self.nutritional_value = self.nutritional_value + 1


def show_plant_status(plant: Plant) -> None:
    print(f' [statistics for {plant._name}]')
    plant._status.show_status()


if __name__ == '__main__':
    print('=== Garden statistics ===')
    print('=== Check year-old')
    print(f'Is 30 days more than a year? -> {Plant.is_older_than_year(30)}')
    print(f'Is 400 days more than a year? -> '
          f'{Plant.is_older_than_year(400)}\n'
          )

    print('=== Flower')
    rose = Flower('Rose', 15, 10, 8, 'red')
    rose.show()
    show_plant_status(rose)
    rose.bloom()
    rose.grow()
    rose.show()
    show_plant_status(rose)
    print('')

    print('=== Tree')
    oak = Tree('Oak', 200, 365, 10, 5)
    oak.show()
    show_plant_status(oak)
    oak.produce_shade()
    show_plant_status(oak)
    print('')

    print('=== Seed')
    sunflower = Seed('Sunflower', 80, 45, 30, 'yellow', 42)
    sunflower.show()
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    show_plant_status(sunflower)
    print('')

    print('=== Anonymous')
    unknown = Plant.create_anonymous()
    unknown.show()
    show_plant_status(unknown)
