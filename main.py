from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes.welcome import router as welcome_router
from routes.processamento import router as processamento_router
from routes.processamento import desc_documentacao as desc_documentacao_processamento

app = FastAPI(
    title="API EMBRAPA",
    description=f"""
    Rotas válidas:
    {desc_documentacao_processamento.replace('<b>', '').replace('</b>', '').replace('<br>', '')}
    """,
    version="1.0.0"
)

app.include_router(welcome_router)
app.include_router(processamento_router)