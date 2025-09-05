from pathlib import Path

from web.factory import selenium_table_scraper, html_table_scraper

BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = BASE_DIR / "config.yaml"

# Set web data directory
WEB_DATA_DIR = BASE_DIR / "web" / "data"
WEB_JSON = BASE_DIR / WEB_DATA_DIR / "company_web.json"


def main():
    "test"
    with selenium_table_scraper("chrome", headless=True) as scraper:
        scraper.scrape_table(
            url="https://www.makati.gov.ph/cms/business/top-100-corporations/2261?content=4721",
            table_xpath="/html/body/app-root/app-cms/div/div[4]/app-default-cms/div/div/div/div/div[2]/div/cms-content-viewer/div/cms-html-content-viewer/drag-scroll/div/div/div/div/div/table",
            output_file=BASE_DIR / WEB_DATA_DIR / "companies.csv",
            timeout=15
        )


if __name__ == "__main__":
    main()