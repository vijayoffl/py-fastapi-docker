from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UpcomingReleaseDB(Base):
    __tablename__ = "upcoming_releases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    year = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    ott = Column(String, nullable=False)
    cast = Column(String, nullable=False)
    landscape_image_url = Column(String, nullable=False)
    portrait_image_url = Column(String, nullable=False)
    director = Column(String, nullable=False)
    music = Column(String, nullable=False)
    streaming_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=True)
