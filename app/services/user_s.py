from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext
from app.models.models import User
from app.schemas.user_schm import UserCreate, UserUpdate
from app.utils.jwt import verify_token, create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

async def create_user(db: AsyncSession, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(email=user.email, password=hashed_password, image_url=user.image_url, username=user.username, is_active=True)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def authenticate_user(db: AsyncSession, email: str, password: str):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()
    if not user or not verify_password(password, user.password):
        return False
    return user

async def refresh_access_token(refresh_token: str):
    payload = verify_token(refresh_token)
    if not payload:
        return None
    email = payload.get("sub")
    if not email:
        return None
    return create_access_token(data={"sub": email})

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()

async def get_user_by_token(db: AsyncSession, tkn: str):
    payload = verify_token(tkn)
    if not payload:
        return None
    email = payload.get("sub")
    if not email:
        return None
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()

async def update_user(db: AsyncSession, user: UserUpdate, tkn: str):
    usr = await get_user_by_token(db, tkn)
    if not usr:
        return None

    if user.email is not None:
        usr.email = user.email
    if user.username is not None:
        usr.username = user.username
    if user.password is not None:
        usr.password = hash_password(user.password)
    if user.image_url is not None:
        usr.image_url = user.image_url

    await db.commit()
    await db.refresh(usr)
    return usr

async def update_user_image(db: AsyncSession, image: str, tkn: str):
    usr = await get_user_by_token(db, tkn)
    if not usr:
        return None
    usr.image_url = image
    await db.commit()
    await db.refresh(usr)
    return usr
