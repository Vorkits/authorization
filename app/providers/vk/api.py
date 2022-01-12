   
# from app.api import crud
# from app.api.models import NoteDB, NoteSchema
from fastapi import APIRouter, HTTPException, Path, FastAPI,Depends
from typing import List 
from app.providers.models import AuthModel,VkAuthModel
from fastapi.responses import HTMLResponse,RedirectResponse
from app.providers.emaildb import EmailRedis
vk_router = APIRouter()
@vk_router.get("/", status_code=201,response_class=HTMLResponse)
async def create_note(data: AuthModel = Depends()):
    html_content=open('app/providers/vk/page.html').read()
    return HTMLResponse(content=html_content, status_code=200)

@vk_router.get("/result", status_code=201,response_class=RedirectResponse)
async def create_note(data: VkAuthModel = Depends()):
    email=(EmailRedis().get_email('VK',data.id))
    if not email:
        return RedirectResponse(url='https://github.com/tiangolo/fastapi/issues/199')
    return '200'
