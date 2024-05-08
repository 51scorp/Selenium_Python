from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.avito.ru/')
time.sleep(15)
driver.quit()
