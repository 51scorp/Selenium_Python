import time
import math
from selenium import webdriver
from data import *

driver = webdriver.Chrome()
from moduls import *


def test_scenario():
    what_search = 'какой ответ мы должны получить?'  # passing criterion
    what_check = 'какой штраф будет за выброшенный окурок в водоохранной зоне?'  # test phrase
    where_search = 'где искать ответ?'  # where to search answer
    connect(url)  # connect to the site
    authorisation(test_login, test_password)  # authorization
    click_('выбрать каталог')
    click_('выбрать диалог')
    write_in('поле ввода', what_check)
    click_("отправить вопрос")
    driver.implicitly_wait(10)
    assert check_success(what_search, where_search) is True

    driver.quit()
