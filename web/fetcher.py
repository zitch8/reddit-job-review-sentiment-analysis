from abc import ABC, abstractmethod
from typing import Any

import requests
import logging

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver_manager import WebDriverManager

class DataFetcher(ABC):
    """
     Abstract base class for data fetching implementations.
    """

    @abstractmethod
    def fetch(self, url: str, **kwargs) -> Any:
        """ Fetch data from the given URL. """
        pass

class HTMLFetcher(DataFetcher):

    """
    For static HTML content using requests.
    """

    def fetch(self, url: str, **kwargs) -> Any:
        """
        Fetch HTML content and return BeatifulSoup object.
        
        Args:
            url (str): The URL to fetch.
            kwargs: Additional arguments for requests.get (e.g., headers, params).
        """

        try:
            response = requests.get(url, **kwargs)
            response.raise_for_status()  # Raise an error for bad responses
            return BeautifulSoup(response.text, 'html.parser')
        
        except requests.RequestException as e:
            logging.error(f"Error fetching {url}: {e}")
            return None
        
class SeleniumFetcher(DataFetcher):
    """
    For dynamic content rendered by JavaScript using Selenium WebDriver.
    """

    def __init__(self, driver_manager: WebDriverManager):
        self.driver = driver_manager

    def fetch(self, url: str, element_path: tuple, **kwargs) -> Any:

        """ 
        Fetch element using Selenium. 

        Args:
            url (str): The URL to fetch.
            element_path (tuple): Tuple of (By, value) for locating elements.
            kwargs: Additional arguments for WebDriverWait (e.g., timeout).

        """

        driver = WebDriverManager.get_driver()
        try:
            driver.get(url)

            element = WebDriverWait(self.driver, kwargs).until(
                EC.presence_of_element_located((element_path))
            )
            
            return element
        
        except Exception as e:
            logging.error(f"Error fetching {url} with Selenium: {e}")
            return []