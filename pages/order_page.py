from locators.order_page_locators import OrderPageLocators

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class OrderPage():
    def __init__(self, web_driver: webdriver.Remote):
        self.driver = web_driver        


    def wait_order_page_load(self):
        WebDriverWait(self.driver, 7).until(
            EC.visibility_of_element_located(OrderPageLocators.input_first_name)
        )


    def fill_first_name(self, first_name):
        self.driver.find_element(*OrderPageLocators.input_first_name).send_keys(first_name)
    

    def fill_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.input_last_name).send_keys(last_name)


    def fill_address(self, address):
        self.driver.find_element(*OrderPageLocators.input_address).send_keys(address)


    def fill_metro_station(self, metro_station):
        self.driver.find_element(*OrderPageLocators.input_metro_station).send_keys(metro_station)
        self.driver.find_element(*OrderPageLocators.get_metro_station_item_locator(metro_station)).click()


    def fill_telephone(self, telephone):
        self.driver.find_element(*OrderPageLocators.input_telephone).send_keys(telephone)
    

    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()


    def fill_date(self, date):
        element = self.driver.find_element(*OrderPageLocators.input_date)
        element.send_keys(date)
        element.send_keys(Keys.RETURN)
    

    def fill_rental_period(self, rental_period):
        self.driver.find_element(*OrderPageLocators.input_rental_period).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.get_rental_period_item_locator(rental_period))
        ).click()


    def fill_scooter_color(self, scooter_color):
        self.driver.find_element(*OrderPageLocators.get_scooter_color_locator(scooter_color)).click()


    def fill_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.input_comment).send_keys(comment)


    def click_order_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.order_button)
        ).click()


    def click_yes_order_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.order_yes_button)
        ).click()


    def wait_order_ready(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(OrderPageLocators.order_success_text)
        ).is_displayed()
