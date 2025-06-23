from fastapi import FastAPI

from app.routers import * 

app = FastAPI()

app.include_router(users.router)
app.include_router(teams.router)
app.include_router(media_roles.router)
app.include_router(proficiency_levels.router)
app.include_router(schedule_date_types.router)
app.include_router(dates.router)
app.include_router(schedules.router)
app.include_router(user_availability.router)
app.include_router(team_users.router)
# app.include_router(user_roles.router)
# app.include_router(schedule_dates.router)
# app.include_router(schedule_date_roles.router)