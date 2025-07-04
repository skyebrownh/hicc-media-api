from pydantic import BaseModel

class TeamBase(BaseModel):
    team_name: str | None = None
    is_active: bool | None = None
    lookup: str | None = None

class TeamCreate(TeamBase):
    # team_id is auto-generated by the DB
    team_name: str
    lookup: str 
    # is_active is defaulted by the DB

class TeamUpdate(TeamBase):
    pass

class TeamOut(TeamBase):
    team_id: str