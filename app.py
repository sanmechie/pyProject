'''
A simple rest API to demonstrate GHA
'''
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello():
    '''
    A return a success message
    '''
    return 'success'
