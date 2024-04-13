import pandas as pd
from models import CV, NLP
from datetime import datetime
from database import SessionLocal

cv_db = pd.read_csv('./outputs/job_korea.csv')

db = SessionLocal()

for i in range(5, len(cv_db)):
    elem = cv_db.loc[i]
    company = elem['회사명']
    title = elem['채용공고 제목']
    detail = elem['채용공고 세부 사항']
    link = elem['링크']

    q = CV(company=company, title=title, detail=detail, href=link, create_date=datetime.now())
    db.add(q)
    db.commit()