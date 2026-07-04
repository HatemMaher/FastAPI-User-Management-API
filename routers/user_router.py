from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from database.database import get_db

from dependencies.auth import get_current_user
from database.models import User
from schemas.user_schema import  UserUpdate
from services.user_service import (
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
def users_index(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_users(db)


@router.get("/{user_id}")
def users_show(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# @router.post("/", status_code=status.HTTP_201_CREATED)
# def users_store(
#     user: UserCreate,
#     db: Session = Depends(get_db)
# ):

#     new_user = create_user(db, user)

#     return {
#         "message": "User created",
#         "data": new_user
#     }

@router.put("/{user_id}")
def users_update(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
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

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def users_delete(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    deleted_user = delete_user(db, user_id)

    if not deleted_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )