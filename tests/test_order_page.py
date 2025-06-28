import pytest

from selenium import webdriver

from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.base_page import BasePage
from data.test_data import TestData
from helpers.test_helpers import TestHelpers


class TestOrderPage:
    @pytest.mark.parametrize('order_data', [TestData.order_data])
    def test_order_via_header_button(self, order_data: dict[str, str], web_driver: webdriver.Remote):
        home_page = HomePage(web_driver)
        home_page.click_on_order_header_button()

        order_page = OrderPage(web_driver)
        TestHelpers.fill_order_page(order_page, order_data)
        assert order_page.wait_order_ready()


    @pytest.mark.parametrize('order_data', [TestData.order_data])
    def test_order_via_button(self, order_data: dict[str, str], web_driver: webdriver.Remote):
        home_page = HomePage(web_driver)
        home_page.click_on_order_button()

        order_page = OrderPage(web_driver)
        TestHelpers.fill_order_page(order_page, order_data)
        assert order_page.wait_order_ready()


    def test_back_to_main_page_via_scooter_logo(self, web_driver: webdriver.Remote):        
        base_page = BasePage(web_driver)
        web_driver.get(base_page.page)
        base_page.click_on_scooter_logo()
        base_page.home_page_load()


    def test_back_to_dzen_page_via_yandex_logo(self, web_driver: webdriver.Remote):
        base_page = BasePage(web_driver)
        base_page.click_on_yandex_logo()
        base_page.check_current_page_is_dzen()
