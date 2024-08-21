import time
from selenium import webdriver

from data import *

driver = webdriver.Chrome()
from moduls import *


def test_add_to_cart():
    connect(url)  # connect to the site
    driver.close()
