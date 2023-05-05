from pydantic import BaseModel,Field

class UserSchema(BaseModel):
    email:str=Field(...)
    username:str=Field(...)
    password:str=Field(...)


class biding(BaseModel):
    Energy:int=Field(...)
    

class Create_bid(BaseModel):
    Pricing:int=Field(...)
    Bid_creator_id:str=Field(...)

class accept_bid(BaseModel):
    userid:str=Field(...)
    user:str=Field(...)
    Energy:str=Field(...)
    Bidder:str=Field(...)
    price:str=Field(...)

class User_Solar_info(BaseModel):
    total_watts:int=Field(...)
    terrif_cost:int=Field(...)
    operational_hours:int=Field(...)
