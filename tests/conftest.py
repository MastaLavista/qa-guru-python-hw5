import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = "https://demoqa.com"
    browser.config.driver.maximize_window()
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.page_load_strategy = 'eager'

    yield

    browser.quit()