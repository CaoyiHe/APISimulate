# api/main.py

from fastapi import FastAPI
from api.v1.endpoints import mock
from core.config import settings

app = FastAPI()

# 包含 API 路由
app.include_router(mock.router, prefix="/mock", tags=["mock"])
