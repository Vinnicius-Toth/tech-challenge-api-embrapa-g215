from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Rota de boas-vindas
from routes.welcome import router as welcome_router

# Rota de processamento
from routes.processamento import router as processamento_router
from routes.processamento import desc_documentacao as desc_documentacao_processamento

# Rota de comercialização
from routes.comercializacao import router as comercializacao_router
from routes.comercializacao import desc_documentacao as desc_documentacao_comercializacao

# Rota de produção
from routes.producao import router as producao_router
from routes.producao import desc_documentacao as desc_documentacao_producao

# Rota de importação
from routes.importacao import router as importacao_router
from routes.importacao import desc_documentacao as desc_documentacao_importacao

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

    Produção:
    {desc_documentacao_producao.replace('<b>', '').replace('</b>', '').replace('<br>', '')}

    Importação:
    {desc_documentacao_importacao.replace('<b>', '').replace('</b>', '').replace('<br>', '')}
    """,
    version="1.0.0"
)


app.include_router(welcome_router)
app.include_router(producao_router)
app.include_router(processamento_router)
app.include_router(comercializacao_router)
app.include_router(importacao_router)