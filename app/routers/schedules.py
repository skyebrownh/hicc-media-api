from fastapi import APIRouter, Depends

from app.models.schedule import ScheduleCreate, ScheduleUpdate, ScheduleOut 
from app.utils.supabase import SupabaseService
from app.dependencies import get_supabase_service

router = APIRouter(prefix="/schedules")

@router.get("/", response_model=list[ScheduleOut])
async def get_schedules(service: SupabaseService = Depends(get_supabase_service)):
    return service.get(table="schedules")

@router.get("/{id}", response_model=list[ScheduleOut])
async def get_schedule(id: str, service: SupabaseService = Depends(get_supabase_service)):
    return service.get(table="schedules", id=id)

@router.post("/", response_model=ScheduleOut)
async def post_schedules(schedule: ScheduleCreate, service: SupabaseService = Depends(get_supabase_service)):
    payload = schedule.model_dump(exclude_none=True)
    payload["month_start_date"] = payload["month_start_date"].isoformat()
    raw = service.post(table="schedules", body=payload)
    return ScheduleOut(**raw)

@router.patch("/{id}", response_model=ScheduleOut)
async def update_schedule(id: str, schedule: ScheduleUpdate, service: SupabaseService = Depends(get_supabase_service)):
    payload = schedule.model_dump(exclude_none=True)

    if "month_start_date" in payload:
        payload["month_start_date"] = payload["month_start_date"].isoformat()

    raw = service.update(table="schedules", body=payload, id=id)
    return ScheduleOut(**raw) 

@router.delete("/{id}", response_model=ScheduleOut)
async def delete_schedule(id: str, service: SupabaseService = Depends(get_supabase_service)):
    return service.delete(table="schedules", id=id)