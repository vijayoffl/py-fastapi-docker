from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..models.upcoming import UpcomingReleaseDB  # Fixed import
from ..schemas.upcoming import UpcomingReleaseBase, UpcomingReleaseCreate, UpcomingRelease  # Keep Pydantic schema
from ..database import SessionLocal

router = APIRouter(prefix="/api/upcoming-releases", tags=["Upcoming Releases"])

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UpcomingRelease)
def create_release(release: UpcomingReleaseCreate, db: Session = Depends(get_db)):
    # Convert Pydantic model to dictionary
    new_movie_data = release.model_dump()

    # Create ORM instance
    new_movie = UpcomingReleaseDB(**new_movie_data)

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)  # Ensure ID is included in the response

    return new_movie  # FastAPI automatically converts ORM to Pydantic model

@router.get("/{release_id}", response_model=UpcomingRelease)
def get_release(release_id: int, db: Session = Depends(get_db)):
    release = db.query(UpcomingReleaseDB).filter(UpcomingReleaseDB.id == release_id).first()  # Fixed ORM query
    if not release:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Release not found")
    return release

# @router.get("/", response_model=List[UpcomingRelease])
# def get_all_releases(db: Session = Depends(get_db)):
#     releases = db.query(UpcomingReleaseDB).all()  # Fixed ORM query

#     if not releases:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="No upcoming releases found"
#         )

#     return releases

@router.get("/", response_model=List[UpcomingRelease])
def get_all_releases(db: Session = Depends(get_db)):
    releases = db.query(UpcomingReleaseDB).filter(UpcomingReleaseDB.is_active == True).all()

    if not releases:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No upcoming releases found"
        )

    return releases


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_release(release_id: int, db: Session = Depends(get_db)):
    release = db.query(UpcomingReleaseDB).filter(UpcomingReleaseDB.id == release_id).first()

    if not release:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Release not found"
        )

    db.delete(release)
    db.commit()
    return {"message": "Release deleted successfully"}

