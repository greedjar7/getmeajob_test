from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.get_cv_db import cv_crud, cv_schema

router = APIRouter(
    prefix='/api/get_cv_db',
)

@router.get('/cv_list', response_model=list[cv_schema.CV])
def cv_list(db: Session=Depends(get_db)):
    _cv_list = cv_crud.get_cv_list(db)

    return _cv_list

@router.get('/detail/{cv_id}', response_model=cv_schema.CV)
def cv_detail(cv_id:int, db:Session=Depends(get_db)):
    cv = cv_crud.get_cv(db, cv_id=cv_id)
    
    return cv