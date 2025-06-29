import allure

from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import BasePageLocators
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):
    @allure.step('Ожидаем загрузки страницы формы заказа')
    def wait_order_page_load(self):
        WebDriverWait(self.driver, 7).until(
            EC.visibility_of_element_located(OrderPageLocators.input_first_name)
        )


    @allure.step('Заполняем поле "Имя"')
    def fill_first_name(self, first_name):
        self.driver.find_element(*OrderPageLocators.input_first_name).send_keys(first_name)
    

    @allure.step('Заполняем поле "Фамилия"')
    def fill_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.input_last_name).send_keys(last_name)


    @allure.step('Заполняем поле "Адрес"')
    def fill_address(self, address):
        self.driver.find_element(*OrderPageLocators.input_address).send_keys(address)


    @allure.step('Заполняем поле "Станция метро"')
    def fill_metro_station(self, metro_station):
        self.driver.find_element(*OrderPageLocators.input_metro_station).send_keys(metro_station)
        self.driver.find_element(*OrderPageLocators.get_metro_station_item_locator(metro_station)).click()


    @allure.step('Заполняем поле "Телефон"')
    def fill_telephone(self, telephone):
        self.driver.find_element(*OrderPageLocators.input_telephone).send_keys(telephone)
    

    @allure.step('Нажимаем кнопку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()


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


    @allure.step('Заполняем поле "Комментарий"')
    def fill_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.input_comment).send_keys(comment)


    @allure.step('Нажимаем кнопку "Заказать"')
    def click_order_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.order_button)
        ).click()


    @allure.step('Нажимаем кнопку для подтверждения заказа "Да"')
    def click_yes_order_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.order_yes_button)
        ).click()


    @allure.step('Ожидаем появление окна о готовности заказа')
    def wait_order_ready(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(OrderPageLocators.order_success_text)
        ).is_displayed()


    @allure.step('Нажимаем на кнопку "Самокат"')
    def click_on_scooter_logo(self):
        self.driver.find_element(*BasePageLocators.scooter_logo).click()


    @allure.step('Нажимаем на кнопку "Яндекс"')
    def click_on_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.yandex_logo).click()


    @allure.step('Проверяем, что текущая страница - главная')
    def check_current_page_is_home(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(HomePageLocators.faq_section)
        ).is_displayed()


    @allure.step('Проверяем, что текущая страница - Дзен')
    def check_current_page_is_dzen(self):
        return WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located(BasePageLocators.dzen_logo)
        ).is_displayed()
