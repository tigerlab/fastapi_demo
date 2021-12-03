from django.db import models
from pydantic import BaseModel as _BaseModel
from typing import List, Optional
from datetime import date

class BaseModel(_BaseModel):
    @classmethod
    def from_orms(cls, instances: List[models.Model]):
        return [cls.from_orm(inst) for inst in instances]


class Contract(BaseModel):
    insurer: str
    number: str
    end_date: Optional[date] = None
    cancellation_date: Optional[date] = None
    publish_date: Optional[date] = None
    effective_date: Optional[date] = None
    payment_date: Optional[date] = None
     
    

    class Config:
        orm_mode = True


class Contracts(BaseModel):
    items: List[Contract]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=Contract.from_orms(qs))
