from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://www.avito.ru/')
time.sleep(5)
driver.quit()
