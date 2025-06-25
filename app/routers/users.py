from fastapi import APIRouter, Depends, status

from app.models.user import UserCreate, UserUpdate, UserOut
from app.utils.supabase import SupabaseService
from app.dependencies import get_supabase_service

router = APIRouter(prefix="/users")

@router.get("/", response_model=list[UserOut])
async def get_users(service: SupabaseService = Depends(get_supabase_service)):
    return service.get_all(table="users")

@router.get("/{id}", response_model=UserOut)
async def get_user(id: str, service: SupabaseService = Depends(get_supabase_service)):
    return service.get_single(table="users", id=id)

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def post_users(user: UserCreate, service: SupabaseService = Depends(get_supabase_service)):
    return service.post(table="users", body=user.model_dump(exclude_none=True))

@router.patch("/{id}", response_model=UserOut)
async def update_user(id: str, user: UserUpdate, service: SupabaseService = Depends(get_supabase_service)):
    return service.update(table="users", body=user.model_dump(exclude_none=True), id=id)

@router.delete("/{id}", response_model=UserOut)
async def delete_user(id: str, service: SupabaseService = Depends(get_supabase_service)):
    return service.delete(table="users", id=id)