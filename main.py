from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from utils.utils import remover_tags_html

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

# Rota de exportação
from routes.exportacao import router as exportacao_router
from routes.exportacao import desc_documentacao as desc_documentacao_exportacao

app = FastAPI(
    title="API EMBRAPA",
    description=f"""
    |--Rotas válidas--|

    Boas-vindas (root): "/"
    Bem-vindo à API EMBRAPA!
    
    Processamento: 
    {remover_tags_html(desc_documentacao_processamento)}

    Comercialização:
    {remover_tags_html(desc_documentacao_comercializacao)}

    Produção:
    {remover_tags_html(desc_documentacao_producao)}

    Importação:
    {remover_tags_html(desc_documentacao_importacao)}

    Exportação:
    {remover_tags_html(desc_documentacao_exportacao)}
    """,
    version="1.0.0"
)


app.include_router(welcome_router)
app.include_router(producao_router)
app.include_router(processamento_router)
app.include_router(comercializacao_router)
app.include_router(importacao_router)
app.include_router(exportacao_router)