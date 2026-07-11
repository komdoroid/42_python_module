#!/usr/bin/env python3


def secure_archive(file_name: str,
                   option: int = 0,
                   content: str = ''
                   ) -> tuple[bool, str]:
    success_message = 'Content successfully writtten to file'
    try:
        if option == 0:
            with open(file_name, 'r') as f:
                content = f.read()
        if option == 1:
            with open(file_name, 'w') as f:
                f.write(content)
                content = success_message
        return True, content
    except FileNotFoundError as e:
        return False, str(e)
    except PermissionError as e:
        return False, str(e)
    except OSError as e:
        return False, str(e)


if __name__ == '__main__':
    print('=== Cyber Archives Security ===\n')

    file_names = ['/not/existing/file',
                  '/etc/master.passwd',
                  'ancient_fragment.txt',
                  'new']

    print(f"Using '{secure_archive.__name__}' "
          f"to read from a nonexistent file:")
    bl, message = secure_archive(file_names[0], 0)
    print(f'({bl}, "{message}")\n')

    print(f"Using '{secure_archive.__name__}' "
          f"to read from a inaccessible file:")
    bl, message = secure_archive(file_names[1], 0)
    print(f'({bl}, "{message}")\n')

    print(f"Using '{secure_archive.__name__}' to read from a regular file:")
    bl, message = secure_archive(file_names[2], 0)
    replaced_message = message.replace('\n', '\\n')
    print(f"({bl}, '{replaced_message}')\n")

    print(f"Using '{secure_archive.__name__}' "
          f"to write previous content to a new file:")
    bl, message = secure_archive(file_names[3], 1)
    print(f"({bl}, '{message}')\n")
