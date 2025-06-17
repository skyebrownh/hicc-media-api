from fastapi import APIRouter

from app.models.user import UserBase
from app.utils.supabase import supabase_get, supabase_post, supabase_update, supabase_delete

router = APIRouter(prefix="/users")

@router.get("/")
async def get_users():
    return supabase_get("users")

@router.post("/")
async def post_users(user: UserBase):
    return supabase_post("users", body=user.model_dump())