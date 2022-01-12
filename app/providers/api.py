   
# from app.api import crud
# from app.api.models import NoteDB, NoteSchema
from fastapi import APIRouter, HTTPException, Path, FastAPI,Depends
from typing import List 
from app.providers.models import AuthModel,ResultModel,get_return_url
from fastapi.responses import HTMLResponse,RedirectResponse
from app.providers.emaildb import EmailRedis
result_router = APIRouter()

@result_router.get("/auth/result", status_code=201,response_class=RedirectResponse)
async def return_result(data: ResultModel = Depends()):
    email=(EmailRedis().get_email(data.provider,data.id))
    if  email:
        return RedirectResponse(url='https://github.com/tiangolo/fastapi/issues/199')
    return RedirectResponse(url=get_return_url(dict(data),'/emailinput'))

@result_router.get("/{provider}", status_code=201,response_class=HTMLResponse)
async def auth_provider(provider:str,data: AuthModel = Depends()):
    html_content=open(f'app/providers/{provider}/page.html').read()
    return HTMLResponse(content=html_content, status_code=200)

