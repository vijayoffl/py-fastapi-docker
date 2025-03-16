from datetime import date
from pydantic import BaseModel

class UpcomingReleaseBase(BaseModel):
    name: str
    year: str
    genre: str
    ott: str
    cast: str
    landscape_image_url: str
    portrait_image_url: str
    director: str
    music: str
    streaming_date: date
    is_active: bool

class UpcomingReleaseCreate(UpcomingReleaseBase):
    pass

class UpcomingRelease(UpcomingReleaseBase):
    id: int

    model_config = {
        "from_attributes": True  # Allows converting ORM objects to Pydantic models
    }
