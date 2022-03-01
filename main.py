from fastapi import FastAPI
from routes.age_route import age_api_router

app = FastAPI()

app.include_router(age_api_router)
