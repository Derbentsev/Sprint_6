from pages.home_page import HomePage
from pages.order_page import OrderPage
from data.test_data import DataTest


class TestOrderPage:
    def test_order_via_header_button(self):
        HomePage.click_on_order_header_button()


    def test_order_via_button(self):
        HomePage.click_on_order_button()


    def test_back_to_main_page_via_scooter_logo(self):
        HomePage.click_on_scooter_logo()
        HomePage.wait_home_page_load()
    

    def test_back_to_dzen_page_via_yandex_logo(self):
        HomePage.click_on_yandex_logo()
        HomePage.check_current_page_is_dzen()
