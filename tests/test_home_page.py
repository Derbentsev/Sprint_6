import pytest

from pages.home_page import HomePage
from data.test_data import TestData


class TestQuestions:
    @pytest.mark.parametrize(
        'question_number, answer_text',
        TestData.questions.items())
    def test_open_question(self, question_number, answer_text):
        home_page = HomePage()
        home_page.scroll_to_faq()
        home_page.click_on_question(question_number)

        answer_text_current = home_page.get_answer_text(question_number)
        assert answer_text_current == answer_text
