from selenium.webdriver.common.by import By


class BasePageLocators:
    scooter_logo = (By.XPATH, '//img[@alt="Scooter"]')
    yandex_logo = (By.XPATH, '//img[@alt="Yandex"]')
    dzen_logo = (By.XPATH, '//div[text()="Новости"]')
