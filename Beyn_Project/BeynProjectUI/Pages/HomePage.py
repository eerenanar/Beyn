from selenium.webdriver.common.by import By


from Config.config import TestData
#from Driver.DriverManager import driver
from Pages.BasePage import BasePage


class HomePage(BasePage):

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.url)

    """page actions for home page"""
    sports_btn = (By.XPATH, "//a[contains(text(),'Sport')]")
    """this used to click sport button"""
    def click_sport(self):
        self.do_click(self.sports_btn)
