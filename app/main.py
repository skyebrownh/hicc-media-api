from fastapi import FastAPI

from app.routers import * 

app = FastAPI()

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