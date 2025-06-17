from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    phone: str | None = None
    is_active: bool | None = None

class UserCreate(UserBase):
    first_name: str # type: ignore
    last_name: str # type: ignore
    phone: str # type: ignore

class UserUpdate(UserBase):
    pass

class UserOut(UserBase):
    user_id: str