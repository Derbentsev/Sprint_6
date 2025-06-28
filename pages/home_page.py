from locators.home_page_locators import HomePageLocators
from data.test_data import TestData

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, web_driver: webdriver.Remote):
        self.driver = web_driver
        self.driver.get(TestData.home_page_url)
        self.driver.maximize_window()

    def home_page_load(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(HomePageLocators.faq_section)
        )


    def click_on_question(self, question_number : int):
        self.driver.find_elements(*HomePageLocators.faq_question_item)[question_number].click()


    def get_answer_text(self, question_number : int):
        answer_text = self.driver.find_elements(*HomePageLocators.faq_answer_item)[question_number].text
        return answer_text
    

    def scroll_to_faq(self):
        element = self.driver.find_element(*HomePageLocators.faq_section)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(HomePageLocators.faq_section)
        )


    def click_on_order_header_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(HomePageLocators.order_header_button)
        ).click()


    def click_on_order_button(self):
        element = self.driver.find_element(*HomePageLocators.order_button)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.order_button)
        ).click()
