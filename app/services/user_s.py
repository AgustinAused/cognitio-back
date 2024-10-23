from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import User
from app.schemas.user_schm import UserCreate
from app.utils.jwt import create_access_token, verify_token
from sqlalchemy.sql.expression import select

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
        return pwd_context.hash(password)

async def create_user(db: AsyncSession, user: UserCreate):
        hashed_password = hash_password(user.password)
        db_user = User(email=user.email, password=hashed_password, username=user.username, is_active=True)
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user

async def authenticate_user(db: AsyncSession, email: str, password: str):
        user = await db.execute(select(User).where(User.email == email))
        user = user.scalars().first()
        if not user:
            return False
        if not verify_password(password, user.password):
            return False
        return user

async def refresh_access_token(refresh_token: str):
        payload = verify_token(refresh_token)
        if not payload:
            return None
        email = payload.get("sub")
        if not email:
            return None
        new_access_token = create_access_token(data={"sub": email})
        return new_access_token


async def get_user(db: AsyncSession, user_id: int = None):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    return user

async def get_user_by_token(db: AsyncSession, tkn: str):
        payload = verify_token(tkn)
        if not payload:
                return None
        email = payload.get("sub")
        if not email:
                return None
        user = await db.execute(select(User).where(User.email == email))
        user = user.scalars().first()
        return user
