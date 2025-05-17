from fastapi import FastAPI
# from routes.producao import get_producao
from routes.processamento import router as get_processamento

app = FastAPI()

# app.include_router(get_producao.router)
app.include_router(get_processamento)
