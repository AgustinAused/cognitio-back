﻿from fastapi import FastAPI
from app.routers import user_r, game_r, progress_r, image_r
from fastapi.middleware.cors import CORSMiddleware
from app.database.db import create_db_and_tables, drop_db_and_tables

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def on_startup():
#      await drop_db_and_tables()
#      await create_db_and_tables()



# Incluir routers (rutas)
app.include_router(user_r.router,tags=['User'],prefix='/user')
app.include_router(game_r.router,tags=['Game'],prefix='/game')
app.include_router(progress_r.router,tags=['Progress'],prefix='/progress')
app.include_router(image_r.router,tags=['Image'],prefix='/image')


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Project!"}
