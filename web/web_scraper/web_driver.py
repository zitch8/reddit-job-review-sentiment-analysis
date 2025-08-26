from selenium import webdriver

# Import other broweser driver services and options when needed
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(browser="chrome", headless=True):
    if browser.lower() == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument('--headless')  # Run in headless mode
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), 
            options=options
        )
        return driver
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")
