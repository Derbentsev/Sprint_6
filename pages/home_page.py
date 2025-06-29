from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage

import allure


class HomePage(BasePage):
    _LOCATORS = BasePage._LOCATORS | {
        'faq_section': HomePageLocators.faq_section,
        'order_button': HomePageLocators.order_button,
        'order_header_button': HomePageLocators.order_header_button,
        'faq_section': HomePageLocators.faq_section
    }


    @allure.step('Щелкаем на вопрос номер {question_number}')
    def click_on_question(self, question_number : int):
        self.find_elements(HomePageLocators.faq_question_item)[question_number].click()


    @allure.step('Считываем ответ на вопрос {question_number}')
    def get_answer_text(self, question_number : int):
        answer_text = self.find_elements(HomePageLocators.faq_answer_item)[question_number].text
        return answer_text
