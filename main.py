from pathlib import Path
import argparse
from web.web_scraper import fetcher as web_fetcher, parser as web_parser, writer as web_writer, web_driver

# set base directory
BASE_DIR = Path(__file__).resolve().parent
print("base: " + str(BASE_DIR))

# set csv data directory
COMPANY_CSV = BASE_DIR / "web" / "data" / "companies.csv"
# print("compnay_csv " + COMPANY_CSV)

def run_web_scraper():

    url = "https://www.makati.gov.ph/cms/business/top-100-corporations/2261?content=4721"
    table_xpath = '/html/body/app-root/app-cms/div/div[4]/app-default-cms/div/div/div/div/div[2]/div/cms-content-viewer/div/cms-html-content-viewer/drag-scroll/div/div/div/div/div/table'
    
    driver = web_driver.get_driver(browser="chrome", headless=False)
    table_fetch = web_fetcher.selenium_fetch(driver, url, table_xpath)
    table_contents, headers = web_parser.parse_companies(table_fetch)
    print(headers)

    # CSV Write
    web_writer.write_to_csv(
        COMPANY_CSV, 
        table_contents, 
        headers
    )

    driver.quit()


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