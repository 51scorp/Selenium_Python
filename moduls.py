from main import driver
from selenium.webdriver.common.by import By


def connect(url):
    driver.get(url)
    driver.implicitly_wait(10)


def click_(press_the_button):
    driver.find_element(By.XPATH, press_the_button).click()
    driver.implicitly_wait(10)


def write_in(where_change, send_keys):
    element = driver.find_element(By.XPATH, where_change)
    element.clear()
    driver.implicitly_wait(10)
    element.send_keys(send_keys)
    driver.implicitly_wait(10)


def check_success(what_search, where_search):
    element = driver.find_element(By.XPATH, where_search)
    info = element.text
    return what_search in info


def authorisation(login, password):
    write_in("путь к полю логина", login)  # Пользователь
    write_in("путь к полю пароля", password)  # Пароль
    click_("путь к \"войти\"")
    driver.implicitly_wait(10)
