import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait


def login(username, password,driver):
    # инициализируем драйвер


    # открываем страницу авторизации
    driver.get('https://www.copart.com/login/')
    time.sleep(4)
    # находим кнопку "Consent" и кликаем на нее
    consent_button = driver.find_element(By.CSS_SELECTOR, 'p.fc-button-label')
    consent_button.click()
    try:
        # находим поле для ввода логина и вводим логин
        username_input = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
        username_input.send_keys(username)
        # находим поле для ввода пароля и вводим пароль
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password_input.send_keys(password)
    except Exception as ex:
        return f"[ERROR]: {ex}"

    # нажимаем клавишу Enter в поле для ввода пароля, чтобы отправить форму
    password_input.send_keys(Keys.RETURN)

    # находим кнопку "закрыть" и кликаем на нее
    try:
        consent_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-white')
        consent_button.click()
    except:
        pass

    # ждем, пока страница загрузится после авторизации
    driver.implicitly_wait(10)
    get_content(driver)

def get_content(driver):
    driver.get('https://www.copart.com/public/quickPickSearch/VEHICLE_FINDER/FETI/buyitnow/?displayStr=Buy%20It%20Now&from=%2FvehicleFinder')
    driver.implicitly_wait(5)
    # находим все товары на странице и выводим их названия
    products = driver.find_elements(By.CSS_SELECTOR, 'a.search-results')
    with open('links.txt', 'w') as f:
        for product in products:
            link = product.get_attribute('href')
            f.write(link + '\n')
            print(link)



def get_content_from_link(driver):
    with open('links.txt', 'r') as f:
        links = f.readlines()

    for link in links:
        link = link.strip()  # удаляем лишние символы

        driver.get(str(link))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.title')))
        title = driver.find_element(By.CSS_SELECTOR, 'h1.title').text

        results_dict = {
        'site_name': '',
        'title': title,
        'number_lot':"" ,
        'vin': '',
        'vacancy_url': link,
        'Odometr': '',
        'main': 'runanddrive',
        'main_damage': '',
        'second_damage': '',
        'price': '',
        'engine': '',
        'akpp': '',
        'place_sale': '',
        'time_of_sale': '',
        }
        print(results_dict)





def main():
    driver = webdriver.Chrome()
    login('Valebtinbest@gmail.com', 'Plaalen18',driver)
    get_content_from_link(driver)



if __name__ == "__main__":
    main()