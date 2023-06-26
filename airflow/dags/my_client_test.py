# http://jsonplaceholder.typicode.com/posts

import requests
import json

API_ENDPOUNT = 'http://jsonplaceholder.typicode.com/posts'

def call_api():
    response = requests.get(url="http://jsonplaceholder.typicode.com/posts")
    print (f'response = {response}')
    print (f'status_code = {response.status_code}')