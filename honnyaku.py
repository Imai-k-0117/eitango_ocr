# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 16:13:37 2018

@author: KAZUKI
"""

# -*- coding: utf-8 -*-
import requests, uuid, json

target_text = """----------"""

base_url = '--------------------------------'
path = '----------------------'
params = "&to=ja"
constructed_url = base_url + path + params

headers = {
    'Ocp-Apim-Subscription-Key': '-------------------',
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

body = [{
    'text' : target_text
}]

request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()

print(response[0]['translations'][0]['text'])











