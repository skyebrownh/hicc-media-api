from datetime import date

from pydantic import BaseModel

class DateBase(BaseModel):
    calendar_year: int | None = None
    calendar_month: int | None = None
    month_name: str | None = None
    month_abbr: str | None = None
    calendar_day: int | None = None
    weekday: int | None = None
    weekday_name: str | None = None
    is_weekend: bool | None = None
    is_weekday: bool | None = None
    is_holiday: bool | None = None
    week_number: int | None = None
    is_first_of_month: bool | None = None
    is_last_of_month: bool | None = None
    calendar_quarter: int | None = None
    weekday_of_month: int | None = None 

class DateCreate(DateBase):
    date: date
    # all other fields are either optional or defaulted

class DateUpdate(DateBase):
    pass

class DateOut(DateBase):
    date: date