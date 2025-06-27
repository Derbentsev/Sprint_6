from selenium.webdriver.common.by import By


class HomePageLocators:
    main_page_text = (By.XPATH, '//div[contains(., "Самокат на пару дней")]')

    faq_section = (By.CLASS_NAME, 'accordion')
    faq_question_item = (By.XPATH, '//div[@role="heading"]/div')
    faq_answer_item = (By.XPATH, '//div[@role="region"]/p')

    order_header_button = (By.XPATH, '//div[contains(@class, "Header_Nav")]/div[text()="Заказать"]')
    order_button = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/div[text()="Заказать"]')
    
    faq_questions_items = {
        1 : (By.XPATH, '//div[@id="accordion__heading-8"]'),
        2 : (By.XPATH, '//div[@id="accordion__heading-9"]'),
        3 : (By.XPATH, '//div[@id="accordion__heading-10"]'),
        4 : (By.XPATH, '//div[@id="accordion__heading-11"]'),
        5 : (By.XPATH, '//div[@id="accordion__heading-12"]'),
        6 : (By.XPATH, '//div[@id="accordion__heading-13"]'),
        7 : (By.XPATH, '//div[@id="accordion__heading-14"]'),
        8 : (By.XPATH, '//div[@id="accordion__heading-15"]')
    }

    faq_answers_items = {
        1 : (By.XPATH, '//div[@id="accordion__panel-8"]'),
        2 : (By.XPATH, '//div[@id="accordion__panel-9"]'),
        3 : (By.XPATH, '//div[@id="accordion__panel-10"]'),
        4 : (By.XPATH, '//div[@id="accordion__panel-11"]'),
        5 : (By.XPATH, '//div[@id="accordion__panel-12"]'),
        6 : (By.XPATH, '//div[@id="accordion__panel-13"]'),
        7 : (By.XPATH, '//div[@id="accordion__panel-14"]'),
        8 : (By.XPATH, '//div[@id="accordion__panel-15"]')
    }

    scooter_logo = (By.XPATH, '//img[@alt="Scooter"]')
    yandex_logo = (By.XPATH, '//img[@alt="Yandex"]')
    dzen_logo = (By.XPATH, '//div[text()="Новости"]')
