import time
import math
from selenium import webdriver
from data import *

driver = webdriver.Chrome()
from moduls import *


def test_scenario():
    connect(url)  # connect to the site
    click_('/html/body/div/div/div[2]/div[2]/section/div[2]/button') # click authorisation
    click_('/html/body/div/div/div[2]/div[2]/section/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[4]/button[1]')
    authorisation(test_login, test_password)
    driver.switch_to.window(driver.window_handles[0]) # Пока что, всё останавливается на этом этапе
    click_('/html/body/div/div/div[2]/div[2]/section/div[2]/div/div[2]/div/div/div[1]/button/svg') # закрыть окно авторизации
    click_('/html/body/div/div/div[2]/div[4]/section/div/span[1]/div/div/div/span[3]/div/div/button[3]/svg') # раскрываем список chat
    click_('/html/body/div/div/div[2]/div[4]/section/div/span[1]/div/div/div/span[3]/div/div[2]/div/div[1]/div[1]/div[2]/button') # try it
    write_in('/html/body/div/div/div[2]/div[4]/section/div/span[1]/div/div/div/span[3]/div/div[2]/div/div[1]/div['
             '2]/div/table/tbody/tr[1]/td[2]/input', '1')
    write_in('/html/body/div/div/div[2]/div[4]/section/div/span[1]/div/div/div/span[3]/div/div[2]/div/div[1]/div['
             '3]/div[2]/div/div/div/textarea', 'тут надо вставить переменную с json')
    driver.implicitly_wait(10)
    # assert check_success(what_search, where_search) is True # Тут будет проверка, что тест прошёл успешно.

    driver.close() # close the browser


