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
        return []






