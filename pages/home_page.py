from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage

import allure


class HomePage(BasePage):
    @allure.step('Щелкаем на вопрос номер {question_number}')
    def click_on_question(self, question_number : int):
        self.driver.find_elements(*HomePageLocators.faq_question_item)[question_number].click()


    @allure.step('Считываем ответ на вопрос {question_number}')
    def get_answer_text(self, question_number : int):
        answer_text = self.driver.find_elements(*HomePageLocators.faq_answer_item)[question_number].text
        return answer_text
