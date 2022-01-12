from pydantic import BaseModel, ValidationError, validator
from typing import Optional

def get_return_url(data,url):
    url=url

class AuthModel(BaseModel):
    url: str
    @validator('url')
    def name_must_contain_space(cls, url):
        if 'http' not in url:
            raise ValueError('url must be url')
        return url

class ResultModel(BaseModel):
    id:str
    first_name:str
    last_name:str
    url:str
    email:Optional[str] = None
    provider:str