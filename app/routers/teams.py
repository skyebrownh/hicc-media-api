from fastapi import APIRouter

from app.models.team import TeamCreate, TeamUpdate, TeamOut 
from app.utils.supabase import supabase_get, supabase_post, supabase_update, supabase_delete

router = APIRouter(prefix="/teams")

@router.get("/", response_model=list[TeamOut])
async def get_teams():
    return supabase_get(table="teams")

@router.get("/{id}", response_model=list[TeamOut])
async def get_team(id: str):
    return supabase_get(table="teams", id=id)

@router.post("/", response_model=TeamOut)
async def post_teams(user: TeamCreate):
    return supabase_post(table="teams", body=user.model_dump(exclude_none=True))

@router.patch("/{id}", response_model=TeamOut)
async def update_team(id: str, user: TeamUpdate):
    return supabase_update(table="teams", body=user.model_dump(exclude_none=True), id=id)

@router.delete("/{id}", response_model=TeamOut)
async def delete_team(id: str):
    return supabase_delete(table="teams", id=id)