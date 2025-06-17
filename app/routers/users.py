from fastapi import APIRouter

from app.utils.supabase import supabase_get

router = APIRouter(prefix="/users")

@router.get("/")
async def get_users():
    return await supabase_get("users")