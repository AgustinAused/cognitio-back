from fastapi import APIRouter, UploadFile, HTTPException
from app.controllers import image_c

router = APIRouter()

@router.get("/avatars")
async def read_avatars():
    return await image_c.list_avatars()

@router.post("/avatars")
async def create_avatar(file: UploadFile):
    return await image_c.create_avatar(file)
