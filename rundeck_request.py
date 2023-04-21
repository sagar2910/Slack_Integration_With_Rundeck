import requests
import json
from requests.auth import HTTPBasicAuth

headers={
    #'Content-Type':'application/json', 
    #'Accept':'application/json',
    'X-Rundeck-Auth-Token' : 'kJUIAvtWht594S56HxsHTk7W0JjUREsi'
}

url_post = "http://localhost:4440/api/11/job/1ea9039b-5f0c-4644-a5b6-b983f50b298d/run?kJUIAvtWht594S56HxsHTk7W0JjUREsi"

post_response = requests.post(url_post,
                              headers= headers
                            )

print(post_response)

print(post_response.status_code)
