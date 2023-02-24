from fastapi import FastAPI
import random
from generator import generate

app=FastAPI();

for i in range(0,10):
    generate()

@app.get('/')
async def root():
    return "Bc"

@app.get('/dailyData')
async def dailyData():
    return "had hai bc"