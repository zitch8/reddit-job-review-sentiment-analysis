import logging

from driver_manager import WebDriverManager
from fetcher import DataFetcher
from parser import DataParser
from writer import DataWriter

class WebScraper:
    """
    Main Web Scraper
    """

    def __init__(self, 
                 driver_manager: WebDriverManager = None,
                 fetcher: DataFetcher = None,
                 parser: DataParser = None,
                 writer: DataWriter = None):
        
        self.fetcher = fetcher
        self.parser = parser
        self.writer = writer

    def scrape(self, url: str, output_file: str, fetcher_kwargs: dict, writer_kwargs: dict) -> None:
        """
        Main method to perform scraping.

        Args:
            url (str): The URL to scrape.
            output_file (str): The path to the output file.
            fetcher_kwargs (dict): Additional arguments for the fetcher.
            writer_kwargs (dict): Additional arguments for the writer.
        """

        logging.info(f"Starting scrape for {url}")

        # Fetch data
        raw_data = self.fetcher.fetch(url, **fetcher_kwargs)
        if raw_data is None:
            logging.error(f"Failed to fetch data from {url}")
            return

        # Parse data
        structured_data, headers = self.parser.parse(raw_data)
        if not structured_data:
            logging.warning(f"No data parsed from {url}")
            return

        # Write data
        self.writer.write(output_file, structured_data, headers, **writer_kwargs)

        logging.info(f"Scraping completed for {url}, data written to {output_file}")