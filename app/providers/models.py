from pydantic import BaseModel, ValidationError, validator
from typing import Optional

class AuthModel(BaseModel):
    url: str
    @validator('url')
    def name_must_contain_space(cls, url):
        if 'http' not in url:
            raise ValueError('url must be url')
        return url

class VkAuthModel(BaseModel):
    id:str
    first_name:str
    last_name:str
    url:str
    email:Optional[str] = None