#! /usr/bin/python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int < 0:
        raise ValueError(f'{temp_int}°C is too cold for plants (min 0°C)')
    if 40 < temp_int:
        raise ValueError(f'{temp_int}°C is too hot for plants (max 40°C)')
    return int(temp_str)


def test_temperature(temp: str) -> int:
    try:
        return input_temperature(temp)
    except Exception as e:
        # print(type(e))
        # print(type(e).__name__)
        # print(e.args)
        print(f'Caught input_temperature error: {e}\n')
        return 0


if __name__ == '__main__':
    print('=== Garden Temperature Checker ===\n')

    print("Input data is '25'")
    print(f'Temperature is now {test_temperature("25")}°C\n')

    print("Input data is 'abc'")
    test_temperature('abc')

    print("Input data is '100'")
    test_temperature('100')

    print("Input data is '-50'")
    test_temperature('-50')

    print('All tests completed - program didn\'t crash')
