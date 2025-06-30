from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage

import allure


class HomePage(BasePage):
    @allure.step('Скроллим до FAQ')
    def scroll_to_faq(self):
        self.scroll_to_element(HomePageLocators.faq_section)


    @allure.step('Щелкаем на вопрос номер {question_number}')
    def click_on_question(self, question_number : int):
        self.find_elements(HomePageLocators.faq_question_item)[question_number].click()


    @allure.step('Считываем ответ на вопрос {question_number}')
    def get_answer_text(self, question_number : int):
        answer_text = self.find_elements(HomePageLocators.faq_answer_item)[question_number].text
        return answer_text


    @allure.step('Щелкаем по верхней кнопке "Заказать"')
    def click_on_question_order_header_button(self):
        self.click_on_element(HomePageLocators.order_header_button)


    @allure.step('Щелкаем по нижней кнопке "Заказать"')
    def click_on_question_order_button(self):
        self.click_on_element(HomePageLocators.order_button)


    @allure.step('Скроллим до нижней кнопки "Заказать"')
    def scroll_to_order_button(self):
        self.scroll_to_element(HomePageLocators.order_button)
