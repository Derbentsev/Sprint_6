import pytest
import allure

from selenium import webdriver

from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.base_page import BasePage
from data.data import TestData
from helpers.helpers import TestHelpers


@allure.parent_suite('Страница заказа самоката')
class TestOrderPage:
    @pytest.mark.parametrize('order_data', [TestData.order_data])
    @allure.title('Проверка корректности заказа самоката' \
    ' через верхнюю кнопку "Заказать"')
    @allure.description('Нажимаем на верхнюю кнопку "Заказать",' \
    ' заполняем форму заказа')
    def test_order_via_header_button_success(
        self,
        order_data: dict[str, str],
        web_driver: webdriver.Remote
        ):

        home_page = HomePage(web_driver)
        home_page.wait_main_page_completed()
        home_page.click_on_question_order_header_button()

        order_page = OrderPage(web_driver)
        order_page.wait_order_page_completed()
        TestHelpers.fill_order_page(order_page, order_data)
        assert order_page.wait_order_success()


    @pytest.mark.parametrize('order_data', [TestData.order_data])
    @allure.title('Проверка корректности заказа самоката' \
    ' через кнопку "Заказать" в середине страницы')
    @allure.description('Нажимаем на кнопку "Заказать" в середине страницы,' \
    'заполняем форму заказа')
    def test_order_via_button_success(
        self,
        order_data: dict[str, str],
        web_driver: webdriver.Remote
        ):

        home_page = HomePage(web_driver)
        home_page.wait_main_page_completed()
        home_page.scroll_to_order_button()
        home_page.click_on_question_order_button()

        order_page = OrderPage(web_driver)
        order_page.wait_order_page_completed()
        TestHelpers.fill_order_page(order_page, order_data)
        assert order_page.wait_order_success()


    @allure.title('Проверка на корректный переход' \
    ' на главную страницу при нажатии на "Самокат"')
    @allure.description('Нажимаем текст "Самокат"' \
    ' и ожидаем перехода на главную страницу')
    def test_go_to_main_page_via_scooter_logo_success(
        self,
        web_driver: webdriver.Remote
        ):

        order_page = OrderPage(web_driver)
        order_page.wait_order_page_completed()
        order_page.click_on_scooter_logo()
        assert order_page.wait_main_page_completed()


    @allure.title('Проверка на корректный переход на сайт dzen.ru'
    ' при нажатии на "Яндекс"')
    @allure.description('Нажимаем текст "Яндекс"' \
    ' и ожидаем перехода на страницу dzen.ru')
    def test_go_to_dzen_page_via_yandex_logo_success(
        self,
        web_driver: webdriver.Remote
        ):

        order_page = OrderPage(web_driver)
        order_page.wait_order_page_completed()
        order_page.click_on_yandex_logo()
        
        new_driver = TestHelpers.get_new_browser_page(web_driver)
        base_page = BasePage(new_driver)
        assert base_page.wait_dzen_page_completed()
