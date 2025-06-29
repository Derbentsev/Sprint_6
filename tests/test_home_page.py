import pytest
import allure

from pages.home_page import HomePage
from data.data import TestData
from locators.home_page_locators import HomePageLocators


@allure.parent_suite('Домашняя страница')
class TestHomePage:
    @pytest.mark.parametrize(
        'question_number, answer_text',
        TestData.questions.items()
    )
    def test_open_question_success(self, question_number, answer_text, web_driver):
        allure.dynamic.title(f'Успешное открытие вопроса {question_number} в секции FAQ')
        allure.dynamic.description(f'На странице ищем раздел FAQ, открываем вопрос {question_number} ' \
        'и проверяем текст ответа')

        home_page = HomePage(web_driver)
        home_page.wait_page_load(HomePageLocators.faq_section)
        home_page.scroll_to_element(HomePageLocators.faq_section)
        home_page.click_on_question(question_number)

        answer_text_current = home_page.get_answer_text(question_number)
        assert answer_text_current == answer_text
