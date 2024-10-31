from fastapi import HTTPException, status, UploadFile
from app.services import image_service

# Listar avatares
async def list_avatars():
    avatar_urls = await image_service.list_avatars()
    if avatar_urls is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error al obtener la lista de avatares"
        )
    return avatar_urls

# Subir un avatar
async def create_avatar(file: UploadFile):
    secure_url = await image_service.upload_avatar(file)
    if secure_url is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error al subir el avatar"
        )
    return secure_url
