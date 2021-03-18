import os
from SETTINGS import pathway
from shutil import copyfile, move, rmtree

pathway = pathway
head_directory_name = os.path.split(pathway)[1]


class FileManager:
    @staticmethod
    def create_directory(name):
        if os.path.isdir(fr'{os.path.join(pathway, name)}') is False:
            os.mkdir(f"{os.path.join(pathway, name)}")
            dir_way = os.path.join(pathway, name)
            return f'{dir_way} - создан'
        else:
            return f'Папка уже создана'

    @staticmethod
    def remove_directory(name):
        files = os.listdir(f'{os.path.join(pathway, name)}')
        if len(files) > 0:
            rmtree(f'{os.path.join(pathway, name)}')
            return f'папка {name} удалена рекурсивным методом'
        else:
            os.rmdir(f"{os.path.join(pathway, name)}")
            return f'папка {name} удалена'

    @staticmethod
    def move_in_path(name):
        global pathway
        if os.path.isdir(f'{os.path.join(pathway, name)}'):
            pathway = fr'{os.path.join(pathway, name)}'
            return pathway
        else:
            return 'Папка не существует'

    @staticmethod
    def move_up():
        global pathway
        if os.path.split(pathway)[1] != head_directory_name:
            pathway = os.path.split(pathway)[0]
            return pathway
        else:
            return "Переместиться выше нельзя"

    @staticmethod
    def create_file(name):
        file_name = os.path.join(pathway, name)
        if os.path.isfile(fr'{os.path.join(pathway, name)}') is False:
            file = open(fr'{file_name}', 'w')
            file.close()
            return f'{file_name} создан'
        else:
            return f'Файл {name} уже существует'

    @staticmethod
    def write_file(name, text):
        file = os.path.isfile(os.path.join(pathway, name))
        if file:
            with open(os.path.join(pathway, name), 'w') as f:
                f.write(text)
            return f'в файл {name} записан текст'
        else:
            return f'Файл {name}не существует'

    @staticmethod
    def read_file(name):
        file = os.path.isfile(os.path.join(pathway, name))
        if file:
            with open(os.path.join(pathway, name), 'r') as f:
                read = f.read()
            return read
        else:
            return f"Файл {name} не существует"

    @staticmethod
    def delete_file(name):
        file = os.path.isfile(os.path.join(pathway, name))
        if file:
            os.remove(os.path.join(pathway, name))
            return f'Файл {os.path.join(pathway, name)} удален'
        return f'Файл {name} не существует'

    @staticmethod
    def copy_file(name, to):
        directory = os.path.isdir(os.path.join(pathway, os.path.split(to)[0]))
        file = os.path.isfile(os.path.join(pathway, name))
        if file and directory:
            copyfile(os.path.join(pathway, name), os.path.join(pathway, to))
            return f"Файл {os.path.join(pathway, name)} копирован в {os.path.join(pathway, to)}"
        elif file is False:
            return f"Файл {name} не найден"
        else:
            return f"Директория {to} не найдена"

    @staticmethod
    def move_file(name, to):
        directory = os.path.isdir(os.path.join(pathway, os.path.split(to)[0]))
        file = os.path.isfile(os.path.join(pathway, name))
        if file and directory:
            move(os.path.join(pathway, name), os.path.join(pathway, to))
            return f"Файл {os.path.join(pathway, name)} перемещен в {os.path.join(pathway, to)}"
        elif file is False:
            return f"Файл {os.path.join(pathway, name)} не найден"
        else:
            return f"Директория {os.path.join(pathway, to)} не найдена"

    @staticmethod
    def rename_file(name, to):
        file = os.path.isfile(os.path.join(pathway, name))
        if file:
            os.rename(os.path.join(pathway, name), os.path.join(pathway, to))
            return f"Файл {os.path.join(pathway, name)} переименован в {os.path.join(pathway, to)}"

    @staticmethod
    def get_pwd():
        return pathway

    @staticmethod
    def show_list(path=None):
        return f'Содержимое текущей дериктории: {", ".join(os.listdir(pathway))}' if path is None else f'Содержимое директории: {", ".join(os.listdir(os.path.join(pathway, path)))}'