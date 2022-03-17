from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from selenium import webdriver
import time
import pyautogui
from Config.config import TestData

class SportPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    """page actions for home page"""
    search_area = (By.ID, "nvscoreSearchWidgetSearchInput")
    searh_results_item = (By.CSS_SELECTOR, ".active > .sport-container .result-row:nth-child(1) > .event-info > span:nth-child(1)")

    def sport(self):
        action = webdriver.ActionChains(self.driver)
        bet_list_items_on_basket = self.driver.find_element(By.CSS_SELECTOR, ".active > .sport-container .result-row:nth-child(1) > .event-info > span:nth-child(1)")

        action.move_to_element(bet_list_items_on_basket)
        action.perform()
        time.sleep(2)
        pyautogui.screenshot(r'{}SelectItemDetails.png'.format(TestData.screenshot_base_directory))

    """this used to click search area"""
    def click_search_area(self):
        self.do_click(self.search_area)
    """this used to click item on search result"""
    def click_search_result_item(self):
        self.do_click(self.searh_results_item)

