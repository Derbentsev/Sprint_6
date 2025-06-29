import allure

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators
from locators.home_page_locators import HomePageLocators



class BasePage:
    def __init__(self, web_driver: webdriver.Remote):
        self.driver = web_driver        


    @allure.step('Проверяем, что текущая страница - главная')
    def wait_page_load(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(HomePageLocators.faq_section)
        )


    @allure.step('Проверяем, что текущая страница - Дзен')
    def check_current_page_is_dzen(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(BasePageLocators.dzen_logo)
        )
