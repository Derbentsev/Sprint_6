from locators.home_page_locators import HomePageLocators
from data.test_data import TestData
from pages.base_page import BasePage

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import allure


class HomePage(BasePage):
    @allure.step('Ожидаем загрузки главной страницы')
    def wait_home_page_load(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(HomePageLocators.faq_section)
        )


    @allure.step('Щелкаем на вопрос номер {question_number}')
    def click_on_question(self, question_number : int):
        self.driver.find_elements(*HomePageLocators.faq_question_item)[question_number].click()


    @allure.step('Считываем ответ на вопрос {question_number}')
    def get_answer_text(self, question_number : int):
        answer_text = self.driver.find_elements(*HomePageLocators.faq_answer_item)[question_number].text
        return answer_text
    

    @allure.step('Скроллим до секции FAQ')
    def scroll_to_faq(self):
        element = self.driver.find_element(*HomePageLocators.faq_section)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(HomePageLocators.faq_section)
        )


    @allure.step('Щелкаем на кнопку "Заказать" в шапке страницы')
    def click_on_order_header_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(HomePageLocators.order_header_button)
        ).click()


    @allure.step('Щелкаем на кнопку "Заказать" в середине страницы')
    def click_on_order_button(self):
        element = self.driver.find_element(*HomePageLocators.order_button)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.order_button)
        ).click()
