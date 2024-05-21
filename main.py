from selenium import webdriver
import time


def test_authorization():
    driver = webdriver.Firefox()
    driver.get('https://www.avito.ru/')
    driver.implicitly_wait(1)
    driver.find_element('xpath', "/html/body/div[1]/div/div[3]/div/div/div/a").click()
    find_enter.click()

    driver.quit()
