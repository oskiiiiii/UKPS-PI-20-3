#для успешного запуска нужно, чтобы на компьютере был установлен chromedriver
#его можно поставить по ссылке https://chromedriver.chromium.org
#также нужно установить библиотеку "selenium"

#импортируем необходимые библиотеки
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


# в переменную path нужно записать рассположение файла chromedriver
global path
path = '/Users/Oskiii/PycharmProjects/Selenium/chromedriver'

#Проверка 1 тест-кейса (Выбор региона на Краснодар)
def test_keys1():

    #открываем chrome и запускаем сайт https://re-store.ru/
    global driver
    driver = webdriver.Chrome(path)
    driver.get("https://re-store.ru/")
    time.sleep(4)

    #находим элемент отвечающий за смену региона и нажимаем на него
    button_region = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/div/div[1]/button')
    button_region.click()
    time.sleep(2)

    #Выбираем "Краснодар" среди регионов и городов
    button_city = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/div[10]/span')
    button_city.click()


#Проверка 2 тест-кейса (сортировка товара по выбору (macbook air))
def test_keys2():

    #открываем chrome и запускаем сайт https://re-store.ru/
    global driver2
    driver2 = webdriver.Chrome(path)
    driver2.get("https://re-store.ru/")
    time.sleep(4)

    #нажимае на "Mac" в панели навигации
    button_mac = driver2.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div/nav/ul[1]/li[1]/a')
    button_mac.click()
    time.sleep(3)

    #нажимаем на чек-бокс "macbook air"
    chechbox_1 = driver2.find_element(By.XPATH, '// *[ @ id = "sticky-parent"] / form / div[2] / div[1] / div / label / span[1]')
    chechbox_1.click()
    time.sleep(1)

    #нажимаем "применить"
    final_button = driver2.find_element(By.XPATH, '// *[ @ id = "submit_filters_btn"]')
    final_button.click()

#Проверка 3 тест-кейса (работа блога)
def test_keys3():

    #открываем chrome и запускаем сайт https://re-store.ru/
    global driver3
    driver3 = webdriver.Chrome(path)
    driver3.get("https://re-store.ru/")
    time.sleep(4)

    #скоролим до блока с блогом
    element = driver3.find_element(By.XPATH, '/html/body/div[2]/div[7]/div/div[2]')
    actions = ActionChains(driver3)
    actions.move_to_element(element).perform()
    time.sleep(1)

    #нажимаем "mac"
    button_mac = driver3.find_element(By.XPATH, '/html/body/div[2]/div[7]/div/h2/div[2]/a[1]')
    button_mac.click()

#Проверка 4 тест-кейса (сравнение товаров)
def test_keys4():

    #открываем chrome и запускаем сайт https://re-store.ru/
    global driver4
    driver4 = webdriver.Chrome(path)
    driver4.get("https://re-store.ru/")
    time.sleep(4)

    #скорллим к ipad
    element = driver4.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[6]/div/a/div/picture/img')
    actions = ActionChains(driver4)
    actions.move_to_element(element).perform()
    time.sleep(1)

    #нажимаем на карточку ipad
    button_ipad = driver4.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/div/a/div/picture /img')
    button_ipad.click()
    time.sleep(4)

    #наводим курсор на ipad mini
    element2 = driver4.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div[9]/a/span[1]/div[2]/img')
    hover = ActionChains(driver4).move_to_element(element2)
    hover.perform()
    time.sleep(1)

    #нажимаем "сравнить"
    sravn = driver4.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div[9]/div/div/div[2]')
    sravn.click()
    time.sleep(6.5)

    #наводим курсор на ipad pro
    element3 = driver4.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div[30]/a/span[1]/div[2]/img')
    hover2 = ActionChains(driver4).move_to_element(element3)
    hover2.perform()
    time.sleep(1)

    #нажимаем "сравнить"
    sravn2 = driver4.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div[30]/div/div[1]/div[2]')
    sravn2.click()
    time.sleep(1)

    #нажимаем на эмблему весов (сравнить)
    sravn_emb = driver4.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/div[2]/a/span')
    sravn_emb.click()

#Проверка 5 тест-кейса (сортировка товара по выбору (macbook mini))
def test_keys5():

    #открываем chrome и запускаем сайт https://re-store.ru/
    global driver5
    driver5 = webdriver.Chrome(path)
    driver5.get("https://re-store.ru/")
    time.sleep(4)

    #нажимаем "MAC" в панели навигации
    button_mac = driver5.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div/nav/ul[1]/li[1]/a')
    button_mac.click()
    time.sleep(3)

    #нажимаем checkbox (mac mini)
    chechbox = driver5.find_element(By.XPATH, '//*[@id="sticky-parent"]/form/div[2]/div[5]/div/label/span[2]')
    chechbox.click()
    time.sleep(1)

    #нажимаем "применить"
    final_button = driver5.find_element(By.XPATH, '//*[@id="submit_filters_btn"]')
    final_button.click()
    time.sleep(1)

#Проверка 6 тест-кейса (Работа всплывающих меню навигационной панели)
def test_keys6():

    #открываем chrome и запускаем сайт https://re-store.ru/
    global driver6
    driver6 = webdriver.Chrome(path)
    driver6.get("https://re-store.ru/")
    time.sleep(4)

    #наводим мышку на "Аксессуары"
    element = driver6.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div/nav/ul[1]/li[5]/a')
    hover = ActionChains(driver6).move_to_element(element)
    hover.perform()
    time.sleep(1)

    #нажимаем "наушники"
    headphones = driver6.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div/nav/ul[1]/li[5]/ul/li[7]/a')
    headphones.click()

#запускаем тест-кейсы
test_keys1()
test_keys2()
test_keys3()
test_keys4()
test_keys5()
test_keys6()