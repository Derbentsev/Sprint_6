from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, web_driver: webdriver.Remote, page_url):
        self.driver = web_driver
        self.driver.get(page_url)


    def wait_page_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.load
        )


    def click_on_scooter_logo(self):
        self.driver.find_element(*BasePageLocators.scooter_logo).click()


    def click_on_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.yandex_logo).click()
    

    def check_current_page_is_dzen(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(BasePageLocators.dzen_logo)
        )
