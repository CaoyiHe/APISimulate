# api/api/v1/endpoints/api_document.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import SessionLocal
from api.v1.models.api_document import APIDocument as APIDocumentModel
from db.models.api_document import APIDocument as DBAPIDocument

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/import_api_document/")
def import_api_document(api_document: APIDocumentModel, db: Session = Depends(get_db)):
    db_api_document = DBAPIDocument(**api_document.dict())
    db.add(db_api_document)
    db.commit()
    db.refresh(db_api_document)
    return {"message": "API document imported successfully"}


@router.post("/validate_request/")
def validate_request(path: str, request_data: dict, db: Session = Depends(get_db)):
    api_document = db.query(DBAPIDocument).filter(DBAPIDocument.path == path).first()
    if not api_document:
        raise HTTPException(status_code=404, detail="API document not found")

    # 在这里实现对请求数据的验证逻辑，比如检查字段是否一致、必填项是否存在等

    return {"message": "Request is valid"}
