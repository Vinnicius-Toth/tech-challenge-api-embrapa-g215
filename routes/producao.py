from fastapi import APIRouter, HTTPException
from scrape.scrape import scrape_table
from utils.utils import validar_ano
from utils.utils import capturar_url
from enums.enums import range_anos_embrapa

router = APIRouter()

desc_documentacao = (
    f"""
    <b>Dados de Producao: "producao/ano"</b><br></b><br>
    <b>Possíveis valores</b><br>
    <b>ano:</b> {range_anos_embrapa[0]} a {range_anos_embrapa[1]}<br>
    """
)

@router.get("/producao", include_in_schema=False)
async def producao_root():
    """
    Rota informativa raiz para Producao.
    Retorna uma mensagem de erro informando que o ano deve ser informados na URL.
    :return: Mensagem de erro.
    """
    raise HTTPException(
            status_code=400, 
            detail="Informe o ano na URL: /producao/{ano}"
        )


@router.get("/producao/{ano}", description=desc_documentacao, tags=["Producao"])
async def get_producao(ano: int) -> dict:
    """
    Rota para obter dados de Producao.
    :param ano: Ano a ser informado.
    :return: Dados de Producao.
    """
    aba = "producao"
    # validar_abas_embrapa(aba)
    validar_ano(ano)

    try:
        url = capturar_url(aba, ano)
        data = await scrape_table(url)
        return { "200": "OK", "data": data }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Site da EMBRAPA está fora do ar, tente novamente mais tarde - {str(e)}"
        )