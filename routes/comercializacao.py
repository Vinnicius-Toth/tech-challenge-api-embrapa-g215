from fastapi import APIRouter, HTTPException
from scrape.scrape import scrape_table
from utils.utils import validar_ano
from utils.utils import capturar_url
from enums.enums import range_anos_embrapa

router = APIRouter()

desc_documentacao = (
    f"""
    <b>Dados de Comercializacao: "comercializacao/ano"</b><br></b><br>
    <b>Possíveis valores</b><br>
    <b>ano:</b> {range_anos_embrapa[0]} a {range_anos_embrapa[1]}<br>
    """
)

@router.get("/comercializacao", include_in_schema=False)
async def comercializacao_root():
    """
    Rota informativa raiz para Comercializacao.
    Retorna uma mensagem de erro informando que o ano deve ser informados na URL.
    :return: Mensagem de erro.
    """
    raise HTTPException(
            status_code=400, 
            detail="Informe o ano na URL: /comercializacao/{ano}"
        )


@router.get("/comercializacao/{ano}", description=desc_documentacao, tags=["Comercializacao"])
async def get_comercializacao(ano: int) -> dict:
    """
    Rota para obter dados de Comercializacao.
    :param ano: Ano a ser informado.
    :return: Dados de Comercializacao.
    """
    aba = "comercializacao"
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