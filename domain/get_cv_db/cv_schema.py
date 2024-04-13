import datetime

from pydantic import BaseModel

class CV(BaseModel):
    id: int
    company: str
    title: str
    detail: str
    href: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True