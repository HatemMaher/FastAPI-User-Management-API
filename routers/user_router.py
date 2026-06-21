from fastapi import APIRouter, status, HTTPException

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
def users_index():
    return get_all_users()


@router.get("/{user_id}")
def users_show(user_id: int):

    user = get_user_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.post("/", status_code=status.HTTP_201_CREATED)
def users_store(user: UserCreate):

    new_user = create_user(user.name)

    return {
        "message": "User created",
        "data": new_user
    }

@router.put("/{user_id}")
def users_update(
    user_id: int,
    user: UserUpdate
):
    
    updated_user = update_user(
        user_id,
        user.name
    )

    if not updated_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    return {
        "messaage": "User updated successfully",
        "date": update_user
    }

@router.delete("/{user_id}")
def users_delet(user_id: int):

    deleted_user = delete_user(user_id)

    if not deleted_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {
        "message": "User deleted successfully",
        "data": deleted_user
    }