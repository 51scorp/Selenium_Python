import pytest
import math
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import *

list_sites = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


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
    step = re.search(r'(\d+)', link)
    driver.get(link)
    # driver.maximize_window()  # maximize the window
    driver.save_screenshot(f"./screenshots/{step}.png")
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "ember459").click()
    driver.find_element(By.ID, "id_login_email").send_keys(login)
    driver.find_element(By.ID, "id_login_password").send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login_form"]/button').click()
    time.sleep(4)
    input_field = driver.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div/div[2]/div['
                                                '1]/div/article/div/div/div[2]/div/section/div/div[1]/div['
                                                '2]/div/div/div/textarea')
    input_field.clear()
    answer = math.log(int(time.time()))
    input_field.send_keys(str(answer))
    driver.find_element(By.CLASS_NAME, 'submit-submission').click()
    # time.sleep(2)
