import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.page_load_strategy = 'eager'
    browser.config.window_height = 1440
    browser.config.window_width = 900
    browser.config.base_url = "https://demoqa.com"

    yield

    browser.quit()
