from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models.new_movie import NewMovieReleaseDB
from app.schemas.new_movie import NewMovieRelease, NewMovieReleaseCreate
from ..models.upcoming import UpcomingReleaseDB  # Fixed import
from ..database import SessionLocal

router = APIRouter(prefix="/api/new-releases", tags=["New Releases"])

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=NewMovieRelease)
def create_release(release: NewMovieReleaseCreate, db: Session = Depends(get_db)):
    # Convert Pydantic model to dictionary
    new_movie_data = release.model_dump()

    # Create ORM instance
    new_movie = NewMovieReleaseDB(**new_movie_data)
    new_movie.created_date = datetime.utcnow() # Convert to IST
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)  # Ensure ID is included in the response

    return new_movie  # FastAPI automatically converts ORM to Pydantic model

@router.get("/{release_id}", response_model=NewMovieRelease)
def get_release(release_id: int, db: Session = Depends(get_db)):
    release = db.query(NewMovieReleaseDB).filter(NewMovieReleaseDB.id == release_id).first()  # Fixed ORM query
    if not release:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Release not found")
    return release

@router.get("/", response_model=List[NewMovieRelease])
def get_all_releases(db: Session = Depends(get_db)):
    releases = db.query(NewMovieReleaseDB).order_by(NewMovieReleaseDB.created_date.desc()).all()

    if not releases:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No upcoming releases found"
        )

    return releases


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_release(release_id: int, db: Session = Depends(get_db)):
    release = db.query(NewMovieReleaseDB).filter(NewMovieReleaseDB.id == release_id).first()

    if not release:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Release not found"
        )

    db.delete(release)
    db.commit()
    return {"message": "Release deleted successfully"}

