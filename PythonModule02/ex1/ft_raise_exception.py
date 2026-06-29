#! /usr/bin/python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int < 0:
        raise ValueError(f'{temp_int}°C is too cold for plants (min 0°C)')
    if 40 < temp_int:
        raise ValueError(f'{temp_int}°C is too hot for plants (max 40°C)')
    return int(temp_str)


def test_temperature() -> None:
    test_cases = ['25', 'abc', '100', '-50']
    for temp in test_cases:
        print(f"Input data is '{temp}'")
        try:
            print(f'Temperature is now {input_temperature(temp)}°C\n')
        except Exception as e:
            print(f'Caught input_temperature error: {e}\n')
    print('All tests completed - program didn\'t crash')


if __name__ == '__main__':
    print('=== Garden Temperature Checker ===\n')
    test_temperature()
