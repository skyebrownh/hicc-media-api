from pydantic import BaseModel

class UserBase(BaseModel):
    user_id: str
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    phone: str | None = None
    is_active: bool | None = None