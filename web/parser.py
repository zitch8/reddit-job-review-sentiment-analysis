from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from typing import Any, List, Dict, Tuple
import logging

from abc import ABC, abstractmethod

def parse_companies(table):
    companies = []
    headers = []

    web_table_rows = table.find_elements(By.TAG_NAME, 'tr')

    # Extract headers from the first row
    header_cols = web_table_rows[0].find_elements(By.TAG_NAME, 'th')
    if not header_cols:
        header_cols = web_table_rows[0].find_elements(By.TAG_NAME, 'td')
    headers = [col.text.strip().lower() for col in header_cols]

    for tr in web_table_rows[1:]:  # Skip the header row
        content_cols = tr.find_elements(By.TAG_NAME, 'td')
        company_details = {}

        for i, col in enumerate(content_cols):

            # Key assignment with fallback
            if i < len(headers):
                key = headers[i]
            else:
                key = f"column_{i}"
            
            company_details[key] = col.text.strip()
        companies.append(company_details)

    return companies, headers


class DataParser(ABC):
    """
    Abstract base class for data parsing implementations.
    """

    @abstractmethod
    def parse(self, raw_data: Any, **kwargs) -> Any:
        """ Parse raw data and return structured data. """
        pass


class ElementParser(DataParser):
    """
    Parse HTML element data into structured format.
    """

    def parse(self, table: WebElement) -> Tuple[List[Dict[str, str]], List[str]]:
        """
        Parse table element.

        Args:
            table: The HTML table element to parse.

        Returns:
            Tuple of (List of row data with their respective header key, headers)
        """

        self.table = table

        rows = table.find_elements(By.TAG_NAME, 'tr')

        if not rows:
            logging.error("No rows found in the table.")
            return [], []
        
        # Extract headers
        headers = self._extract_headers(rows[0])

        # Parse data rows
        parsed_data = []
        for row in rows[1:]:
            row_data = self._parse_row(row, headers)


    def _extract_headers(self, header_row) -> List[str]:
        """ 
        Extract headers from the header row. 
        """

        headers = []

        header_cols = header_row.find_elements(By.TAG_NAME, 'th')

        # Create custom header if no th found
        if not header_cols:
            logging.info("No table header, will create custom header")
            header_cols = header_row.find_elements(By.TAG_NAME, 'td')
            for i in range(len(header_cols)):
                headers.append(f"column_{i}")
                
            return headers
        
        for col in header_cols:
            # Remove special characters or spaces
            header_text = col.text.strip().lower()
            clean_header = "".join(c if c.isalnum() else '_' for c in header_text)
            headers.append(clean_header)

        return headers
    
    def _parse_row(self, row, headers: List[str]) -> Dict[str, str]:
        """ 
        Parse a single row into a dictionary using headers as keys. 
        """

        content_cols = row.find_elements(By.TAG_NAME, 'td')
        row_data = {}

        for i, col in enumerate(content_cols):
            key = headers[i]
            row_data[key] = col.text.strip()

        return row_data
        
        

        





    