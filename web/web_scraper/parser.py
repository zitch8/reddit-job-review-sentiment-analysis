from selenium.webdriver.common.by import By

def parse_companies(rows):
    companies = []
    headers = []

    if rows:

        # Extract headers from the first row
        header_cols = rows[0].find_elements(By.TAG_NAME, 'th')
        if not header_cols:
            header_cols = rows[0].find_elements(By.TAG_NAME, 'td')
        headers = [col.text.strip().lower() for col in header_cols]

    for tr in rows[1:]:  # Skip the header row
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

    