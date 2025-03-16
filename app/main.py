from fastapi import FastAPI
from app.database import Base, engine
from app.routes.auth import router as auth_router
from .routes.upcoming import router as upcoming_router 
from .routes.new_movie import router as new_movie_router 



# This must come AFTER model imports
Base.metadata.create_all(bind=engine)

app = FastAPI()

#app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(upcoming_router)
app.include_router(new_movie_router )