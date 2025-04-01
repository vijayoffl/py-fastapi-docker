from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel

class UpcomingReleaseBase(BaseModel):
    name: str
    year: str
    genre: str
    ott: str
    cast: str
    landscape_image_url: Optional[str] = None  # Allows null values
    portrait_image_url: str
    director: str
    music: str
    streaming_date: date
    is_active: bool
    created_date: datetime

class UpcomingReleaseCreate(UpcomingReleaseBase):
    pass

class UpcomingRelease(UpcomingReleaseBase):
    id: int

    model_config = {
        "from_attributes": True  # Allows converting ORM objects to Pydantic models
    }
