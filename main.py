url = 'https://market.yandex.ru'


def test_add_to_cart(driver):
    connect(url, driver)


def connect(url, driver):
    driver.get(url)
    driver.maximize_window()  # maximize the window
    driver.implicitly_wait(10)
