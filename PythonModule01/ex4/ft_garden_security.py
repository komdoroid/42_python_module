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
                f'{self.name}: {round(self.get_height()):.1f}cm, '
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


if __name__ == '__main__':
    print('=== Garden Security System ===')
    rose = Plant('Rose', 15, 10)
    print('Plant created: ', end="")
    rose.show()
    print('')

    rose.set_height(25)
    value = rose.get_height()
    print(f'Height updated: {value}cm')
    rose.set_age(30)
    value = rose.get_age()
    print(f'Age updated: {value} days')
    print('')

    rose.set_height(-25)
    rose.set_age(-30)
    print('')

    print('Current state: ', end="")
    rose.show()
