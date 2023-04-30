from pydantic import BaseModel,Field

class UserSchema(BaseModel):
    email:str=Field(...)
    username:str=Field(...)
    password:str=Field(...)