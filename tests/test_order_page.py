import pytest

from pages.home_page import HomePage
from pages.order_page import OrderPage
from data.test_data import DataTest


class TestOrderPage:
    @pytest.mark.parametrize('order_data', [DataTest.order_data])
    def test_order_via_header_button(self, order_data: dict[str, str], web_driver):
        home_page = HomePage(web_driver)
        home_page.home_page_load()
        home_page.click_on_order_header_button()

        order_page = OrderPage(web_driver)
        order_page.wait_order_page_load()
        order_page.fill_first_name(order_data['first_name'])
        order_page.fill_last_name(order_data['last_name'])
        order_page.fill_address(order_data['address'])
        order_page.fill_metro_station(order_data['metro_station'])
        order_page.fill_telephone(order_data['telephone'])
        order_page.click_next_button()
        order_page.fill_date(order_data['date'])
        order_page.fill_rental_period(order_data['rental_period'])
        order_page.fill_scooter_color(order_data['scooter_color'])
        order_page.fill_comment(order_data['comment'])
        order_page.click_order_button()
        order_page.click_yes_order_button()
        order_page.wait_order_ready()


    @pytest.mark.parametrize('order_data', [DataTest.order_data])
    def test_order_via_button(self, order_data: dict[str, str], web_driver):
        home_page = HomePage(web_driver)
        home_page.click_on_order_header_button()

        order_page = OrderPage(web_driver)
        order_page.wait_order_page_load()
        order_page.fill_first_name(order_data['first_name'])
        order_page.fill_last_name(order_data['last_name'])
        order_page.fill_address(order_data['address'])
        order_page.fill_metro_station(order_data['metro_station'])
        order_page.fill_telephone(order_data['telephone'])
        order_page.click_next_button()
        order_page.fill_date(order_data['date'])
        order_page.fill_rental_period(order_data['rental_period'])
        order_page.fill_scooter_color(order_data['scooter_color'])
        order_page.fill_comment(order_data['comment'])
        order_page.click_yes_order_button()
        order_page.wait_order_ready()


    def test_back_to_main_page_via_scooter_logo(self):
        home_page = HomePage()
        home_page.click_on_scooter_logo()
        home_page.home_page_load()
    

    def test_back_to_dzen_page_via_yandex_logo(self):
        home_page = HomePage()
        home_page.click_on_yandex_logo()
        home_page.check_current_page_is_dzen()
