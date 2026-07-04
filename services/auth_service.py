from sqlalchemy.orm import Session

from database.models import User
from schemas.user_schema import UserCreate
from utils.hashing import hash_password
from database.models import User
from schemas.auth_schema import LoginRequest
from utils.hashing import verify_password


def register_user(db: Session, user: UserCreate):

    db_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        is_active=user.is_active
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def login_user(
    db: Session,
    credentials: LoginRequest
):

    user = (
        db.query(User)
        .filter(User.email == credentials.email)
        .first()
    )

    if not user:
        return None

    if not verify_password(credentials.password, user.password):
        return None

    return user