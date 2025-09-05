from abc import ABC, abstractmethod
from typing import Any, List, Dict

import logging
import os
import csv

class DataWriter(ABC):

    @abstractmethod
    def write(self, data: Any, headers: Any, **kwargs) -> None:
        """ Write structured data to a destination. """
        pass

class CSVWriter(DataWriter):
    """
    Write data to CSV.
    """
    def __init__(self, append_mode: bool = True):
        self.append_mode = append_mode

    def write(self, filename: str, data:List[Dict[str, str]], headers: List[str]) -> None:
        """
        Args:
            filename (str): The path to the output CSV file.
            data (List[Dict[str, str]]): The structured data to write.
            headers (List[str]): The headers for the CSV file.
        """
        if not data:
            logging.warning("No data to write.")
            return None
        
        file_exists = os.path.isfile(filename)
        mode = 'a' if self.append_mode and file_exists else 'w'
        
        try:
            with open(filename, mode=mode, newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()

                if mode == "w" or not file_exists:
                    writer.writeheader()

                writer.writerows(data)

            logging.info(f"Data written to {filename} successfully.")

        except Exception as e:

            logging.error(f"Error writing to {filename}: {e}")
    
