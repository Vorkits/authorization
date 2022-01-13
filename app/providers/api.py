   
# from app.api import crud
# from app.api.models import NoteDB, NoteSchema
from calendar import c
from fastapi import APIRouter, HTTPException, Path, FastAPI,Depends
from typing import List 
from app.providers.models import AuthModel,ResultModel,get_return_url
from fastapi.responses import HTMLResponse,RedirectResponse
from app.providers.emaildb import EmailRedis
import httpx
result_router = APIRouter()

@result_router.get("/auth/result", status_code=201,response_class=RedirectResponse)
async def return_result(data: ResultModel = Depends()):
    if data.email:
        EmailRedis().set_email(data.provider,data.id,data.email)
        return RedirectResponse(url=get_return_url(dict(data),data.url))
    email_in_db=(EmailRedis().get_email(data.provider,data.id))
    if  not email_in_db:
        return RedirectResponse(url=get_return_url(dict(data),'/email/input'))
    data.email=email_in_db
    return RedirectResponse(url=get_return_url(dict(data),data.url))
    

@result_router.get("/{provider}", status_code=201,response_class=HTMLResponse)
async def auth_provider(provider:str,data: AuthModel = Depends()):
    html_content=open(f'app/providers/{provider}/page.html').read()
    return HTMLResponse(content=html_content, status_code=200)

@result_router.get("/email/input", status_code=201,response_class=HTMLResponse)
async def input_email(data: ResultModel = Depends()):
    html_content = open('app/providers/email.html').read()
    return HTMLResponse(content=html_content, status_code=200)

@result_router.get("/vk/cross", status_code=201,response_class=HTMLResponse)
async def auth_provider(code:str):
    print(code)
    r = httpx.get(f'https://api.vkontakte.ru/oauth/access_token?client_id=8048750&client_secret=EF4OzopruPvy1t2h770U&redirect_uri=https://ralae.com/vk/cross&code={code}')
    
    r = httpx.get(f'https://api.vkontakte.ru/method/getProfiles?uid={r.json.user_id}&access_token={r.json.access_token}&params=first_name,last_name,photo')
    return r.text