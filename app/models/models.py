from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, REAL
from sqlalchemy.orm import relationship
from app.database.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

     # Relación con los niveles de progreso
    progress_levels = relationship("ProgressLevel", back_populates="user")


class ProgressLevel(Base):
    __tablename__ = 'progress_levels'

    id = Column(Integer, primary_key=True, index=True)
    level = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  
    completed_at = Column(DateTime, nullable=True)  

    ex1_completed = Column(Boolean, nullable=False, default=False)
    ex2_completed = Column(Boolean, nullable=False, default=False)
    ex3_completed = Column(Boolean, nullable=False, default=False)
    ex4_completed = Column(Boolean, nullable=False, default=False)
    ex5_completed = Column(Boolean, nullable=False, default=False)

    score = Column(REAL, nullable=False, default=0)

    # Relación con el usuario
    user = relationship("User", back_populates="progress_levels")



