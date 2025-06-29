import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):
    @allure.step('Заполняем поле "Станция метро"')
    def fill_metro_station(self, metro_station):
        self.driver.find_element(*OrderPageLocators.input_metro_station).send_keys(metro_station)
        self.driver.find_element(*OrderPageLocators.get_metro_station_item_locator(metro_station)).click()


    @allure.step('Заполняем поле "Дата"')
    def fill_date(self, date):
        element = self.driver.find_element(*OrderPageLocators.input_date)
        element.send_keys(date)
        element.send_keys(Keys.RETURN)


    @allure.step('Заполняем поле "Период аренды"')
    def fill_rental_period(self, rental_period):
        self.driver.find_element(*OrderPageLocators.input_rental_period).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.get_rental_period_item_locator(rental_period))
        ).click()


    @allure.step('Заполняем поле "Цвет самоката"')
    def fill_scooter_color(self, scooter_color):
        self.driver.find_element(*OrderPageLocators.get_scooter_color_locator(scooter_color)).click()
