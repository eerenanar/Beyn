import pytest

from Config.config import TestData
from Pages.BasketPage import BasketPage
from Pages.HomePage import HomePage
from Pages.SportPage import SportPage
from Tests.test_Base import BaseTest
from Pages.TournamentPage import TournamentPage
import pyautogui
import time


class Test_Steps(BaseTest):
    def test(self):
        """Go to Url"""
        self.homepage = HomePage(self.driver)
        time.sleep(3)
        pyautogui.screenshot(r'{}HomePage.png'.format(TestData.screenshot_base_directory))
        """Click on the sports page from the header"""
        self.homepage.do_click(self.homepage.sports_btn)
        time.sleep(3)
        pyautogui.screenshot(r'{}SportPage.png'.format(TestData.screenshot_base_directory))
        """Search for an event in the search input on the left sidebar"""
        self.sportpage = SportPage(self.driver)
        self.sportpage.do_click(self.sportpage.search_area)
        self.sportpage.do_send_keys(self.sportpage.search_area, TestData.search_key)
        time.sleep(2)
        pyautogui.screenshot(r'{}SearchPage.png'.format(TestData.screenshot_base_directory))
        """Click on first event"""
        self.sportpage.sport()
        self.sportpage.do_click(self.sportpage.searh_results_item)
        """Add all events in the table to bet slip"""
        self.tournament_page = TournamentPage(self.driver)
        tournament_page_return_data = self.tournament_page.tournament()
        time.sleep(2)
        pyautogui.screenshot(r'{}EventTable.png'.format(TestData.screenshot_base_directory))
        """Check for the selected events name and their time. See if there is any difference"""
        self.basketpage = BasketPage(self.driver)
        basket_page_return_data=self.basketpage.basket()

        assert tournament_page_return_data[0] in basket_page_return_data[0]
        assert tournament_page_return_data[1] in basket_page_return_data[1]
