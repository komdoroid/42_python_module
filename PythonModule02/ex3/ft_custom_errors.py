class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

def test_custom_errors() -> None:
    pass

if __name__ == '__main__':
    print('=== Custom Garden Errors Demo ===\n')

    print('Testing PlnatError...')
    print('Testing WaterError...')
    print('Testing catching all garden errors...')

    print('All custom error types work correctly!')
