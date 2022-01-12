from pydantic import BaseModel, ValidationError, validator
from typing import Optional
import validators
def get_return_url(data,url):
    params='?'
    for param in data:
        params+=f'{param}={data[param]}&'
    return url+params

class AuthModel(BaseModel):
    url: str
    @validator('url')
    def name_must_contain_space(cls, url):
        url_valid=validators.url(url)
        if  not url_valid:
            raise ValueError('url must be url')
        return url

class ResultModel(BaseModel):
    id:str
    first_name:str
    last_name:str
    url:str
    email:Optional[str] = None
    image:Optional[str] = None
    provider:str