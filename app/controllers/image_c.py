from fastapi import HTTPException, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import image_ser as image_s


# listar avatares
async def list_avatars():
    try:
        return await image_s.list_avatars()
    except Exception as e:
        print(f"Error al listar los avatares: {e}")
        raise HTTPException(status_code=400, detail="Error listing avatars")
    
# subir avatar
async def upload_avatar(file: UploadFile = File(...)):
    try:
        return await image_s.upload_avatar(file)
    except Exception as e:
        print(f"Error al subir el avatar: {e}")
