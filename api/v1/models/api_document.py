# api/api/v1/models/api_document.py

from pydantic import BaseModel

class APIDocument(BaseModel):
    path: str
    fields: list
    # 其他文档信息，例如是否必填、字符类型等
