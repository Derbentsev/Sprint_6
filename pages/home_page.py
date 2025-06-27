from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_page_locators import HomePageLocators


class HomePage:
    def __init__(self, web_driver):
        self.driver = web_driver
        self.driver.get('https://qa-scooter.praktikum-services.ru/')


    def wait_home_page_load(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(HomePageLocators.main_page_text)
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
        self.driver.find_element(*HomePageLocators.order_header_button).click()

    
    def click_on_order_button(self):
        self.driver.find_element(*HomePageLocators.order_button).click()


    def click_on_scooter_logo(self):
        self.driver.find_element(*HomePageLocators.scooter_logo).click()


    def click_on_yandex_logo(self):
        self.driver.find_element(*HomePageLocators.yandex_logo).click()
    

    def check_current_page_is_dzen(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(HomePageLocators.dzen_logo)
        )


    def __del__(self):
        self.driver.quit()
