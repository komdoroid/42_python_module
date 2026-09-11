from ex0 import CreatureFactory, FlameFactory, AquaFactory


if __name__ == '__main__':
    for factory in (FlameFactory(), AquaFactory()):
        print('Testing Factory')
        c = factory
        base = c.create_base()
        base.describe()
        base.attack()

        evolved = c.create_evolved()
        evolved.describe()
        evolved.attack()
        print()

    print('Testing battle')
    flame = FlameFactory()
    aqua = AquaFactory()
    flame_base = flame.create_base()
    aqua_base = aqua.create_base()
    
    flame_base.describe()
    print(' vs')
    aqua_base.describe()
    print(' fight!')
    flame_base.attack()
    aqua_base.attack()
