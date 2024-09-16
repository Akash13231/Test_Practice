


import pytest
from selenium import webdriver

#from selenium import webdriver
driver = None

def pytest_addoption(parser):   # this code is defined to take browser option from user
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        driver = webdriver.Chrome()

    elif browser_name == 'edge':
        driver = webdriver.Edge()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()
