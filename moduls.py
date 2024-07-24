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


def else_flutter():  # если сайт написан на флаттер, нужно запустить скрипт
    driver.execute_script("document.querySelector('flt-glass-pane').shadowRoot.querySelector("
                          "'flt-semantics-placeholder').click();")

# def authorisation(login, password):
#     driver.switch_to.window(driver.window_handles[-1])
#     write_in('/html/body/div/div[2]/div/div/div[1]/div[1]/form/div[1]/input', login)  # Пользователь
#     write_in('/html/body/div/div[2]/div/div/div[1]/div[1]/form/div[2]/input', password)  # Пароль
#     click_('/html/body/div/div[2]/div/div/div[1]/div[1]/form/div[4]/input[2]')
#     driver.implicitly_wait(10)
