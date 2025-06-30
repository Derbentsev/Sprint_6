import allure
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from urls.urls import TestUrls


class OrderPage(BasePage):
    @allure.step('Ожидаем загрузки страницы формы заказа')
    def wait_order_page_completed(self):
        self.wait_element_displayed(OrderPageLocators.input_first_name)


    @allure.step('Заполняем поле')
    def fill_date(self, locator):
        element = self.find_element(OrderPageLocators.input_date)
        element.send_keys(locator)


    @allure.step('Открываем страницу заказа самоката')
    def wait_order_page_completed(self):
        self.driver.get(TestUrls.order_page_url)
        self.wait_element_displayed(OrderPageLocators.input_first_name)


    @allure.step('Заполняем поле "Станция метро"')
    def fill_metro_station(self, metro_station):
        self.find_element(OrderPageLocators.input_metro_station).send_keys(metro_station)
        self.click_on_element(OrderPageLocators.get_metro_station_item_locator(metro_station))


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
        self.click_on_element(OrderPageLocators.get_scooter_color_locator(scooter_color))


    @allure.step('Ожидаем успешного принятия заказа')
    def wait_order_success(self):
        return self.wait_element_displayed(OrderPageLocators.order_success_text)


    @allure.step('Заполняем поле имя')
    def fill_input_first_name(self, text):
        self.fill_input_field(OrderPageLocators.input_first_name, text)


    @allure.step('Заполняем поле фамилия')
    def fill_input_last_name(self, text):
        self.fill_input_field(OrderPageLocators.input_last_name, text)


    @allure.step('Заполняем поле адрес')
    def fill_input_address(self, text):
        self.fill_input_field(OrderPageLocators.input_address, text)


    @allure.step('Заполняем поле телефон')
    def fill_input_telephone(self, text):
        self.fill_input_field(OrderPageLocators.input_telephone, text)


    @allure.step('Заполняем поле комментарий')
    def fill_input_comment(self, text):
        self.fill_input_field(OrderPageLocators.input_comment, text)


    @allure.step('Щелкаем по кнопке "Далее"')
    def click_on_next_order_button(self):
        self.click_on_element(OrderPageLocators.next_order_button)


    @allure.step('Щелкаем по кнопке "Заказать"')
    def click_on_order_button(self):
        self.click_on_element(OrderPageLocators.order_button)


    @allure.step('Щелкаем по кнопке "Да"')
    def click_on_order_yes_button(self):
        self.click_on_element(OrderPageLocators.order_yes_button)
