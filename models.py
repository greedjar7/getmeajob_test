# Model 생성

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

# primary_key = 고유 키
# nullable = null값 허용여부
class CV(Base):
    __tablename__ = 'CV'

    id = Column(Integer, primary_key=True)
    company = Column(String, nullable=False)
    title = Column(String, nullable=False)
    detail = Column(String, nullable=False)
    href = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=False)

class NLP(Base):
    __tablename__ = 'NLP'
    id = Column(Integer, primary_key=True)
    company = Column(String, nullable=False)
    title = Column(String, nullable=False)
    detail = Column(String, nullable=False)
    href = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=False)