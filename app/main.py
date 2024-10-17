from fastapi import FastAPI
from app.routers import user_r
from app.database.db import create_db_and_tables

app = FastAPI()

# @app.on_event("startup")
# async def on_startup():
#      await create_db_and_tables()

# Incluir routers (rutas)
app.include_router(user_r.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Project!"}
