from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, REAL
from sqlalchemy.orm import relationship
from app.database.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    image_url = Column(String)
    is_active = Column(Boolean, default=True)

    # Relación con los niveles de progreso
    progress_levels = relationship("ProgressLevel", back_populates="user")


class ProgressLevel(Base):
    __tablename__ = 'progress_levels'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False, index=True)
    level = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  
    completed_at = Column(DateTime, nullable=True)  
    total = Column(Integer, nullable=False)
    correct = Column(Integer, nullable=False)

    # Relación con el usuario
    user = relationship("User", back_populates="progress_levels")



