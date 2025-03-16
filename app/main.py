from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes.auth import router as auth_router
from .routes.upcoming import router as upcoming_router 
from .routes.new_movie import router as new_movie_router 



# This must come AFTER model imports
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allowed origins (use "*" to allow all)
origins = [
    "https://www.otttrackers.com",  # Your frontend URL
    "*",  # Allow all (only for testing, not recommended in production)
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specified domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


#app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(upcoming_router)
app.include_router(new_movie_router )