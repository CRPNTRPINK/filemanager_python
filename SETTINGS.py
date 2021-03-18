import os
from sys import platform
pathway = None


def default_path():
    global pathway
    if platform == 'darwin' or platform == 'linux' or platform == 'linux2':
        pathway = os.path.join(os.getcwd(), os.environ.get("USER"))
    elif platform == 'win32':
        pathway = os.path.join(os.getcwd(), os.environ.get("USERNAME"))
    if os.path.isdir(os.environ.get('USER')) is False:
        os.mkdir(f'{pathway}')
    else:
        return f"Сдандартная директория уже создана - {pathway}"


default_path()
