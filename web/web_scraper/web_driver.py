from selenium import webdriver

# Import other browser driver services and options when needed
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(browser, headless):
    if browser.lower() == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument('--headless=new')
        options.add_argument('--remote-allow-origins=*')
        
        service_path = ChromeDriverManager().install()
        service = ChromeService(executable_path=service_path)
        driver = webdriver.Chrome(
            service=service,
            options=options
        )
        return driver
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")
