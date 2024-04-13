from models import CV
from sqlalchemy.orm import Session

def get_cv_list(db: Session):
    cv_list = db.query(CV).order_by(CV.create_date.desc()).all()
    return cv_list

def get_cv(db:Session, cv_id:int):
    cv = db.query(CV).get(cv_id)
    return cv