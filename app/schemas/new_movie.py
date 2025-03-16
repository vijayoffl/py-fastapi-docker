from datetime import date
from pydantic import BaseModel

class NewMovieReleaseBase(BaseModel):
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
    ott_link: str

class NewMovieReleaseCreate(NewMovieReleaseBase):
    pass

class NewMovieRelease(NewMovieReleaseBase):
    id: int

    model_config = {
        "from_attributes": True  # Allows converting ORM objects to Pydantic models
    }
