from fastapi import APIRouter

from app.models.user import UserCreate, UserUpdate, UserOut
from . import supabase

router = APIRouter(prefix="/users")

@router.get("/", response_model=list[UserOut])
async def get_users():
    return supabase.get(table="users")

@router.get("/{id}", response_model=list[UserOut])
async def get_user(id: str):
    return supabase.get(table="users", id=id)

@router.post("/", response_model=UserOut)
async def post_users(user: UserCreate):
    return supabase.post(table="users", body=user.model_dump(exclude_none=True))

@router.patch("/{id}", response_model=UserOut)
async def update_user(id: str, user: UserUpdate):
    return supabase.update(table="users", body=user.model_dump(exclude_none=True), id=id)

@router.delete("/{id}", response_model=UserOut)
async def delete_user(id: str):
    return supabase.delete(table="users", id=id)