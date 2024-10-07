from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.config import TestConfig

class BrowserFactory:
    @staticmethod
    def get_browser():
        browser_name = TestConfig.BROWSER.lower()
        if browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            if TestConfig.HEADLESS:
                options.add_argument('--headless')
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            if TestConfig.HEADLESS:
                options.add_argument('--headless')
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")