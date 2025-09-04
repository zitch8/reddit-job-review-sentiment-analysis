from selenium import webdriver

# Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

# Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

# Edge
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class WebDriverManager:
    
    SUPPORTED_BROWSERS = ['chrome', 'firefox', 'edge']
    
    def __init__(self, browser: str = 'chrome', headless: bool = False):
        self.browser = browser.lower()
        self.headless = headless
        self._driver = None

        if self.browswer not in self.SUPPORTED_BROWSERS:
            raise ValueError(f"Browser '{self.browser}' is not supported.")

    def get_driver(self):
        """ 
        Initialize and return the WebDriver instance.
        """
        if self._driver is None:
            self._driver = self._create_driver()
        return self._driver

    def _create_driver(self):
        """ 
        Create a new web driver instance based on the specified browser. 
        """
        
        if self.browser == 'chrome':
            self._driver = self._init_chrome_driver()

        elif self.browser == 'firefox':
            self._driver = self._init_firefox_driver()

        elif self.browser == 'edge':
            self._driver = self._init_edge_driver()

        else:
            raise ValueError(f"Browser '{self.browser}' is not supported.")
        
    def _init_chrome_driver(self):
        options = ChromeOptions()
        if self.headless:
            options.add_argument('--headless')

        options.add_argument('--remote-allow-origins=*')
        
        service_path = ChromeDriverManager().install()
        service = ChromeService(executable_path=service_path)
        
        return webdriver.Chrome(service=service, options=options)
    
    def _init_firefox_driver(self):
        options = FirefoxOptions()
        if self.headless:
            options.add_argument('--headless')

        options.add_argument('--remote-allow-origins=*')
        
        service_path = GeckoDriverManager().install()
        service = FirefoxService(executable_path=service_path)
        
        return webdriver.Firefox(service=service, options=options)
    
    def _init_edge_driver(self):
        options = EdgeOptions()
        if self.headless:
            options.add_argument('--headless')

        options.add_argument('--remote-allow-origins=*')
        
        service_path = EdgeChromiumDriverManager().install()
        service = EdgeService(executable_path=service_path)
        
        return webdriver.Edge(service=service, options=options)

    def quit_driver(self):
        """ 
        Quit the WebDriver instance if it exists.
        """
        if self._driver:
            self._driver.quit()
            self._driver = None

    def __enter__(self):
        return self.get_driver()
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.quit_driver()