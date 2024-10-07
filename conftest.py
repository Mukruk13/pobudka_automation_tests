import pytest
from utils.browser_factory import BrowserFactory
from config.config import TestConfig

@pytest.fixture(scope="function")
def driver():
    browser = BrowserFactory.get_browser()
    browser.implicitly_wait(TestConfig.IMPLICIT_WAIT)
    yield browser
    browser.quit()

@pytest.fixture(scope="session")
def base_url():
    return TestConfig.BASE_URL

@pytest.fixture(scope="function")
def login(driver):
    # logika logowania
    pass