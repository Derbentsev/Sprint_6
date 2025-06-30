import pytest
from selenium import webdriver
from urls.urls import TestUrls


@pytest.fixture
def web_driver():
    driver = webdriver.Firefox()
    driver.get(TestUrls.home_page_url)
    yield driver
    driver.quit()
