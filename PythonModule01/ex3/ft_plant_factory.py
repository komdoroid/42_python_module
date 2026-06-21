class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f'Created: {self.name}: {round(self.height):.1f}cm, {self.age} days old')


rose = Plant('Rose', 25, 30)
oak = Plant('Oak', 200, 365)
cactus = Plant('Cactus', 5, 90)
sunflower = Plant('Sunflower', 80, 45)
fern = Plant('Fern', 15, 120)

if __name__ == '__main__':
    print('=== Plant Factory Output ===')
    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()
