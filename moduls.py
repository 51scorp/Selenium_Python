from selenium.common.exceptions import NoSuchElementException
from main import driver
from selenium.webdriver.common.by import By


def connect(url):
    driver.get(url)
    driver.maximize_window()  # maximize the window
    driver.implicitly_wait(10)


def click_(press_the_button):
    driver.find_element(By.XPATH, press_the_button).click()
    driver.implicitly_wait(10)


def click_first_match(class_name):
    driver.find_element(By.CLASS_NAME, class_name).click()
    driver.implicitly_wait(10)


def write_in(where_change, send_keys):
    element = driver.find_element(By.XPATH, where_change)
    element.clear()
    driver.implicitly_wait(10)
    element.send_keys(send_keys)


def authorisation(login, password):
    click_(
        '/html/body/div[1]/div/div[2]/div[2]/div/header/div[1]/div/div/noindex[2]/nav/ul/li[5]/div/div/div/div/div/a')
    write_in('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div['
             '2]/div/div/span/input', login)  # идентификация
    click_(
        '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/button')  # Войти
    write_in('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div/div[2]/div[2]/div[1]/span/input',
             password)  # аутентификация
    click_('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div/div[3]/div[1]/button')  # продолжить
    driver.implicitly_wait(30)  # Ожидание авторизации


def clear_cart():
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div/div[2]/div[2]/div/header/div[1]/div/div/noindex[2]/nav/ul/li['
                        '4]/div/div/div/a').click()  # goCart
    driver.implicitly_wait(5)
    try:
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div[3]/div/div/div/div/main/div[2]/div/div[2]/div['
                            '1]/div/div/div/ul/li/div/div/div/div[1]/div/div/div/div[2]/div[2]').click()  # clear Cart
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div[3]/div/div/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/ul/'
                            'li/div/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]'
                            '/div/div[2]/button[2]').click()  # confirm clear
        driver.implicitly_wait(5)
    except NoSuchElementException:
        pass
    finally:
        driver.back()
