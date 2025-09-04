import argparse
import logging

from pathlib import Path
from web import driver, parser, writer
from web.data import fetcher

BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = BASE_DIR / "config.yaml"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set web data directory
WEB_DATA_DIR = BASE_DIR / "web" / "data"

COMPANY_CSV = BASE_DIR / WEB_DATA_DIR / "companies.csv"
WEB_JSON = BASE_DIR / WEB_DATA_DIR / "company_web.json"

def run_web_scraper():

    url = "https://www.makati.gov.ph/cms/business/top-100-corporations/2261?content=4721"
    table_xpath = '/html/body/app-root/app-cms/div/div[4]/app-default-cms/div/div/div/div/div[2]/div/cms-content-viewer/div/cms-html-content-viewer/drag-scroll/div/div/div/div/div/table'
    
    web_driver = driver.get_driver(browser="chrome", headless=True)
    table_fetch = fetcher.selenium_fetch_table(web_driver, url, table_xpath)
    table_contents, headers = parser.parse_companies(table_fetch)

    # CSV Write
    writer.write_to_csv(
        COMPANY_CSV, 
        table_contents, 
        headers
    )

    web_driver.quit()


def main():

    # create CLI argument parser
    parser = argparse.ArgumentParser(description="Reddit and Web Scraper")

    parser.add_argument(
        "--web_parse",
        action="store_true",
        help="Run the web scraper")
    
    # parser.add_argument("--reddit_parse", action="store_true", help="Run the Reddit scraper")
    args = parser.parse_args()

    if args.web_parse:
        run_web_scraper()

    # if args.reddit_parse:


if __name__ == "__main__":
    main()