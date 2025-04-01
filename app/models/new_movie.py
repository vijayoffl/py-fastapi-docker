from sqlalchemy import Column, DateTime, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class NewMovieReleaseDB(Base):
    __tablename__ = "new_movies"

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
    ott_link = Column(String, nullable=False)
    streaming_date = Column(Date, nullable=False)
    created_date = Column(DateTime, nullable=False)
