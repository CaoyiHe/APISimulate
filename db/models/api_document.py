# api/db/models/api_document.py

from sqlalchemy import Column, Integer, String, JSON
from db.base import Base

class APIDocument(Base):
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String, index=True, unique=True)
    fields = Column(JSON)
