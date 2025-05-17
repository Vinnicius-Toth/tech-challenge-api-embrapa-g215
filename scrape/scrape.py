from fastapi import HTTPException
import httpx
from bs4 import BeautifulSoup
import pandas as pd

async def scrape_table(url: str) -> dict:
    """
    Função para fazer o scraping de uma tabela de uma página da web.
    :param url: URL da página a ser raspada.
    :return: Dados da tabela em formato de dicionário.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'tb_base tb_dados'})

    if not table:
        raise HTTPException(
            status_code=404,
            detail="Tabela não encontrada na página."
        )

    # Extrair cabeçalhos
    headers = [th.text.strip() for th in table.find_all('th')]

    # Extrair Linhas
    rows = []
    for tr in table.find_all('tr'):
        cols = tr.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:
            rows.append(cols)

    # Converter para DataFrame
    df = pd.DataFrame(rows, columns=headers)
    return df.to_dict(orient='records')