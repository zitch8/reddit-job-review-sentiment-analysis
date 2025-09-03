import requests
from bs4 import BeautifulSoup
from .web_driver import get_driver

# For table data that requires JavaScript rendering
def selenium_fetch(url, browser="chrome"):
    driver = get_driver(browser=browser)
    
    try:
        driver.get(url)
        driver.implicitly_wait(10)  # Wait for elements to load

        # BeautifulSoup object
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # Parse with xpath based element
        table = driver.find_element_by_xpath('/html/body/app-root/app-cms/div/div[4]/app-default-cms/div/div/div/div/div[2]/div/cms-content-viewer/div/cms-html-content-viewer/drag-scroll/div/div/div/div/div/table')
        if not table:
            print(f"No table found on the webpage: {url}")
            return[]
        
        rows = table.find_elements_by_tag_name('tr')

        driver.quit()
        return rows
        
    
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