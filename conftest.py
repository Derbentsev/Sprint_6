import pytest

from selenium import webdriver


@pytest.fixture
def web_driver():
    driver = webdriver.Firefox()    
    yield driver
    driver.quit()
