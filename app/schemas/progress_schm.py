from pydantic import BaseModel
from typing import List, Optional


class ProgressBase(BaseModel):
    level: int
    type: str


class ProgressCreated(ProgressBase):
    correct: int
    incorrect: int


class ProgressUpdate(ProgressBase):
    completed_at: Optional[str] = None
    correct: Optional[int] = None
    incorrect: Optional[int] = None


class ProgressOut(BaseModel):
    id: int
    level: int
    type: str
    completed_at: str| None 
    correct: int
    total: int

    class Config:
        from_attributes = True
