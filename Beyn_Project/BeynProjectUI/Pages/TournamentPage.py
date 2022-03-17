from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class TournamentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    """this is used click bet11X2 button for all rows on Tournament List"""
    def tournament(self):
        try:
            tournament_table = self.driver.find_element(By.XPATH,"//*[@id='nvsCoreTournamentAndTimeEventView']/div/div/nvscore-accordion/div/div[2]/nvscore-accordion-content/div/div/nvscore-dynamic-table/table")
            tournament_table_rows = tournament_table.find_elements(By.TAG_NAME, "tr")
            event_name_on_tournament_row = tournament_table_rows[4].find_element(By.XPATH,'//tr[6]/td[3]/nvscore-table-column/nvscore-table-column-text/div/span').text
            event_time_on_tournament_row = tournament_table_rows[4].find_element(By.XPATH,'//tr[6]/td[2]/nvscore-table-column/nvscore-table-column-text/div/span').text
            event_time_and_name=[event_name_on_tournament_row,event_time_on_tournament_row]
            print(event_time_and_name)

            j = 3
            for i in range(len(tournament_table_rows) - 2):
                bet11X2 = tournament_table_rows[i].find_element(By.XPATH, "//tr[{0}]/td[5]".format(str(j)))
                bet11X2.click()
                j = j + 1

        finally:

            return event_time_and_name

