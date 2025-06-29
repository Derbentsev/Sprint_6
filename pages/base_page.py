import allure

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, web_driver: webdriver.Remote):
        self.driver = web_driver


    _LOCATORS = {
        'scooter_logo': BasePageLocators.scooter_logo,
        'yandex_logo': BasePageLocators.yandex_logo,
        'dzen_logo': BasePageLocators.dzen_logo
    }


    @allure.step('Проверяем, что страница загрузилась')
    def wait_element_displayed(self, locator_key: str):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self._LOCATORS[locator_key])
        ).is_displayed()


    @allure.step('Щелкаем на кнопку "Заказать" в шапке страницы')
    def click_on_element(self, locator_key: str):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._LOCATORS[locator_key])
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
    def scroll_to_element(self, locator_key: str):
        element = self.driver.find_element(*self._LOCATORS[locator_key])
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of(element)
        )
