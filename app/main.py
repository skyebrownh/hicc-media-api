from fastapi import FastAPI

from app.routers import users, teams, media_roles, proficiency_levels, schedule_date_types, dates

app = FastAPI()

app.include_router(users.router)
app.include_router(teams.router)
app.include_router(media_roles.router)
app.include_router(proficiency_levels.router)
app.include_router(schedule_date_types.router)
app.include_router(dates.router)