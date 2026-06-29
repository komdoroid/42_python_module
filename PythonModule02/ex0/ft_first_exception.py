#! /usr/bin/python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    test_cases = ['25', 'abc']
    for temp in test_cases:
        print(f"Input data is '{temp}'")
        try:
            print(f'Temperature is now {input_temperature(temp)}°C\n')
        except Exception as e:
            print(f'Caught input_temperature error: {e}\n')
    print('All tests completed - program didn\'t crash')


if __name__ == '__main__':
    print('=== Garden Temperature ===\n')
    test_temperature()
