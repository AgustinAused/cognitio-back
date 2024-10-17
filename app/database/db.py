from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL")

# Crear el motor asincrónico para la conexión
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Crear una sesión asincrónica
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Base para las clases de modelos
Base = declarative_base()

# Función para obtener la sesión de la base de datos
async def get_db():
    async with SessionLocal() as session:
        yield session

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

