import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Run driver in headless mode.")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        if not request.config.getoption("--headless"):
            print("\nstart chrome browser for test..")
            options = ChromeOptions()
            options.add_argument("--window-size=1280,720")
            driver = webdriver.Chrome(options=options)
        else:
            print("\nstart chrome browser for test..")
            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--window-size=1280,720")
            driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        if not request.config.getoption("--headless"):
            print("\nstart firefox browser for test..")
            options = FirefoxOptions()
            options.add_argument("--window-size=1280,720")
            driver = webdriver.Firefox(options=options)
        else:
            print("\nstart firefox browser for test..")
            options = FirefoxOptions()
            options.add_argument("--headless")
            options.add_argument("--window-size=1280,720")
            driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()

# запуск тестов
# pytest -rx -v test_change_password_page.py
# pytest -rx -v
# pytest -s -v test_main_page.py
# pytest -s -v test_basket_page.py --headless
# pytest -s -v --browser_name=chrome --headless
# pytest -s -v --browser_name=firefox
# pytest -s -v --browser_name=chrome
# pytest -s -v --headless
# pytest -s -v --browser_name=firefox test_product_page.py




