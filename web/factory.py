
from .web_scraper import WebScraper
from .driver_manager import WebDriverManager
from .fetcher import SeleniumFetcher, HTMLFetcher
from .parser import TableParser
from .writer import CSVWriter


"""
Factory methods to create different types of web scrapers
"""

def selenium_table_scraper(browser: str = "chrome", headless: bool = True, ) -> WebScraper:
    """
    Create scraper that uses Selenium
    """
    driver_manager = WebDriverManager(browser=browser, headless=headless)
    fetcher = SeleniumFetcher(driver_manager)
    parser = TableParser()  
    writer = CSVWriter()

    return WebScraper(driver_manager, fetcher, parser, writer)


def html_table_scraper() -> WebScraper:
    """
    Create scraper that uses requests and BeautifulSoup
    """
    fetcher = HTMLFetcher()
    parser = TableParser()  
    writer = CSVWriter()

    return WebScraper(None, fetcher, parser, writer)
