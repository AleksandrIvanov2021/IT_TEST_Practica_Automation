import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
            options = Options()
            options.add_argument("--window-size=1280,720")
            driver = webdriver.Chrome(options=options)
        else:
            print("\nstart chrome browser for test..")
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--window-size=1280,720")
            driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()









