import requests
from bs4 import BeautifulSoup
from .web_driver import get_driver

# For table data that requires JavaScript rendering
def selenium_fetch(url, browser="chrome"):
    driver = get_driver(browser=browser)
    
    try:
        driver.get(url)
        driver.implicitly_wait(10)  # Wait for elements to load
    
        html = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    
    except Exception as e:
        print(f"Error fetching {url} with Selenium: {e}")
        driver.quit()
        return None

# For static HTML content
def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return BeautifulSoup(response.text, 'html.parser')
    
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None