# http://jsonplaceholder.typicode.com/posts

import requests
import json

API_ENDPOUNT = 'http://jsonplaceholder.typicode.com/posts'

def call_api():
    response = requests.get(url="http://jsonplaceholder.typicode.com/posts")
    print (f'response = {response}')
    print (f'status_code = {response.status_code}')

call_api()


# import urllib3

# API_ENDPOUNT = 'http://jsonplaceholder.typicode.com/posts'
# #resp = urllib3.request("GET", API_ENDPOUNT)
# resp = urllib3.request("GET", "https://httpbin.org/robots.txt")
# print (resp.status)
# print (resp.data)