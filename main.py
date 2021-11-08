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
    response = {'usage': '/dict?=<word>'}
    return jsonable_encoder(response)

@app.get('/dict')
def dictionary(word: str):
    """
    DEFAULT ROUTE
    this method will
    1. Accept a word form the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approcimate matches and return
    """
    if not word:
        response = {'status': 'error',
                    'word': word,
                    'data': 'word not found'}
    
        return jsonable_encoder(response)
    
    definitions = match_exact(word)
    if definitions:
        response = {'status': 'success',
                    'word': word,
                    'data': definitions}
        return jsonable_encoder(response)
        
    
    #try to find an approximate match
    definitions = match_like(word)
    if definitions:
        response  = {'status': 'partia',
                    'word': word,
                    'data': definitions}
        return jsonable_encoder(response)
                    
    else:
        response = {'status': 'error',
                    'word': word,
                    'data': 'word not found'}
        return jsonable_encoder(response)
            