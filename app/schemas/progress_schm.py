from pydantic import BaseModel
from typing import List, Optional



class ProgressBase(BaseModel):
    level: int


class ProgressCreated(ProgressBase):
    completed_at: Optional[str] = None
    ex1_completed = bool
    ex2_completed = bool
    ex3_completed = bool
    ex4_completed = bool
    ex5_completed = bool


class ProgressUpdate(ProgressBase):
    completed_at: Optional[str] = None
    ex1_completed = Optional[bool]
    ex2_completed = Optional[bool]
    ex3_completed = Optional[bool]
    ex4_completed = Optional[bool]
    ex5_completed = Optional[bool]


class ProgressOut(ProgressBase):
    id: int
    level: int
    exercises: List[bool]
    completed_at: Optional[str] = None

    class Config:
        orm_mode = True

