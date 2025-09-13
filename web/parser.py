from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from typing import Any, List, Dict, Tuple
import logging

from abc import ABC, abstractmethod

class DataParser(ABC):
    """
    Abstract base class for data parsing implementations.
    """

    @abstractmethod
    def parse(self, raw_data: Any, **kwargs) -> Any:
        """ Parse raw data and return structured data. """
        pass


class TableParser(DataParser):
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
        rows = table.find_elements(By.TAG_NAME, 'tr')

        if not rows:
            logging.error("No rows found in the element.")
            return [], []
        
        # Extract headers
        headers = self._extract_headers(rows[0])

        # Parse data rows
        parsed_data = []
        for row in rows[1:]:
            row_data = self._parse_row(row, headers)
            if row_data:
                parsed_data.append(row_data)

        return parsed_data, headers


    def _extract_headers(self, header_row) -> List[str]:
        """ 
        Extract headers from the header row. 
        """
        header_cols = header_row.find_elements(By.TAG_NAME, 'th')

        # Create custom header if no th found
        if not header_cols:
            header_cols = header_row.find_elements(By.TAG_NAME, 'td')
        
        headers = []
        for i, col in enumerate(header_cols):
            # Remove special characters or spaces
            header_text = col.text.strip() or f"column_{i}"
            clean_header = "".join(c if c.isalnum() else '_' for c in header_text)
            headers.append(clean_header)

        return headers
    
    def _parse_row(self, row, headers: List[str]) -> Dict[str, str]:
        """ 
        Parse a single row into a dictionary using headers as keys. 
        """

        content_cols = row.find_elements(By.TAG_NAME, 'td')

        if not content_cols:
            logging.warning("Skipping row with no data columns.")
            return {}
        
        row_data = {}
        for i, col in enumerate(content_cols):
            key = headers[i] if i < len(headers) else f"column_{i}"
            row_data[key] = col.text.strip()

        return row_data
        
        

        





    