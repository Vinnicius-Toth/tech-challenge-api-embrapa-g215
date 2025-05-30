from fastapi import APIRouter, HTTPException
from scrape.scrape import scrape_table
from utils.utils import validar_ano
from utils.utils import validar_subcategorias
from utils.utils import capturar_url
from enums.enums import abas_embrapa, range_anos_import_export

router = APIRouter()

desc_documentacao = (
    f"""
    <b>Dados de Exportacao: "/exportacao/ano/subcategoria"</b><br></b><br>
    <b>Possíveis valores</b><br>
    <b>ano:</b> {range_anos_import_export[0]} a {range_anos_import_export[1]}<br>
    <b>subcategoria:</b> {', '.join(abas_embrapa['exportacao']['subcategorias'].keys())}
    """
)

@router.get("/exportacao", include_in_schema=False)
async def exportacao_root():
    """
    Rota informativa raiz para exportacao.
    Retorna uma mensagem de erro informando que o ano e a subcategoria devem ser informados na URL.
    :return: Mensagem de erro.
    """
    raise HTTPException(
            status_code=400, 
            detail="Informe o ano e a subcategoria na URL: /exportacao/{ano}/{subcategoria}"
        )

@router.get("/exportacao/{ano}", include_in_schema=False)
async def exportacao_ano(ano: int):
    """
    Rota informativa para exportacao com ano informado.
    Retorna uma mensagem de erro informando que a subcategoria deve ser informada na URL.
    :param ano: Ano a ser informado.
    :return: Mensagem de erro.
    """
    raise HTTPException(
            status_code=400, 
            detail="Informe também a subcategoria na URL: /exportacao/{ano}/{subcategoria}"
        )

@router.get("/exportacao/{ano}/{subcategoria}", description=desc_documentacao, tags=["Exportacao"])
async def get_exportacao(ano: int, subcategoria: str) -> dict:
    """
    Rota para obter dados de exportacao.
    :param ano: Ano a ser informado.
    :param subcategoria: Subcategoria a ser informada.
    :return: Dados de exportacao.
    """
    aba = "exportacao"
    validar_ano(ano, flg_import_export=True)
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