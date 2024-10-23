from pydantic import BaseModel
from typing import List, Optional


class ProgressBase(BaseModel):
    level: int


class ProgressCreated(ProgressBase):
    ex1_completed: bool
    ex2_completed: bool
    ex3_completed: bool
    ex4_completed: bool
    ex5_completed: bool
    completed_at: Optional[str] = None


class ProgressUpdate(ProgressBase):
    ex1_completed: Optional[bool] = None
    ex2_completed: Optional[bool] = None
    ex3_completed: Optional[bool] = None
    ex4_completed: Optional[bool] = None
    ex5_completed: Optional[bool] = None
    completed_at: Optional[str] = None


class ProgressOut(ProgressBase):
    id: int
    ex1_completed: bool
    ex2_completed: bool
    ex3_completed: bool
    ex4_completed: bool
    ex5_completed: bool
    completed_at: Optional[str] = None

    class Config:
        orm_mode = True
