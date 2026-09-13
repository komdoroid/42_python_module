from ex1 import HealingCreatureFactory, TransformCreatureFactory

if __name__ == '__main__':
    print('Testing Creature with healing capability')
    print(' base:')
    hcf = HealingCreatureFactory()
    hc_base = hcf.create_base()
    hc_base.describe()
    hc_base.attack()
    hc_base.heal()

    print(' evolved:')
    hc_evolved = hcf.create_evolved()
    hc_evolved.describe()
    hc_evolved.attack()
    hc_evolved.heal('itself and others')

    print()

    print('Testing Creature with transform capability')
    print(' base:')
    tcf = TransformCreatureFactory()
    tc_base = tcf.create_base()
    tc_base.describe()
    tc_base.attack()
    tc_base.transform()
    tc_base.attack()
    tc_base.revert()

    print(' evolved:')
    tc_evolved = tcf.create_evolved()
    tc_evolved.describe()
    tc_evolved.attack()
    tc_evolved.transform()
    tc_evolved.attack()
    tc_evolved.revert()
