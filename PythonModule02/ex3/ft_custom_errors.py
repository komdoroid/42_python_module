#! /usr/bin/python3

class GardenError(Exception):
    def __init__(self,
                 message: str = 'Unknown plant error') -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self,
                 message: str = 'The tomato plant is wilting!') -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self,
                 message: str = 'Not enough water in the tank!') -> None:
        super().__init__(message)


def test_custom_errors(test_error_num: int) -> None:
    try:
        if test_error_num == 0:
            raise PlantError()
        if test_error_num == 1:
            raise WaterError()
    except PlantError as e:
        print(f'Caught PlantError: {e}')
    except WaterError as e:
        print(f'Caught WaterError: {e}')


def test_garden_error(test_error_num: int) -> None:
    try:
        if test_error_num == 0:
            raise PlantError()
        if test_error_num == 1:
            raise WaterError()
    except GardenError as e:
        print(f'Caught GardenError: {e}')


if __name__ == '__main__':
    print('=== Custom Garden Errors Demo ===\n')

    print('Testing PlnatError...')
    test_custom_errors(0)
    print()

    print('Testing WaterError...')
    test_custom_errors(1)
    print()

    print('Testing catching all garden errors...')
    test_garden_error(0)
    test_garden_error(1)
    print()

    print('All custom error types work correctly!')
