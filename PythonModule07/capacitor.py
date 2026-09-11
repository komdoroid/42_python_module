from ex1 import CreatureFactory, HealingCreatureFactory, TransformCreatureFactory

if __name__ == '__main__':
    print('Testing Creature with healing capability')
    print(' base:')
    hcf = HealingCreatureFactory()
    hc = hcf.create_base()
    hc.describe()
    hc.attack()
    hc.heal()

    print(' evolved:')
    hc = hcf.create_evolved()
    hc.describe()
    hc.attack()
    hc.heal('itself and others')

    print()

    print('Testing Creature with transform capability')
    print(' base:')
    tcf = TransformCreatureFactory()
    tc = tcf.create_base()
    tc.describe()
    tc.attack()
    tc.transform()
    tc.attack()
    tc.revert()

    print(' evolved:')
    tc = tcf.create_evolved()
    tc.describe()
    tc.attack()
    tc.transform()
    tc.attack()
    tc.revert()
