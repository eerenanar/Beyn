import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    if request.param == 'chrome':
        web_driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        """If faced a fail installing driver ,can use dirctly driver path"""
        #web_driver= webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    request.cls.driver=web_driver
    web_driver.implicitly_wait(10)
    web_driver.maximize_window()
    yield
    web_driver.close()