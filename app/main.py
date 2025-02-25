from fastapi import FastAPI
from app.database import Base, engine
from app.routes.auth import router as auth_router
from .routes.upcoming import router as upcoming_router 



# This must come AFTER model imports
Base.metadata.create_all(bind=engine)

app = FastAPI()

#app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(upcoming_router)