from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
# from pydantic import RequestValidationError,PlainTextResponse
from app.providers.vk.api import vk_router
# from app.db import engine, metadata, database
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, ValidationError
# metadata.create_all(engine)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
     allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def startup():
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=422)
@app.exception_handler(ValueError)
async def value_error_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=422)

app.include_router(vk_router, prefix="/vk", tags=["vk"])
# app.include_router(notes.router, prefix="/notes", tags=["notes"])