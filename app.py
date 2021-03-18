from fmanager import FileManager

print('Файловый менеджер запущен \n')

while True:
    try:
        command = input('').split(' ')
        if command[0] == 'q':
            print('Файловый менеджер отключен')
            break

        elif command[0] == 'pwd':
            print(FileManager.get_pwd())

        elif command[0] + command[1] == 'getlist':
            if len(command) == 2:
             print(FileManager.show_list())
            else:
                print(FileManager.show_list(command[2]))

        elif (command[0] + command[1]) == 'moveup':
            print(FileManager.move_up())

        elif (command[0] + command[1]) == 'create-d':
            print(FileManager.create_directory(command[2]))

        elif (command[0] + command[1]) == 'remove-d':
            print(FileManager.remove_directory(command[2]))

        elif (command[0] + command[1]) == 'movein':
            print(FileManager.move_in_path(command[2]))

        elif (command[0] + command[1]) == 'create-f':
            print(FileManager.create_file(command[2]))

        elif (command[0] + command[1]) == 'read-f':
            print(FileManager.read_file(command[2]))

        elif (command[0] + command[1]) == 'remove-f':
            print(FileManager.delete_file(command[2]))

        elif (command[0] + command[1]) == 'copy-f':
            print(FileManager.copy_file(command[2], command[3]))

        elif (command[0] + command[1]) == 'move-f':
            print(FileManager.move_file(command[2], command[3]))

        elif (command[0] + command[1]) == 'rename-f':
            print(FileManager.rename_file(command[2], command[3]))

        elif (command[0] + command[1]) == 'write-f':
            print(FileManager.write_file(command[2], command[3]))

        else:
            print('Команда введена неверно')
    except IndexError:
        print('Команда введена неверно')
    except KeyboardInterrupt as f:
        print(f'Программа закрыта неправильно {f}')
        break