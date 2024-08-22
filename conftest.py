import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import *


@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-first-run")
    options.add_argument('--disable-search-engine-choice-screen')
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.mark.parametrize('version', list_sites)
def test_guest_should_see_login_link(driver, version):
    link = f'{version}'
    driver.get(link)
    driver.maximize_window()  # maximize the window
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "ember459").click()
    driver.find_element(By.ID, "id_login_email").send_keys(login)
    driver.find_element(By.ID, "id_login_password").send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login_form"]/button').click()
    driver.implicitly_wait(10)
    input_field = driver.find_element(By.ID, "ember509")
    input_field.clear()
    answer = math.log(int(time.time()))
    input_field.send_keys(str(answer))
    driver.find_element(By.XPATH, '//*[@id="ember501"]/div/section/div/div[1]/div[4]/button')
    time.sleep(10)

