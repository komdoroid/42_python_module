class Plant:
    def __init__(self, name: str, height: float,
                 age: int, growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.plant_age = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f'{self.name}: {self.height:.1f}cm, '
              f'{self.plant_age} days old')

    def grow(self) -> None:
        self.height = self.height + self.growth_rate

    def age(self) -> None:
        self.plant_age = self.plant_age + 1


rose = Plant('Rose', 25, 30, 0.8)
sunflower = Plant('Sunflower', 80, 45, 1)
cactus = Plant('Cactus', 15, 120, 0.3)

if __name__ == '__main__':
    print('=== Garden Plant Growth ===')
    rose.show()
    now = rose.height
    for i in range(1, 8):
        print(f'=== Day {i} ===')
        rose.grow()
        rose.age()
        rose.show()
    estimate = rose.height
    print(f'Growth this week: {(estimate - now):.1f}cm')
