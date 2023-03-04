import pytest
from selenium import webdriver
from wait.wait import Wait
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)




#----------------

@pytest.fixture(scope='class')
def get_driver(request, browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://courses.letskodeit.com/practice')

        get_wait = Wait(driver)
        request.cls.driver = driver
        request.cls.get_wait = get_wait
        yield driver
        driver.close()
    elif browser == 'edge':
         from selenium.webdriver.edge.service import Service
         service = Service(executable_path="C:\\Drivers\\msedgedriver.exe")
         driver = webdriver.Edge()
         driver.get("https://courses.letskodeit.com/practice")

         get_wait = Wait(driver)
         request.cls.driver = driver
         request.cls.get_wait = get_wait
         yield driver
         driver.close()
    elif browser == 'firefox':
        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.firefox.service import Service

        service = Service(executable_path=r'C:\Drivers\geckodriver.exe')
        driver = webdriver.Firefox()
        #driver = webdriver.Firefox(executable_path=r'C:\Drivers\geckodriver.exe')
        driver.get("https://courses.letskodeit.com/practice")

        get_wait = Wait(driver)
        request.cls.driver = driver
        request.cls.get_wait = get_wait
        yield driver
        driver.close()
    else:
        print('Error')



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope='session', autouse=True)
def browser(request):
    return request.config.getoption("--browser")

