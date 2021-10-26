from flask import Flask, request, jsonify
from werkzeug.wrappers import response
from model.dbHandler import match_exact, match_like 

app = Flask(__name__)

@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instructions formatted as JSON
    """
    response = {'usage': '/dict?=<word>'}
    
    return jsonify(response)

@app.get("/dict")
def dictionary():
    """
   DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match and return it if found
    3. If not found, find all approximate matches and return
    """
    word = request.args.get('word')

    #return an error querystring is malformed
    if not word:
        return jsonify({'data': 'No a valid word or no word provided'})

    #try to find an exact match
    definition = match_exact(word)
    if definition:
        return jsonify({'data': definition })

    #try to find an approximate match
    definitions = match_like(word)
    if definitions:
        return jsonify({'data': definitions})
    else:
        return jsonify({'data': 'word not found'})

        
        

    
    
     




if __name__ == "__main__":
    app.run()    