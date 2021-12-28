# Лабораторная работа №3. 

Методические указание:
    IDE: VS Code, Pycharm, Replit
    Язык: Python
    Библиотека Requests
    Фрейворк: Pytest
Задание:
1. Зарегистрироваться: https://petfriends1.herokuapp.com
2. Ознакомиться с документацией API: https://petfriends1.herokuapp.com/apidocs/#/
3. Написать приложение содержащие функции работы с API, реализовать методы:
   - GET, 
   - POST, 
   - PUT, 
   - DELETE
4. Написать тесты для функций работы с API:
   - Тесты должны содержать позитивные и негативные сценарии 
   - Необходимо сделать параметризацию 
   - Необходимо использовать фикстуры 
5. Запустить  тесты и сделать скриншот
6. Создаем файл README.md, с описанием приложения
7. Загружаем файлы на Github

Отчет о выполнении 3 практики
------

1. Изучаем методы API на сайте Flasgger. 

![Снимок экрана 2021-12-21 в 13 38 30](https://user-images.githubusercontent.com/72342708/146916186-570bdf15-9560-47ea-ad5f-f33da85779a1.png)

2. Пройдёмся по работе каждой функции. 
    1. POST (new, выкладываем новое животное с фотогрфией)
    
    ![Снимок экрана 2021-12-21 в 14 54 04](https://user-images.githubusercontent.com/72342708/146925975-8dcb1a6f-2f6e-408d-8018-c4e044e6a3fd.png)

    Результат работы: 
    
    ![Снимок экрана 2021-12-21 в 14 55 09](https://user-images.githubusercontent.com/72342708/146926070-6acfa9e5-2513-4be9-b0b9-86ae1acfcea0.png)

    2. GET (получаем список наших животных)

    ![Снимок экрана 2021-12-21 в 14 56 23](https://user-images.githubusercontent.com/72342708/146926196-3601eede-a620-41dc-b93e-8a5e02717cf7.png)

    Результат работы: 

    ![Снимок экрана 2021-12-21 в 14 57 46](https://user-images.githubusercontent.com/72342708/146926332-da512d10-b635-4677-9e98-c4781088321b.png)
    ![Снимок экрана 2021-12-21 в 14 58 09](https://user-images.githubusercontent.com/72342708/146926375-ecf30a30-c200-4e75-82c1-21c7162899b1.png)

    3. DELETE (удаляем животное)

    ![Снимок экрана 2021-12-21 в 15 01 20](https://user-images.githubusercontent.com/72342708/146926708-60643297-0081-4682-9f56-6b4e8c58dacc.png)

    Результат работы: 

    ![Снимок экрана 2021-12-21 в 15 00 06](https://user-images.githubusercontent.com/72342708/146926585-30d6d952-d13c-42f8-8814-1750fc466a3e.png)

    4. POST (выкладываем фото животного)

    ![Снимок экрана 2021-12-21 в 15 03 24](https://user-images.githubusercontent.com/72342708/146926950-70b4cd89-1161-40e8-9820-d8182f2fd2a0.png)

    Результат работы: 

    ![Снимок экрана 2021-12-21 в 15 04 17](https://user-images.githubusercontent.com/72342708/146927062-50bfabeb-6369-4d7c-9d12-ed704319d866.png)

    5. POST (simple, выкладываем новое животное без фотографии)

    ![Снимок экрана 2021-12-21 в 15 06 28](https://user-images.githubusercontent.com/72342708/146927324-bea9ef67-8cd5-491f-b913-969312c79e89.png)

    Результат работы: 

    ![Снимок экрана 2021-12-21 в 15 07 24](https://user-images.githubusercontent.com/72342708/146927472-f4484dac-d36e-496a-9dc3-49d4648daa47.png)

3. После реализации каждой функции началась тестировка с помощью библиотеки pytest. Во время реализации использовались фикстуры. 

![Снимок экрана 2021-12-21 в 15 10 18](https://user-images.githubusercontent.com/72342708/146927827-d9f4a7e0-638c-4fe8-883c-7dd5d679db70.png)