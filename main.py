from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Rota de boas-vindas
from routes.welcome import router as welcome_router

# Rotas de processamento
from routes.processamento import router as processamento_router
from routes.processamento import desc_documentacao as desc_documentacao_processamento

# Rotas de comercialização
from routes.comercializacao import router as comercializacao_router
from routes.comercializacao import desc_documentacao as desc_documentacao_comercializacao

app = FastAPI(
    title="API EMBRAPA",
    description=f"""
    |--Rotas válidas--|

    Boas-vindas (root): "/"
    Bem-vindo à API EMBRAPA!
    
    Processamento: 
    {desc_documentacao_processamento.replace('<b>', '').replace('</b>', '').replace('<br>', '')}

    Comercialização:
    {desc_documentacao_comercializacao.replace('<b>', '').replace('</b>', '').replace('<br>', '')}
    """,
    version="1.0.0"
)

app.include_router(welcome_router)
app.include_router(processamento_router)
app.include_router(comercializacao_router)