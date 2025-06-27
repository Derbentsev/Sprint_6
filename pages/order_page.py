from locators.order_page_locators import OrderPageLocators

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OrderPage():
    def __init__(self, web_driver):
        self.driver = web_driver


    def wait_order_page_load(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(OrderPageLocators.input_first_name)
        )


    def fill_first_name(self, first_name):
        self.driver.find_element(*OrderPageLocators.input_first_name).send_keys(first_name)
    

    def fill_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.input_last_name).send_keys(last_name)


    def fill_first_name(self, address):
        self.driver.find_element(*OrderPageLocators.input_address).send_keys(address)


    def fill_first_name(self, metro_station):
        self.driver.find_element(*OrderPageLocators.input_metro_station).send_keys(metro_station)


    def fill_telephone(self, telephone):
        self.driver.find_element(*OrderPageLocators.input_telephone).send_keys(telephone)
    

    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()
