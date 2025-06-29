import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from urls.urls import TestUrls

from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):
    _LOCATORS = BasePage._LOCATORS | {
        'first_name_order': OrderPageLocators.input_first_name,
        'order_success_text': OrderPageLocators.order_success_text,
        'input_first_name': OrderPageLocators.input_first_name,
        'input_last_name': OrderPageLocators.input_last_name,
        'input_address': OrderPageLocators.input_address,
        'input_telephone': OrderPageLocators.input_telephone,
        'input_comment': OrderPageLocators.input_comment,
        'order_next_button': OrderPageLocators.next_button,
        'order_button': OrderPageLocators.order_button,
        'order_yes_button': OrderPageLocators.order_yes_button
    }


    @allure.step('Заполняем поле')
    def fill_date(self, locator_key: str):
        element = self.find_element(OrderPageLocators.input_date)
        element.send_keys(self._LOCATORS[locator_key])


    @allure.step('Открываем страницу заказа самоката')
    def wait_order_page_load(self):
        self.driver.get(TestUrls.order_page_url)
        self.wait_element_displayed('first_name_order')


    @allure.step('Заполняем поле "Станция метро"')
    def fill_metro_station(self, metro_station):
        self.find_element(OrderPageLocators.input_metro_station).send_keys(metro_station)
        self.find_element(OrderPageLocators.get_metro_station_item_locator(metro_station)).click()


    @allure.step('Заполняем поле "Дата"')
    def fill_date(self, date):
        element = self.find_element(OrderPageLocators.input_date)
        element.send_keys(date)
        element.send_keys(Keys.RETURN)


    @allure.step('Заполняем поле "Период аренды"')
    def fill_rental_period(self, rental_period):
        self.find_element(OrderPageLocators.input_rental_period).click()
        self.click_on_element(OrderPageLocators.get_rental_period_item_locator(rental_period))


    @allure.step('Заполняем поле "Цвет самоката"')
    def fill_scooter_color(self, scooter_color):
        self.find_element(OrderPageLocators.get_scooter_color_locator(scooter_color)).click()
