   
# from app.api import crud
# from app.api.models import NoteDB, NoteSchema
from fastapi import APIRouter, HTTPException, Path, FastAPI,Depends
from typing import List 
from app.providers.models import AuthModel,VkAuthModel
from fastapi.responses import HTMLResponse

vk_router = APIRouter()
@vk_router.get("/", status_code=201,response_class=HTMLResponse)
async def create_note(data: AuthModel = Depends()):
    html_content=open('app/providers/vk/page.html').read()
    return HTMLResponse(content=html_content, status_code=200)

@vk_router.get("/result", status_code=201,response_class=HTMLResponse)
async def create_note(data: VkAuthModel = Depends()):
    html_content=open('app/providers/vk/page.html').read()
    return HTMLResponse(content=html_content, status_code=200)
