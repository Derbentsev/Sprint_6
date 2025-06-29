import allure

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, web_driver: webdriver.Remote):
        self.driver = web_driver        


    @allure.step('Проверяем, что страница загрузилась')
    def wait_page_load(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()


    @allure.step('Щелкаем на кнопку "Заказать" в шапке страницы')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()


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
