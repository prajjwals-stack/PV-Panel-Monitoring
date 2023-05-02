from fastapi import FastAPI,Depends,Body,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
import random
from generator import generate
from models.schema import UserSchema,biding
from fastapi.encoders import jsonable_encoder
import uuid 
from auth import auth_obj
import json
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
    return False