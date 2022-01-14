   
# from app.api import crud
# from app.api.models import NoteDB, NoteSchema
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

@result_router.get("/vk/cross", status_code=201,response_class=RedirectResponse)
async def auth_provider(code:str,state:str):
    r = httpx.get(f'https://api.vkontakte.ru/oauth/access_token?client_id=8048750&client_secret=EF4OzopruPvy1t2h770U&redirect_uri=https://ralae.com/vk/cross&code={code}').json()
    r = httpx.get(f'https://api.vk.com/method/getProfiles?uid={r["user_id"]}&access_token={r["access_token"]}&params=first_name,last_name,photo,email&v=5.131').json()
    return RedirectResponse(url=get_return_url({
        "url":state,"first_name":r['response'][0]['first_name'],
        "last_name":r['response'][0]['last_name'],"id":r['response'][0]['id'],
        "provider":"vk"
        },'/auth/result'))
    
@result_router.get("/google/cross", status_code=201,response_class=RedirectResponse)
async def auth_provider(code:str,state:str):
    print(code,state)
    try:
        r = httpx.get(f'https://oauth2.googleapis.com/token?client_id=774858042763-al4j641acm78t9v97p712i8e5nll10o6.apps.googleusercontent.com&client_secret=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&redirect_uri=https://ralae.com/google/cross&code={code}&grant_type=authorization_code').json()
    except Exception as e:
        print(e)
    print(r)
    r = httpx.get(f'https://www.googleapis.com/auth/userinfo.profile?access_token={r["access_token"]}').json()
    print(r)
    return '200'
    # return RedirectResponse(url=get_return_url({
    #     "url":state,"first_name":r['response'][0]['first_name'],
    #     "last_name":r['response'][0]['last_name'],"id":r['response'][0]['id'],
    #     "provider":"vk"
    #     },'/auth/result'))