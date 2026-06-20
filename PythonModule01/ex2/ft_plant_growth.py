class   Plant:
    def __init__(self, name, height, age, growth_rate):
        self.name = name
        self.height = height
        self.plant_age = age
        self.growth_rate = growth_rate

    def show(self):
        print(f'{self.name}: {self.height:.1f}cm, {self.plant_age} days old')

    def grow(self):
        self.height = self.height + self.growth_rate

    def age(self):
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
