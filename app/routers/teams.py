from fastapi import APIRouter, Depends

from app.models.team import TeamCreate, TeamUpdate, TeamOut 
from app.utils.supabase import SupabaseService
from app.dependencies import get_supabase_service

router = APIRouter(prefix="/teams")

@router.get("/", response_model=list[TeamOut])
async def get_teams(service: SupabaseService = Depends(get_supabase_service)):
    return service.get(table="teams")

@router.get("/{id}", response_model=list[TeamOut])
async def get_team(id: str, service: SupabaseService = Depends(get_supabase_service)):
    return service.get(table="teams", id=id)

@router.post("/", response_model=TeamOut)
async def post_teams(user: TeamCreate, service: SupabaseService = Depends(get_supabase_service)):
    return service.post(table="teams", body=user.model_dump(exclude_none=True))

@router.patch("/{id}", response_model=TeamOut)
async def update_team(id: str, user: TeamUpdate, service: SupabaseService = Depends(get_supabase_service)):
    return service.update(table="teams", body=user.model_dump(exclude_none=True), id=id)

@router.delete("/{id}", response_model=TeamOut)
async def delete_team(id: str, service: SupabaseService = Depends(get_supabase_service)):
    return service.delete(table="teams", id=id)