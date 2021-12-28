import os # модуль содержит функции для работы с операционной системой
import shutil # модуль содержит функции для обработки файлов, групп файлов и папок
from tabulate import tabulate # модуль для красивого отображения табличных данных
from distutils.dir_util import copy_tree # модуль предоставляет функции для работы с деревом каталогов и каталогами


class FileManager:
    def __init__(self):
        with open('working_directory.txt', mode = 'r') as f: # открываем файл с working_directory.txt в режиме для чтения
            self.root_directory = fr'{f.readline()}'  # рабочая директория
        os.chdir(self.root_directory)  # меняем рабочий каталог программы
        # фиксируем изначальную длину рабочей директории для безопасного перемещения вверх (с помощью функции move_up)
        self.path_length = len(self.root_directory.split('/'))
        self.display_data = []
        self.allowed_files = self.list_directory()[1]  # задаем объекты в разрешенной для изменения директории

    def create_directory(self): # создание директории
        directory_name = str(input('Название новой директории: '))
        if not os.path.exists(f'{self.root_directory}/{directory_name}'): # проверяем на наличие директории в корневой папке
            os.makedirs(f'{self.root_directory}/{directory_name}') # создание новой директории в корневой папке
            print(f'Директория "{directory_name}" успешно создана')
            self.refresh_directory()
        else:
            print('Директория уже существует')

    def create_file(self): # создание файла
        file_name = str(input('Имя файла: '))
        if not os.path.exists(f'{self.root_directory}/{file_name}'): # проверка на наличие файла в корневой директории
            new_file = open(f'{self.root_directory}/{file_name}', 'w') # создаем новый файл и открываем его для записи
            # new_file.write(str(input('Введите текст для записи в файл: ')))
            new_file.close()
            print(f'Файл "{file_name}" успешно создан')
            self.refresh_directory()
        else:
            print('Файл с таким названием уже существует')

    def overwrite_file(self): # запись в файл
        file_id = int(input('Введите ID файла для записи: '))
        location = self.id_choice(file_id)
        try:
            with open(f'{self.root_directory}/{location}', mode='w') as f:
                f.write(str(input('Введите текст для записи в файл: ')))
        except FileNotFoundError:
            print(f'Файл с  ID = "{file_id}" не найден')
        except IsADirectoryError:
            print('Это директория')
        else:
            print('Текст успешно записан в файл')

    def read_file(self): # чтение файла
        file_id = int(input('Введите ID файла чтобы прочитать: '))
        file_name = self.id_choice(file_id)
        try:
            file_location = f'{self.root_directory}/{file_name}'
            with open(file_location, 'r') as f:
                text = f.read()
            for line in text.splitlines():
                print(line)
        except FileNotFoundError:
            print(f'Файл с ID = "{file_id}" не найден')

    def delete_directory(self): # удаление директории
        directory_id = int(input('Введите ID директории чтобы удалить: '))
        directory_name = self.id_choice(directory_id)
        try:
            shutil.rmtree(f'{self.root_directory}/{directory_name}')  # удаляем директорию и все файлы в ней
        except OSError as e:
            print(f'Error: {e.filename} - {e.strerror}')
        else:
            print(f'Директория "{directory_name}" успешно удалена')
            self.refresh_directory()

    def delete_file(self): # удаление файла
        file_id = int(input('Введите ID файла чтобы удалить: '))
        file_name = self.id_choice(file_id)
        try:
            os.remove(f"{self.root_directory}/{file_name}")
        except OSError as e:
            print(f'Error: {e.filename} - {e.strerror}')
        else:
            print(f'Файл "{file_name}" успешно удалён')
            self.refresh_directory()

    def move_between_directories(self):  # перемещение по разрешенным директориям
        chosen_directory = int(input('Введите ID директории чтобы переместиться: '))
        location = self.id_choice(chosen_directory)
        move_path = self.root_directory + f'/{location}'
        if os.path.isdir(move_path):
            self.root_directory += f'/{location}'
            os.chdir(self.root_directory)
            self.refresh_directory()
            print(f'Успешный переход в директорию {location}\nТекущий путь: {self.root_directory}')
        else:
            print(f'Попытка перехода в файл!\n{location} - файл, а не директория')

    def move_up(self):  # подъем вверх по директории
        location = self.root_directory.split('/')
        if self.path_length < len(location):
            location.pop()
            up = '/'.join(location)
            self.root_directory = up
            os.chdir(self.root_directory)
            self.refresh_directory()
            print(f'Успешный переход в директорию {location[-1]}\nТекущий путь: {self.root_directory}')
        else:
            print('Ошибка доступа!\nНевозможно переместиться выше заданной корневой директории')

    def rename_file(self): # переименовывание файла
        file_id = int(input('Введите ID файла, чтобы переименовать: '))
        file_to_rename = f"{self.root_directory}/{self.id_choice(file_id)}"
        new_name = str(input('Введите новое название файла: '))
        try:
            os.rename(file_to_rename, f'{self.root_directory}/{new_name}')
        except OSError as e:
            print(f'Error: {e.filename} - {e.strerror}')
        else:
            print('Успешное переименование')
            self.refresh_directory()

    def copy_files(self): # копирование файлов
        start_id = int(input('ID директории из который производится копирование: '))
        start_directory = f"{self.root_directory}/{self.id_choice(start_id)}"
        end_id = int(input('ID директории чтобы скопировать в неё: '))
        end_directory = f"{self.root_directory}/{self.id_choice(end_id)}"
        try:
            copy_tree(start_directory, end_directory)
        except OSError as e:
            print(f'Error: {e.filename} - {e.strerror}')
        else:
            print('Успешное копирование')

    def move_files(self): # перемещение файлов
        self.list_directory()
        start_id = int(input('ID Файла для перемещения: '))
        start_location = f"{self.root_directory}/{self.id_choice(start_id)}"
        end_id = int(input('ID директории куда переместить: '))
        end_directory = f"{self.root_directory}/{self.id_choice(end_id)}"
        try:
            shutil.move(start_location, end_directory)
        except OSError as e:
            print(f'Error: {e.filename} - {e.strerror}')
        else:
            print('Успешное перемещение')

    def create_archive(self):  # создание zip-архива
        file_id = int(input('Введите ID файла или директории для создания zip-архива: '))
        location = self.id_choice(file_id)
        try:
            archive = shutil.make_archive(
                base_name=str(input('Введите новое название архива: ')), base_dir=location, format='zip')
            print(f"zip-архив {archive} создан")
        except FileNotFoundError as err:
            print(err)

    def extract_archive(self):  # извлечение файлов из zip-архива
        file_id = int(input('Введите ID файла архива для разархивации zip-архива: '))
        location = self.id_choice(file_id)
        try:
            shutil.unpack_archive(location, format='zip')
        except shutil.ReadError as err:
            print(err)

    def refresh_directory(self): # обновление директории
        self.allowed_files = self.list_directory()[1]

    def list_directory(self): # вывод директорий
        self.display_data = []
        files = os.scandir(path=self.root_directory)
        file_id = 1
        for each in files:
            object_data = f' - Directory - {each.name} - {file_id}' if each.is_dir() else f' - File - {each.name} - {file_id}'
            object_info = object_data.split(' - ')
            object_info.pop(0)
            self.display_data.append(object_info)
            file_id += 1
        data = tabulate((i for i in self.display_data), headers=['Type', 'Name', 'ID'], tablefmt='pipe',
                        stralign='center')
        return data, self.display_data

    def id_choice(self, object_id):  # получение имени файла по его ID
        ids = [i[2] for i in self.allowed_files]
        names = [i[1] for i in self.allowed_files]
        if str(object_id) in ids:
            return names[object_id - 1]

    def CLI(self):
        print(f'{"-"*15}Файловый менеджер{"-"*15}\n')
        # создание словаря с командами
        commands = [['1', 'Просмотр директории'], ['2', 'Создать папку'], ['3', 'Удалить папку'],
                    ['4', 'Переход между директориями'], ['5', 'Создать пустой файл'], ['6', 'Запись текста в файл'],
                    ['7', 'Просмотр текстового файла'], ['8', 'Удалить файл'], ['9', 'Копирование из папки в папку'],
                    ['10', 'Перемещение файлов'], ['11', 'Переименовать файл'], ['12', 'Архивировать файл/директорию'],
                    ['13', 'Разархивировать файл/директорию'], ['14', 'Подняться вверх по директории (cd ..)']]
        help_page = tabulate((i for i in commands), headers=['ID', 'Метод'], tablefmt='github', stralign='center')
        print(help_page + f'\n\nРабочая директория настроена: {self.root_directory}')
        while True:
            choose = str(input(
                '\nhelp - список команд, exit - выйти из файлового менеджера\nВведите ID команды чтобы продолжить: '))
            print('\n')
            if choose == '1':
                print(self.list_directory()[0])
            if choose == '2':
                self.create_directory()
            if choose == '3':
                self.delete_directory()
            if choose == '4':
                self.move_between_directories()
            if choose == '5':
                self.create_file()
            if choose == '6':
                self.overwrite_file()
            if choose == '7':
                self.read_file()
            if choose == '8':
                self.delete_file()
            if choose == '9':
                self.copy_files()
            if choose == '10':
                self.move_files()
            if choose == '11':
                self.rename_file()
            if choose == '12':
                self.create_archive()
            if choose == '13':
                self.extract_archive()
            if choose == '14':
                self.move_up()
            if choose.lower() == 'help':
                print(f'\n{help_page}')
            if choose.lower() == 'exit':
                exit()


def main():
    manager = FileManager()
    manager.CLI()


if __name__ == '__main__':
    main()