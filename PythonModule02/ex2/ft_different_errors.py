#! /usr/bin/python3

def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        int('invalid data')
    elif (operation_number == 1):
        print(10 / 0)
    elif (operation_number == 2):
        open('/non/existent/file', 'r')
    elif (operation_number == 3):
        print('invalid data' + 10)
    else:
        print('Operation completed successfully')


def test_error_types() -> None:
    for operation_number in range(5):
        print(f'Testing operation {operation_number}...')
        try:
            garden_operations(operation_number)
        except ValueError as e:
            print(f'Caught ValueError: {e}')
        except ZeroDivisionError as e:
            print(f'Caught ZeroDivisionError : {e}')
        except FileNotFoundError as e:
            print(f'Caught FileNotFoundError : {e}')
        except TypeError as e:
            print(f'Caught TypeError : {e}')
    print('\nAll error types tested successfully!')


if __name__ == '__main__':
    print('=== Garden Error Types Demo ===')
    test_error_types()
