import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function", autouse=True)
def driver():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-first-run")
    options.add_argument('--disable-search-engine-choice-screen')
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit browser..")
    driver.quit()
