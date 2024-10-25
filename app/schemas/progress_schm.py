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


class ProgressOut(ProgressBase):
    id: int
    completed_at: Optional[str] = None
    correct: int
    incorrect: int
    class Config:
        from_attributes = True
