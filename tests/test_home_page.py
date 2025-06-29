import pytest
import allure

from pages.home_page import HomePage
from data.test_data import TestData


class TestQuestions:
    @pytest.mark.parametrize(
        'question_number, answer_text',
        TestData.questions.items()
    )

    @allure.title('Успешное открытие вопроса в секции FAQ')
    @allure.description('На странице ищем раздел FAQ, открываем вопрос и проверяем текст ответа')

    def test_open_question_success(self, question_number, answer_text, web_driver):
        home_page = HomePage(web_driver)
        home_page.scroll_to_faq()
        home_page.click_on_question(question_number)

        answer_text_current = home_page.get_answer_text(question_number)
        assert answer_text_current == answer_text
