from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from Config.config import TestData
from Pages.BasePage import BasePage
import pyautogui


class BasketPage(BasePage):



    def __init__(self, driver):
        super().__init__(driver)

    """This is used check basket list items and return activity time and activity name"""
    def basket(self):
        action = webdriver.ActionChains(self.driver)
        bet_list_items_on_basket = self.driver.find_elements(By.XPATH, './/span[@class = "overflow-ellipsis match"]')

        action.move_to_element(bet_list_items_on_basket[0])
        action.perform()
        time.sleep(2)
        pyautogui.screenshot(r'{}BasketDetails.png'.format(TestData.screenshot_base_directory))


        activity_time_on_bet_basket = self.driver.find_elements(By.XPATH,'//*[@id="loaded-ticket"]/div/div[1]/div')
        activity_time_on_bet_basket_event = activity_time_on_bet_basket[0].find_element(By.XPATH,'//*[@id="loaded-ticket"]/div/div[1]/div/span[2]')

        activity_time_text= activity_time_on_bet_basket_event.get_attribute('textContent')
        print("Activity time : " + activity_time_text)

        print("Activity name : " + bet_list_items_on_basket[0].text)
        bet_activity_name = bet_list_items_on_basket[0].text
        basket_item_details=[bet_activity_name, activity_time_text]

        return basket_item_details

