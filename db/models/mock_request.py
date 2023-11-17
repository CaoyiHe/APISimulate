# api/db/models/mock_request.py

from sqlalchemy import Column, Integer, String, JSON, DateTime, func
from db.base import Base


class MockRequest(Base):
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String, index=True)
    response = Column(JSON)
    status_code = Column(Integer)
    timeout = Column(Integer)
    name = Column(String)
    creator = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
