from fastapi import APIRouter, HTTPException
from scrape.scrape import scrape_table
from utils.utils import validar_ano
from utils.utils import validar_subcategorias
from utils.utils import capturar_url
from enums.enums import abas_embrapa, range_anos_embrapa

router = APIRouter()

desc_documentacao = (
    f"""
    <b>Dados de Importacao: "/importacao/ano/subcategoria"</b><br></b><br>
    <b>Possíveis valores</b><br>
    <b>ano:</b> {range_anos_embrapa[0]} a {range_anos_embrapa[1]}<br>
    <b>subcategoria:</b> {', '.join(abas_embrapa['importacao']['subcategorias'].keys())}
    """
)

@router.get("/importacao", include_in_schema=False)
async def importacao_root():
    """
    Rota informativa raiz para importacao.
    Retorna uma mensagem de erro informando que o ano e a subcategoria devem ser informados na URL.
    :return: Mensagem de erro.
    """
    raise HTTPException(
            status_code=400, 
            detail="Informe o ano e a subcategoria na URL: /importacao/{ano}/{subcategoria}"
        )

@router.get("/importacao/{ano}", include_in_schema=False)
async def importacao_ano(ano: int):
    """
    Rota informativa para importacao com ano informado.
    Retorna uma mensagem de erro informando que a subcategoria deve ser informada na URL.
    :param ano: Ano a ser informado.
    :return: Mensagem de erro.
    """
    raise HTTPException(
            status_code=400, 
            detail="Informe também a subcategoria na URL: /importacao/{ano}/{subcategoria}"
        )

@router.get("/importacao/{ano}/{subcategoria}", description=desc_documentacao, tags=["Importacao"])
async def get_importacao(ano: int, subcategoria: str) -> dict:
    """
    Rota para obter dados de importacao.
    :param ano: Ano a ser informado.
    :param subcategoria: Subcategoria a ser informada.
    :return: Dados de importacao.
    """
    aba = "importacao"
    
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