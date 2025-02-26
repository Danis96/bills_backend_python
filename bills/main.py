from fastapi import FastAPI
from routes import user_routes, bill_routes, auth_routes
from database import engine
from models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(user_routes.router)
app.include_router(bill_routes.router)
app.include_router(auth_routes.router)
app.include_router(auth_routes.token_router)
        