from typing import List, Optional
from fastapi import FastAPI, Query
from fastapi . encoders import jsonable_encoder
from model . dbHandler import match_exact, match_like

app = FastAPI()

@app.get('/')
def index():
    """
    DEFAULT ROUTE
    this method will
    1. Provide usage instructions formated as JSON
    """
    return TODO

@app.get('/dict')
def dictionary():
    """
    DEFAULT ROUTE
    this method will
    1. Accept a word form the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approcimate matches and return
    """
    return TODO