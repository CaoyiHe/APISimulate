# api/v1/endpoints/mock.py

from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.session import SessionLocal
from api.v1.models.mock_request import CreateMockRequestModel
from db.models.mock_request import MockRequest as DBMockRequest

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create_mock_request/")
def create_mock_request(mock_request: CreateMockRequestModel, db: Session = Depends(get_db)):
    db_mock_request = DBMockRequest(**mock_request.dict())
    db.add(db_mock_request)
    db.commit()
    db.refresh(db_mock_request)
    return {"message": "Mock request created successfully"}


@router.post("/add_mock_request/")
def add_mock_request(mock_request: CreateMockRequestModel, db: Session = Depends(get_db)):
    db_mock_request = DBMockRequest(**mock_request.dict())
    db.add(db_mock_request)
    db.commit()
    db.refresh(db_mock_request)
    return {"message": "Mock request added successfully"}


@router.get("/get_mock_response")
def get_mock_response(path: str, db: Session = Depends(get_db)):
    mock_request = db.query(DBMockRequest).filter(DBMockRequest.path == path).first()
    if not mock_request:
        raise HTTPException(status_code=404, detail="Mock request not found")

    return JSONResponse(content=mock_request.response, status_code=mock_request.status_code)
