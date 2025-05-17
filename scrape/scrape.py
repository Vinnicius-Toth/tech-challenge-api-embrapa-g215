import httpx
from bs4 import BeautifulSoup
import pandas as pd

async def scrape_table(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'tb_base tb_dados'})

    if not table:
        return {"error": "No table found at the given URL"}

    # Extract headers
    headers = [th.text.strip() for th in table.find_all('th')]

    # Extract rows
    rows = []
    for tr in table.find_all('tr'):
        cols = tr.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:
            rows.append(cols)

    # Convert to DataFrame
    df = pd.DataFrame(rows, columns=headers)
    return df.to_dict(orient='records')