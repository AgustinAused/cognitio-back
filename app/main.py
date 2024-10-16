from fastapi import FastAPI
from app.routers import example_router

app = FastAPI()

# Incluir routers (rutas)
app.include_router(example_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Project Template!"}
