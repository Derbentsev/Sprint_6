from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_page_locators import HomePageLocators


class HomePage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://qa-scooter.praktikum-services.ru/')


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


    def __del__(self):
        self.driver.quit()
