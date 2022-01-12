   
# from app.api import crud
# from app.api.models import NoteDB, NoteSchema
from fastapi import APIRouter, HTTPException, Path, FastAPI,Depends
from typing import List 
from app.providers.models import AuthModel,VkAuthModel
from fastapi.responses import HTMLResponse,RedirectResponse
from app.providers.emaildb import EmailRedis
vk_router = APIRouter()


