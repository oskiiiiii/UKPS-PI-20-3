# Лабораторная работа №2. Тестирование файлового менеджера

### Цель лабораторной работы
Научиться тестировать проекты с помощью юнит-тестов.

### Предусловия: 
Созданный примитивный файловый менеджер.
Программа должна работать в определенной папке (рабочей папки менеджера) и позволять пользователю выполнять следующие простые действия в пределах рабочей папки:

1. Создание папки (с указанием имени); 
2. Удаление папки по имени; 
3. Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх; 
4. Создание пустых файлов с указанием имени; 
5. Запись текста в файл; 
6. Просмотр содержимого текстового файла; 
7. Удаление файлов по имени; 
8. Копирование файлов из одной папки в другую; 
9. Перемещение файлов; 
10. Переименование файлов.

### Задание: 
Необходимо написать тесты, которые проверяют работу файлового менеджера.
Покрытия тестами составляет от 80%. 

### Демонстрация работы тестов
1. создание директории: 

![Снимок экрана 2021-12-21 в 09 57 06](https://user-images.githubusercontent.com/72342708/146885564-3b75ce09-d8f9-45b8-bb25-354810dde28f.png)

вывод результата теста: 

![Снимок экрана 2021-12-21 в 09 58 41](https://user-images.githubusercontent.com/72342708/146885749-0b603b3c-89b0-4670-8abf-31d2a5720f05.png)

повторное проведение теста выдает ошибку, так как подобная директория уже существует в нашей рабочей директории: 

![Снимок экрана 2021-12-21 в 09 59 54](https://user-images.githubusercontent.com/72342708/146885901-5bca6239-69d1-46fa-ab10-33512df28eaa.png)

результат выполнения функции (создалась новая директория 'new directory': 

![Снимок экрана 2021-12-21 в 10 20 46](https://user-images.githubusercontent.com/72342708/146888086-6df069c6-459d-47e2-b82d-def622177078.png)
 
2. создание файла: 

![Снимок экрана 2021-12-21 в 10 28 47](https://user-images.githubusercontent.com/72342708/146889086-caadf00d-eb38-4164-a219-70dc6d22027c.png)

вывод результата теста: 

![Снимок экрана 2021-12-21 в 10 29 22](https://user-images.githubusercontent.com/72342708/146889169-f043ca45-b606-4e09-9c8f-b529e21809d3.png)

проведение повторного теста: 

![Снимок экрана 2021-12-21 в 10 30 03](https://user-images.githubusercontent.com/72342708/146889242-a691a1f2-6016-420c-a70d-f093be5f5dd5.png)

наглядный результат выполнения (создался новый файл 'new_file.txt'): 

![Снимок экрана 2021-12-21 в 10 30 41](https://user-images.githubusercontent.com/72342708/146889312-6a12894b-8b63-49d9-8ec1-2dbed6d750b3.png)

3. запись в файл: 

![Снимок экрана 2021-12-21 в 10 46 45](https://user-images.githubusercontent.com/72342708/146891312-b0020f0e-48f4-4906-94ed-46917cf52030.png)

вывод результата теста: 

![Снимок экрана 2021-12-21 в 10 47 30](https://user-images.githubusercontent.com/72342708/146891407-d558e67d-af44-475e-9ad7-9c7aa08e6275.png)

4. чтение файла:

![Снимок экрана 2021-12-21 в 10 50 05](https://user-images.githubusercontent.com/72342708/146891727-0618757f-bfcc-4934-92bb-a2716f6c54ea.png)

вывод результата теста: 

![Снимок экрана 2021-12-21 в 10 50 58](https://user-images.githubusercontent.com/72342708/146891864-fa6671ef-4518-4f4c-b3c8-eea3cce999bf.png)

Вызовы тестов происходят через функции и метод assert: 

![Снимок экрана 2021-12-21 в 10 54 13](https://user-images.githubusercontent.com/72342708/146892256-e296581b-f8fe-4cb6-b368-f665ea838dc0.png)

Все остальные тесты проводятся аналогично. Полнотый файл с кодом представлен у меня на гитхабе.
Скриншоты остальных пройденных тестов:

5. удаление директории:

![Снимок экрана 2021-12-21 в 11 21 42](https://user-images.githubusercontent.com/72342708/146895941-b49e18f4-4b37-4b44-91e6-c2ee8473e21e.png) 
![Снимок экрана 2021-12-21 в 11 19 46](https://user-images.githubusercontent.com/72342708/146895605-5355e252-71c8-432b-8a89-edfdb59d381d.png)

7. удаление файла: 

![Снимок экрана 2021-12-21 в 11 25 13](https://user-images.githubusercontent.com/72342708/146896482-00d7f367-2c0b-4f85-b064-77cddf2ef120.png) 
![Снимок экрана 2021-12-21 в 11 24 42](https://user-images.githubusercontent.com/72342708/146896401-a7c230ae-4fa1-449a-9fa3-cdb29690aab9.png)

8. перемещение между директориями (переходим в созданую директорию 'new directory'): 

![Снимок экрана 2021-12-21 в 12 26 24](https://user-images.githubusercontent.com/72342708/146905403-f18c4de9-d7dc-495a-8e4d-ca6db7ae4179.png)
![Снимок экрана 2021-12-21 в 12 24 32](https://user-images.githubusercontent.com/72342708/146905144-6d0c2a78-d981-4703-81ad-6f72b735f8bb.png) 

9. подъем в корневую директорию: 

![Снимок экрана 2021-12-21 в 12 51 35](https://user-images.githubusercontent.com/72342708/146909306-0371ce3f-5987-407c-bebd-b1a09b8ffad1.png) 
![Снимок экрана 2021-12-21 в 12 48 40](https://user-images.githubusercontent.com/72342708/146908904-1fa2f037-2fad-439c-a385-931a642aa97e.png)

10. переименование файла: 

![Снимок экрана 2021-12-21 в 12 57 41](https://user-images.githubusercontent.com/72342708/146910230-b9fb3ae1-c7cd-43ba-908b-f3fe06a35a82.png) 
![Снимок экрана 2021-12-21 в 12 56 33](https://user-images.githubusercontent.com/72342708/146910054-b2d0dfd3-c23f-4672-a7f7-965721b832c5.png)

11. копирование файлов из директории в директорию: 

![Снимок экрана 2021-12-21 в 13 05 48](https://user-images.githubusercontent.com/72342708/146911423-3b033bec-dc9d-4334-baa8-c4a48941a222.png) 
![Снимок экрана 2021-12-21 в 13 04 34](https://user-images.githubusercontent.com/72342708/146911271-4f0a7eb2-af07-49e4-9fee-7a51713dac45.png)

12. перемещение файлов из директории в директорию: 

![Снимок экрана 2021-12-21 в 13 06 54](https://user-images.githubusercontent.com/72342708/146911570-7592b3c2-73ed-4806-b2a4-4c5168d359db.png)


