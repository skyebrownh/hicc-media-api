from fastapi import FastAPI, Request, HTTPException, status

from app.routers import * 
from app.utils.env import FAST_API_KEY

app = FastAPI()

@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    api_key = request.headers.get("x-api-key")
    if not api_key:
        api_key = ""

    if api_key.strip().lower() != FAST_API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized: Invalid or missing API Key")
    
    response = await call_next(request)
    return response

app.include_router(user_router)
app.include_router(team_router)
app.include_router(media_role_router)
app.include_router(proficiency_level_router)
app.include_router(schedule_date_type_router)
app.include_router(date_router)
app.include_router(schedule_router)
app.include_router(user_availability_router)
app.include_router(team_user_router)
app.include_router(user_role_router)
app.include_router(schedule_date_router)
app.include_router(schedule_date_role_router)