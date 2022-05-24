from ast import Return
from flask import Flask  
app = Flask(__name__)    
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def hello(name):
    return f'Hi {name}'

@app.route('/repeat/<int:times>/<string:word>')
def repeat(times,word):
    return f'{word}\n'*times

@app.route('/<anything>')
def lost(anything):
    return 'Sorry! No Response. Try again.'


if __name__=="__main__":  
    app.run(debug=True) 
