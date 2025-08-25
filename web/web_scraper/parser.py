
def parse_companies(soup, url):
    print("soup: ", soup)
    table = soup.find('table')
    if not table:
        print(f"No table found on the webpage: {url}")
        return []
    
    rows = table.find_all('tr')
    companies = []

    for tr in rows[1:]:  # Skip the header row
        cols = tr.find_all('td')
        rank = cols[0].text.strip()
        company_name = cols[1].text.strip()
        address = cols[2].text.strip() if len(cols) > 2 else "N/A"
        companies.append({
            "rank": rank,
            "name": company_name,
            "address": address,
        })

    return companies