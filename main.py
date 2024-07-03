import time
import math
from selenium import webdriver

driver = webdriver.Chrome()

from moduls import *
from data import *


def test_scenario():
    connect(url)  # connect to the site
    authorisation(test_login, test_password)  # authorization
    time.sleep(10)
    click_('выбрать каталог')
    click_('выбрать диалог')
    write_in('поле ввода', 'какой штраф будет за выброшенный окурок в водоохранной зоне?')
    driver.implicitly_wait(10)

    driver.quit()
