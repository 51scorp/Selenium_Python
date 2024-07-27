import time
from selenium import webdriver

from data import *

driver = webdriver.Chrome()
from moduls import *


def test_add_to_cart():
    connect(url)  # connect to the site
    authorisation(test_login, test_password)  # authorisation to the site
    clear_cart()  # empty the cart before testing
    write_in('/html/body/div[1]/div/div[2]/div[2]/div/header/div['
             '1]/div/div/div/div/div/div/form/div/div/div/div/div/input[1]', what_search)  # what search
    click_('/html/body/div[1]/div/div[2]/div[2]/div/header/div[1'
           ']/div/div/div/div/div/div/form/div[1]/button')  # click search
    click_('/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[5]/div/div/div/div/div/div/div/div['
           '3]/div/div/div/div[1]/div/div/noindex/div/button[2]')  # sort cheaper
    click_('/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[5]/div/div/div/div/div/aside/div/div['
           '3]/div/div/div/div/div[4]/div/fieldset/div/div/div[2]/div[1]/div/div/div[1]/label/span')  # select 8 GB RAM
    driver.refresh()  # refresh page
    time.sleep(2)  # wait download page
    click_first_match('_1TRiI')  # add to cart first product found
    click_('/html/body/div[1]/div/div[2]/div[2]/div/header/div[1]'
           '/div/div/noindex[2]/nav/ul/li[4]/div/div/div/a')  # goCart
    time.sleep(2)  # wait download page
    driver.save_screenshot("./screenshots/add_to_cart.png")

    driver.close()
