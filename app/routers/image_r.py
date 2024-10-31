from fastapi import APIRouter, UploadFile, HTTPException
from app.controllers import image_controller

router = APIRouter()

@router.get("/avatars")
async def read_avatars():
    return await image_controller.list_avatars()

@router.post("/avatars")
async def create_avatar(file: UploadFile):
    return await image_controller.create_avatar(file)
