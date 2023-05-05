from fastapi import FastAPI,Depends,Body,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
import random
from generator import generate
from models.schema import UserSchema,biding,Create_bid,accept_bid,User_Solar_info
from fastapi.encoders import jsonable_encoder
import uuid 
from auth import auth_obj
import json
from settings.dbconnection import db


USER_COLLECTION='auth collection'

app=FastAPI();
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
    )

@app.post('/login')
async def login(formdata:OAuth2PasswordRequestForm=Depends()):
    if(auth_obj.UserCheck(formdata.username)==False):
        raise HTTPException(status_code=404,detail="user does not exist")
    if(auth_obj.VerifyPassword(formdata.username,formdata.password)==False):
        raise HTTPException(status_code=401,detail="wrong credentials")
    user_obj={
        "username":formdata.username,
    }
    token=auth_obj.Create_token(formdata.username);
    return {
        "access_token":token,
        "token_type":"bearer",
    }
@app.post('/signup')
async def signup(data:UserSchema=Body(...)):
    newdata = jsonable_encoder(data)
    Useruuid =str(uuid.uuid4())
    newdata=auth_obj.addUser(newdata,Useruuid)
    return True

@app.get('/new')
async def root():
    generate()
    return "hogaya"

@app.get('/dailyData')
async def dailyData(token:str=Depends(oauth2_scheme)):
    with open("daily.json",'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            return file_data
    return "error agaya"

@app.post('/biding')
async def binding(data:biding=Body(),token:str=Depends(oauth2_scheme)):
    uuid=auth_obj.get_current_user(token)
    print(uuid)
    user=db["auth collection"].find_one(
       {
        'uuid':str(uuid)
        }, 
        {
        '_id':0
        }
        )
    username=user["username"]

    db["biding_collection"].insert_one({
        'energy':data.Energy,
        "uuid":uuid,
        "user":username,
        "bids":[]
    })
    return username

@app.get('/all_bids')
async def all_bids(token:str=Depends(oauth2_scheme)):
    uuid=auth_obj.get_current_user(token)
    bids= db["biding_collection"].find_one(
        {
            "uuid":uuid,
        },
        {
            '_id':0
        }
    )
    new_bids=db["biding_collection"].find(
        {},
        {
            '_id':0
        }
    )

    return list(new_bids)

@app.post('/create_bid')
async def create_bid(data:Create_bid=Body(),token:str=Depends(oauth2_scheme)):
    uuid=auth_obj.get_current_user(token)
    print(data.Pricing)
    print(data.Bid_creator_id)
    original_id=db["biding_collection"].find_one({
        'uuid':data.Bid_creator_id
    },
    {
        '_id':0
    })
    user=db['auth collection'].find_one({
        'uuid':uuid
    },
    {
        '_id':0
    })
    bids=original_id['bids']
    bids.append({
        'bidder_id':uuid,
        'pricing_rate':data.Pricing,
        'bidder__name':user['username']

    })
    newdata={
        'bids':bids
    }
    db["biding_collection"].update_one({
        'uuid':data.Bid_creator_id
    }, {
        "$set":newdata
    })
    
    return bids

@app.post('/accept')
async def accept(data:accept_bid=Body(),token:str=Depends(oauth2_scheme)):
    uuid=auth_obj.get_current_user(token)
    db['biding_collection'].delete_one({
        'uuid':uuid
    })

    return data

@app.get('/get_id')
async def get_id(token:str=Depends(oauth2_scheme)):
    return auth_obj.get_current_user(token)

@app.post('/update_db')
async def update_db(data:User_Solar_info=Body(),token:str=Depends(oauth2_scheme)):
    uuid=auth_obj.get_current_user(token)
    x=db["solar_info"].find_one({
        "uuid":uuid,
    },{
        '_id':0
    })
    if(x):
        newdata={
        "uuid":uuid,
        "Total_watts":data.total_watts,
        "terrif_cost":data.terrif_cost,
        "operational_hours":data.operational_hours,

        }
        db['solar_info'].update_one({
           "uuid":uuid, 
        },{
        "$set":newdata
    })
    else:
        db["solar_info"].insert_one({
            "uuid":uuid,
            "Total_watts":data.total_watts,
            "terrif_cost":data.terrif_cost,
            "operational_hours":data.operational_hours,

        })
    return True

@app.get('/get_solar_data')
async def get_solar_data(token:str=Depends(oauth2_scheme)):
    uuid=auth_obj.get_current_user(token)
    x=db["solar_info"].find_one({
        "uuid":uuid,
    },{
        '_id':0
    })
    return {
        "total_watts":x['Total_watts'],
        "terrif_cost":x['terrif_cost'],
        "operational_hours":x['operational_hours'],
    }