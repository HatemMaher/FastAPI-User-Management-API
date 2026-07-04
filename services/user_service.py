from sqlalchemy.orm import Session

from database.models import User
from schemas.user_schema import UserCreate




def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def create_user(db: Session, user: UserCreate):

    db_user = User(
        name=user.name,
        email=user.email,
        is_active=user.is_active
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user

def update_user(
    db: Session,
    user_id: int,
    name: str,
    email: str,
    is_active: bool
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        return None

    user.name = name
    user.email = email
    user.is_active = is_active
    db.commit()
    db.refresh(user)

    return user

def delete_user(
    db: Session,
    user_id: int
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        return None

    db.delete(user)
    db.commit()

    return user