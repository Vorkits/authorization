   
# from app.api import crud
# from app.api.models import NoteDB, NoteSchema
from fastapi import APIRouter, HTTPException, Path, FastAPI,Depends
from typing import List 
from app.providers.models import AuthModel,ResultModel
from fastapi.responses import HTMLResponse,RedirectResponse
from app.providers.emaildb import EmailRedis
result_router = APIRouter()

@result_router.get("/result", status_code=201,response_class=RedirectResponse)
async def return_result(data: ResultModel = Depends()):
    email=(EmailRedis().get_email(data.provider,data.id))
    if not email:
        return RedirectResponse(url='https://github.com/tiangolo/fastapi/issues/199')
    return '200'

@result_router.get("/{provider}", status_code=201,response_class=HTMLResponse)
async def auth_provider(provider:str,data: AuthModel = Depends()):
    html_content=open(f'app/providers/{provider}/page.html').read()
    return HTMLResponse(content=html_content, status_code=200)

