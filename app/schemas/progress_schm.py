from pydantic import BaseModel
from typing import List, Optional


class ProgressBase(BaseModel):
    level: int
    type: str


class ProgressCreated(ProgressBase):
    exercises_completed: List[bool]


class ProgressUpdate(ProgressBase):
    exercises_completed: Optional[List[bool]] = None
    completed_at: Optional[str] = None


class ProgressOut(ProgressBase):
    id: int
    completed_at: Optional[str] = None
    score: float
    class Config:
        from_attributes = True
