import os
import shutil
from distutils.dir_util import copy_tree # модуль предоставляет функции для работы с деревом каталогов и каталогами
import pytest

# наша рабочая директория
dir_path = '/Tests2'

@pytest.fixture # создание директории
def create_directory():
    directory_name = 'New directory'
    if not os.path.exists(f'{dir_path}/{directory_name}'):
        os.makedirs(f'{dir_path}/{directory_name}')
        print(f'Директория "{directory_name}" успешно создана')
        return True
    else:
        print('Директория уже существует')

@pytest.fixture # удаление директории
def delete_directory():
    directory_name = 'New directory'
    try:
        shutil.rmtree(f'{dir_path}/{directory_name}')
    except OSError as e:
        print(f'Error: {e.filename} - {e.strerror}')
    else:
        print(f'Директория "{directory_name}" успешно удалена')
        return True

@pytest.fixture # создание файла
def create_file():
    file_name = 'New_file.txt'
    if not os.path.exists(f'{dir_path}/{file_name}'):
        New_file = open(f'{dir_path}/{file_name}', 'w')
        New_file.close()
        print(f'Файл "{file_name}" успешно создан')
        return True
    else:
        print('Файл с таким названием уже существует')

@pytest.fixture # запись в файл
def overwrite_file():
    file_name = 'New_file.txt'
    try:
        with open(f'{dir_path}/{file_name}', mode='w') as f:
            f.write('привет, мир, это первая запись в этот файл')
    except FileNotFoundError:
        print(f'Файл с  именем = "{file_name}" не найден')
    except IsADirectoryError:
        print('Это директория, а не файл')
    else:
        print('Текст успешно записан в файл')
        return True

@pytest.fixture # чтение файла
def read_file():
    file_name = 'New_file.txt'
    try:
        file_location = f'{dir_path}/{file_name}'
        with open(file_location, 'r') as f:
            text = f.read()
        for line in text.splitlines():
            print(line)
        return True
    except FileNotFoundError:
        print(f'Файл с именем = "{file_name}" не найден')

@pytest.fixture # удаление файла
def delete_file():
    file_name = 'New_file.txt'
    try:
        os.remove(f"{dir_path}/{file_name}")
    except OSError as e:
        print(f'Error: {e.filename} - {e.strerror}')
    else:
        print(f'Файл "{file_name}" успешно удалён')
        return True

@pytest.fixture # перемещение по разрешенным директориям
def move_between_directories():
    location = 'New directory'
    move_path = f'{dir_path}/{location}'
    if os.path.isdir(move_path):
        new_path = f'{dir_path}/{location}'
        os.chdir(new_path)
        print(f'Успешный переход в директорию {location}\nТекущий путь: {new_path}')
        return True
    else:
        print(f'Попытка перехода в файл!\n{location} - файл, а не директория')

@pytest.fixture # подъем вверх по директории
def move_up():
    location = 'New directory'
    move_path = f'{dir_path}/{location}'
    if len(dir_path) < len(location):
        up = location.replace('/New directory', '')
        print(f'Успешный переход в директорию {dir_path}\nТекущий путь: {up}')
        return True
    else:
        print('Ошибка доступа!\nНевозможно переместиться выше заданной корневой директории')

@pytest.fixture # переименовывание файла
def rename_file():
    file_name = 'New_file.txt'
    file_to_rename = f'{dir_path}/{file_name}'
    new_name = 'renamed_file.txt'
    try:
        os.rename(file_to_rename, f'{dir_path}/{new_name}')
    except OSError as e:
        print(f'Error: {e.filename} - {e.strerror}')
    else:
        print('Успешное переименование')
        return True

@pytest.fixture # копирование файлов в другую директорию
def copy_files():
    start_directory = f'{dir_path}'
    end_directory = f'{dir_path}/New directory'
    try:
        copy_tree(start_directory, end_directory)
    except OSError as e:
        print(f'Error: {e.filename} - {e.strerror}')
    else:
        print('Успешное копирование')
        return True


@pytest.fixture # перемещение файлов в другую директторию
def move_files():
    start_directory = f'{dir_path}'
    end_directory = f'{dir_path}/New directory'
    try:
        shutil.move(start_directory, end_directory)
    except OSError as e:
        print(f'Error: {e.filename} - {e.strerror}')
    else:
        print('Успешное перемещение')
        return True


def test_create_directory(create_directory):
    assert (create_directory == 1)

def test_delete_directory(delete_directory):
    assert (delete_directory == 1)

def test_create_file(create_file):
    assert (create_file == 1)

def test_overwrite_file(overwrite_file):
    assert (overwrite_file == 1)

def test_read_file(read_file):
    assert (read_file == 1)

def test_delete_file(delete_file):
    assert (delete_file == 1)

def test_rename_file(rename_file):
    assert (rename_file == 1)

def test_move_between_directories(move_between_directories):
    assert (move_between_directories == 1)

def test_move_up(move_up):
    assert (move_up == 1)

def test_copy_files(copy_files):
    assert (copy_files == 1)

def test_move_files(move_files):
    assert (move_files == 1)


