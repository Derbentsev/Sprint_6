from selenium.webdriver.common.by import By


class OrderPageLocators:
    input_first_name = (By.XPATH, '//input[@placeholder="* Имя"]')
    input_last_name = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    input_address = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    input_metro_station = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    input_telephone = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    next_button = (By.XPATH, '//button[text()="Далее"]')

    input_date = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    input_rental_period = (By.XPATH, '//div[text()="* Срок аренды]')
    input_scooter_colors = [(By.ID, 'black'), (By.ID, 'grey')]
    input_comment = (By.XPATH, '//div[text()="Комментарий для курьера]')

    order_button = (By.XPATH, '//button[text()="Заказать"]')

    order_yes_button = (By.XPATH, '//button[text()="Да"]')

    order_success_text = (By.XPATH, '//div[text()="Заказ оформлен"]')
