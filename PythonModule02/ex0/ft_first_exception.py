#! /usr/bin/python3

def input_temperature(temp_str: str) -> int:
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
    print('=== Garden Temperature ===\n')

    print("Input data is '25'")
    print(f'Temperature is now {test_temperature("25")}°C\n')
    print("Input data is 'abc'")
    test_temperature('abc')

    print('All tests completed - program didn\'t crash')
