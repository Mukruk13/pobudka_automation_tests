import os
from dotenv import load_dotenv

load_dotenv()

class TestConfig:
    BASE_URL = os.getenv('BASE_URL', 'https://www.pobudka.waw.pl/')
    BROWSER = os.getenv('BROWSER', 'chrome')
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', 10))
    EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', 20))
    HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'