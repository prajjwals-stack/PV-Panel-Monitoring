from pydantic import BaseModel,Field

class UserSchema(BaseModel):
    email:str=Field(...)
    username:str=Field(...)
    password:str=Field(...)


class biding(BaseModel):
    Energy:int=Field(...)
    Expiry_Time:str=Field(...)

class Create_bid(BaseModel):
    Pricing:int=Field(...)
    Bid_creator_id:str=Field(...)