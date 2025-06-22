from fastapi import APIRouter, Depends

from app.models.schedule_date_type import ScheduleDateTypeCreate, ScheduleDateTypeUpdate, ScheduleDateTypeOut 
from app.utils.supabase import SupabaseService
from app.dependencies import get_supabase_service

router = APIRouter(prefix="/schedule_date_types")

@router.get("/", response_model=list[ScheduleDateTypeOut])
async def get_schedule_date_types(service: SupabaseService = Depends(get_supabase_service)):
    return service.get(table="schedule_date_types")

@router.get("/{id}", response_model=list[ScheduleDateTypeOut])
async def get_schedule_date_type(id: str, service: SupabaseService = Depends(get_supabase_service)):
    return service.get(table="schedule_date_types", id=id)

@router.post("/", response_model=ScheduleDateTypeOut)
async def post_schedule_date_types(schedule_date_type: ScheduleDateTypeCreate, service: SupabaseService = Depends(get_supabase_service)):
    return service.post(table="schedule_date_types", body=schedule_date_type.model_dump(exclude_none=True))

@router.patch("/{id}", response_model=ScheduleDateTypeOut)
async def update_schedule_date_type(id: str, schedule_date_type: ScheduleDateTypeUpdate, service: SupabaseService = Depends(get_supabase_service)):
    return service.update(table="schedule_date_types", body=schedule_date_type.model_dump(exclude_none=True), id=id)

@router.delete("/{id}", response_model=ScheduleDateTypeOut)
async def delete_schedule_date_type(id: str, service: SupabaseService = Depends(get_supabase_service)):
    return service.delete(table="schedule_date_types", id=id)