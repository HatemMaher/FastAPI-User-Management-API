from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from database.database import get_db

from schemas.user_schema import UserCreate, UserUpdate
from services.user_service import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
def users_index(
    db: Session = Depends(get_db)
):
    return get_all_users(db)


@router.get("/{user_id}")
def users_show(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.post("/", status_code=status.HTTP_201_CREATED)
def users_store(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = create_user(db, user)

    return {
        "message": "User created",
        "data": new_user
    }

@router.put("/{user_id}")
def users_update(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    
    updated_user = update_user(
        db,
        user_id,
        user.name,
        user.email,
        user.is_active
    )

    if not updated_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    return {
        "message": "User updated successfully",
        "data": updated_user
    }

@router.delete("/{user_id}")
def users_delete(user_id: int, db: Session = Depends(get_db)):

    deleted_user = delete_user(db, user_id)

    if not deleted_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {
        "message": "User deleted successfully",
        "data": deleted_user
    }