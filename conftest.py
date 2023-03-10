import pytest
from selenium import webdriver
from wait.wait import Wait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope='class', autouse=True)
def get_driver(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        service = Service(executable_path="C:\\Drivers\\msedgedriver.exe")
        driver = webdriver.Edge()
    elif browser == 'firefox':
        service = Service(executable_path=r'C:\Drivers\geckodriver.exe')
        driver = webdriver.Firefox()
    else:
        print('Error')

    get_wait = Wait(driver)
    driver.get(url)
    request.cls.driver = driver
    request.cls.get_wait = get_wait
    # yield driver
    # driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption('--url')


