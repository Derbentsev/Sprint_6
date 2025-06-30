import allure

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, web_driver: webdriver.Remote):
        self.driver = web_driver


    @allure.step('Ожидаем загрузки главной страницы')
    def wait_main_page_completed(self):
        return self.wait_element_displayed(BasePageLocators.wait_home_page_element)


    @allure.step('Проверяем, что элемент загрузился')
    def wait_element_displayed(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()


    @allure.step('Щелкаем по элементу')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()


    @allure.step('Находим элемент на странице')
    def find_element(self, locator):
        return self.driver.find_element(*locator)


    @allure.step('Находим список элементов на странице')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)


    @allure.step('Заполняем поле')
    def fill_input_field(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)


    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of(element)
        )


    @allure.step('Щелкаем по тексту "Скутер"')
    def click_on_scooter_logo(self):
        self.click_on_element(BasePageLocators.scooter_logo)


    @allure.step('Щелкаем по тексту "Яндекс"')
    def click_on_yandex_logo(self):
        self.click_on_element(BasePageLocators.yandex_logo)


    @allure.step('Проверяем, что страница Дзен загрузилась')
    def wait_dzen_page_completed(self):
        return self.wait_element_displayed(BasePageLocators.dzen_logo)
