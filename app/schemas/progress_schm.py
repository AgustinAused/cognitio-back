from pydantic import BaseModel
from typing import List, Optional



class ProgressBase(BaseModel):
    user_id: int
    level: int


class ProgressCreated(ProgressBase):
    exercises: List[bool]
    completed_at: Optional[str] = None


class ProgressUpdate(ProgressBase):
    exercises: Optional[List[bool]]
    completed_at: Optional[str] = None


class ProgressOut(ProgressBase):
    id: int
    level: int
    exercises: List[bool]
    completed_at: Optional[str] = None

    class Config:
        orm_mode = True

