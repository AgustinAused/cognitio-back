import cloudinary
import cloudinary.uploader
import os
import cloudinary.api

# Configuration
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

# Función para listar avatares
async def list_avatars():
    try:
        # Obtiene todas las imágenes dentro de la carpeta 'avatars'
        resources = cloudinary.api.resources(type="upload", prefix="avatars/")
        # Extrae las URLs seguras de las imágenes
        avatar_urls = [resource['secure_url'] for resource in resources['resources']]
        return avatar_urls
    except Exception as e:
        print(f"Error al listar los avatares: {e}")
        return None

# Función para subir un avatar
async def upload_avatar(file):
    try:
        # Carga la imagen en Cloudinary
        upload_response = cloudinary.uploader.upload(file.file, folder="avatars/")
        # Obtiene la URL segura de la imagen
        secure_url = upload_response['secure_url']
        return secure_url
    except Exception as e:
        print(f"Error al subir el avatar: {e}")
        return None
    






