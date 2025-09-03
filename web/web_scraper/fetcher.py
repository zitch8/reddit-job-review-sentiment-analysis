import requests
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# For table data that requires JavaScript rendering
def selenium_fetch(driver, url, table_xpath):
    
    try:
        driver.get(url)

        # Parse with XPATH based element
        table = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, table_xpath))
        )

        
        rows = table.find_elements(By.TAG_NAME, 'tr')
        return rows
    
    except Exception as e:
        print(f"Error fetching {url} with Selenium: {e}")
        return []

# For static HTML content
def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return BeautifulSoup(response.text, 'html.parser')
    
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None