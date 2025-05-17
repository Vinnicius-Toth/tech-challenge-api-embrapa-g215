from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get(
    "/",
    response_class=HTMLResponse,
    summary="Página de boas-vindas",
    description="Exibe uma mensagem de boas-vindas para a API EMBRAPA.",
    tags=["Boas-vindas"],
)
def welcome():
    return "<h1>Bem-vindo à API EMBRAPA! - Para mais informações acesse a Rota '/docs'</h1>"