from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import api_route

app = FastAPI()

version = 'v1'

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(api_route, prefix=f"/api/{version}/tasks", tags=['books'])
