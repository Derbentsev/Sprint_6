from pages.order_page import OrderPage


class TestHelpers:
    def fill_order_page(order_page: OrderPage, order_data: dict[str, str]):
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
