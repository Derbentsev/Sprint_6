import pytest

from selenium import webdriver

from data.test_data import TestData


@pytest.fixture
def web_driver():
    driver = webdriver.Firefox()
    driver.get(TestData.home_page_url)
    yield driver
    driver.quit()
