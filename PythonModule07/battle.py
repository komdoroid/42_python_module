from ex0 import CreatureFactory, FlameFactory, AquaFactory


def factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    base.describe()
    base.attack()

    evolved = factory.create_evolved()
    evolved.describe()
    evolved.attack()


def battle(factory1: CreatureFactory,
           factory2: CreatureFactory) -> None:
    flame_base = flame.create_base()
    aqua_base = aqua.create_base()

    flame_base.describe()
    print(' vs.')
    aqua_base.describe()
    print(' fight!')
    flame_base.attack()
    aqua_base.attack()


if __name__ == '__main__':
    for f in (FlameFactory(), AquaFactory()):
        print('Testing factory')
        factory(f)
        print()

    print('Testing battle')
    flame = FlameFactory()
    aqua = AquaFactory()
    battle(flame, aqua)
