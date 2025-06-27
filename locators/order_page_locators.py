from selenium.webdriver.common.by import By


class OrderPageLocators:
    input_first_name = (By.XPATH, '//input[@placeholder="* Имя"]')
    input_last_name = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    input_address = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    input_telephone = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    next_button = (By.XPATH, '//button[text()="Далее"]')

    input_date = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    input_metro_station = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    input_rental_period = (By.XPATH, '//div[text()="* Срок аренды"]')    
    input_comment = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    order_button = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]')

    order_yes_button = (By.XPATH, '//button[text()="Да"]')
    order_success_text = (By.XPATH, '//div[text()="Заказ оформлен"]')


    def get_metro_station_item_locator(metro_station):
        return (By.XPATH, f'//div[contains(@class, "Order_Text") and text()="{metro_station}"]')


    def get_rental_period_item_locator(rental_period):
        return (By.XPATH, f'//div[@class="Dropdown-option" and text()="{rental_period}"]')


    def get_scooter_color_locator(scooter_color):
        return (By.XPATH, f'//label[text()="{scooter_color}"]')
