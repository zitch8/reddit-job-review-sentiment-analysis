import logging

from .driver_manager import WebDriverManager
from .fetcher import DataFetcher
from .parser import DataParser
from .writer import DataWriter

class WebScraper:
    """
    Main Web Scraper
    """

    def __init__(self, 
                 driver_manager: WebDriverManager = None,
                 fetcher: DataFetcher = None,
                 parser: DataParser = None,
                 writer: DataWriter = None):
        
        self.logging = logging.getLogger(__name__)
        self.driver_manager = driver_manager
        self.fetcher = fetcher
        self.parser = parser
        self.writer = writer

    def scrape_table(self, 
                     url: str, 
                     element_path: tuple, 
                     output_file: str, 
                     timeout: int = 15) -> bool:
        
        """
        Main method to perform scraping.

        Args:
            url (str): The URL to scrape.
            element_path (tuple): The XPath to locate the table element.
            output_file (str): The path to the output file.
            parser_kwargs (dict): Additional arguments for the writer.
        """
        try:

            logging.info(f"Starting scrape for {url}")

            # Fetch data
            raw_data = self.fetcher.fetch(url, element_path, timeout=timeout)
            if raw_data is None:
                logging.error(f"Failed to fetch data from {url}")
                return False

            # Parse data
            structured_data, headers = self.parser.parse(raw_data)
            if not structured_data:
                logging.warning(f"No data parsed from {url}")
                return False

            # Write data
            self.writer.write(output_file, structured_data, headers)

            logging.info(f"Scraping completed for {url}, data written to {output_file}")
            return True
        except Exception as e:
            logging.exception(f"Error during scraping {url}: {e}")
            return False
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.driver_manager:
            self.driver_manager.quit_driver()