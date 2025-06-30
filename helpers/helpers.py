from pages.order_page import OrderPage
from selenium import webdriver


class TestHelpers:
    def fill_order_page(order_page: OrderPage, order_data: dict[str, str]):
        order_page.fill_input_first_name(order_data['first_name'])
        order_page.fill_input_last_name(order_data['last_name'])
        order_page.fill_input_address(order_data['address'])
        order_page.fill_metro_station(order_data['metro_station'])
        order_page.fill_input_telephone(order_data['telephone'])
        order_page.click_on_next_order_button()

        order_page.fill_date(order_data['date'])
        order_page.fill_rental_period(order_data['rental_period'])
        order_page.fill_scooter_color(order_data['scooter_color'])
        order_page.fill_input_comment(order_data['comment'])
        order_page.click_on_order_button()
        order_page.click_on_order_yes_button()


    @staticmethod
    def get_new_browser_page(web_driver: webdriver.Remote):
        window_handles = web_driver.window_handles
        web_driver.switch_to.window(window_handles[-1])
        return web_driver
