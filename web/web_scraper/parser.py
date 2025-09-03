def parse_companies(rows):
    companies = []

    for tr in rows[1:]:  # Skip the header row
        cols = tr.find_all('td')
        rank = cols[0].text.strip() if cols else "N/A"
        company_name = cols[1].text.strip()
        address = cols[2].text.strip() if len(cols) > 2 else "N/A"
        companies.append({
            "rank": rank,
            "name": company_name,
            "address": address,
        })

    return companies

    