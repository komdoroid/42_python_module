from ex2 import (
        CreatureFactory,
        FlameFactory,
        AquaFactory,
        HealingCreatureFactory,
        TransformCreatureFactory,
        BattleStrategy,
        NormalStrategy,
        AggressiveStrategy,
        DefensiveStrategy,
        InvalidStrategyError)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    for i in range(len(opponents)):
        factory = opponents[i][0]
        strategy = opponents[i][1]
        creature = factory.create_base()
        for j in range(i + 1, len(opponents)):
            print('* Battle *')
            opponent_factory = opponents[j][0]
            opponent_strategy = opponents[j][1]
            opponent = opponent_factory.create_base()

            creature.describe()
            print(' vs.')
            opponent.describe()

            try:
                print(' now fight!')
                strategy.act(creature)
                opponent_strategy.act(opponent)
                print()
            except InvalidStrategyError as e:
                print(f'Battle error, aborting tournament: {e}\n')


if __name__ == '__main__':
    ff = FlameFactory()
    af = AquaFactory()
    hcf = HealingCreatureFactory()
    tcf = TransformCreatureFactory()

    ns = NormalStrategy()
    agrs = AggressiveStrategy()
    defs = DefensiveStrategy()

    print('Tournament 0 (basic)')
    opponents = [(ff, ns), (hcf, defs)]
    print(' [ (Flameling+Normal), (Healing+Defensive) ]')
    print('*** Tournament ***')
    print('2 opponents involved\n')
    battle(opponents)

    print('Tournament 1 (error)')
    opponents = [(ff, agrs), (hcf, defs)]
    print(' [ (Flameling+Aggressive), (Healing+Defensive) ]')
    print('*** Tournament ***')
    print('2 opponents involved\n')
    battle(opponents)

    print('Tournament 2 (multiple)')
    opponents = [(af, ns), (hcf, defs), (tcf, agrs)]
    print(' [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]')
    print('*** Tournament ***')
    print('3 opponents involved\n')
    battle(opponents)
