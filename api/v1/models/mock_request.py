# api/v1/models/mock_request.py

from pydantic import BaseModel


class CreateMockRequestModel(BaseModel):
    path: str
    response: dict
    status_code: int
    timeout: int
    name: str
    creator: str
