from selenium.webdriver.common.by import By


class HomePageLocators:
    faq_section = (By.CLASS_NAME, 'accordion')
    faq_question_item = (By.XPATH, '//div[@class="accordion__button"]')
    faq_answer_item = (By.XPATH, '//div[@class="accordion__panel"]/p')

    order_header_button = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')
    order_button = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')
