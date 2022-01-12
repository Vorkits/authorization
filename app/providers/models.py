from pydantic import BaseModel, ValidationError, validator

class AuthModel(BaseModel):
    url: str
    @validator('url')
    def name_must_contain_space(cls, url):
        if 'http' not in url:
            raise ValueError('url must be url')
        return url