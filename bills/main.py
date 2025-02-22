from fastapi import FastAPI
from database import engine
import models
from routes import user_routes, bill_routes

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(user_routes.router)
app.include_router(bill_routes.router)
        