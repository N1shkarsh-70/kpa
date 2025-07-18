from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import forms

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(forms.router)

