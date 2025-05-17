from fastapi import APIRouter, HTTPException
from scrape.scrape import scrape_table
from utils.utils import validar_ano
from utils.utils import validar_subcategorias
from utils.utils import capturar_url
from enums.enums import abas_embrapa, range_anos_embrapa

router = APIRouter()

desc_documentacao = (
    f"""
    <b>Dados de processamento: "/processamento/ano/subcategoria"</b><br></b><br>
    <b>Possíveis valores</b><br>
    <b>ano:</b> {range_anos_embrapa[0]} a {range_anos_embrapa[1]}<br>
    <b>subcategoria:</b> {', '.join(abas_embrapa['processamento']['subcategorias'].keys())}
    """
)

@router.get("/processamento", include_in_schema=False)
async def processamento_root():
    """
    Rota informativa raiz para processamento.
    Retorna uma mensagem de erro informando que o ano e a subcategoria devem ser informados na URL.
    :return: Mensagem de erro.
    """
    raise HTTPException(
            status_code=400, 
            detail="Informe o ano e a subcategoria na URL: /processamento/{ano}/{subcategoria}"
        )

@router.get("/processamento/{ano}", include_in_schema=False)
async def processamento_ano(ano: int):
    """
    Rota informativa para processamento com ano informado.
    Retorna uma mensagem de erro informando que a subcategoria deve ser informada na URL.
    :param ano: Ano a ser informado.
    :return: Mensagem de erro.
    """
    raise HTTPException(
            status_code=400, 
            detail="Informe também a subcategoria na URL: /processamento/{ano}/{subcategoria}"
        )

@router.get("/processamento/{ano}/{subcategoria}", description=desc_documentacao, tags=["Processamento"])
async def get_processamento(ano: int, subcategoria: str) -> dict:
    """
    Rota para obter dados de processamento.
    :param ano: Ano a ser informado.
    :param subcategoria: Subcategoria a ser informada.
    :return: Dados de processamento.
    """
    aba = "processamento"
    # validar_abas_embrapa(aba)
    validar_ano(ano)
    validar_subcategorias(aba, subcategoria)

    try:
        url = capturar_url(aba, ano, subcategoria)
        data = await scrape_table(url)
        return { "200": "OK", "data": data }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Site da EMBRAPA está fora do ar, tente novamente mais tarde - {str(e)}"
        )