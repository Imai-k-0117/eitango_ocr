# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:15:12 2018

@author: KAZUKI
"""
import  requests 
import  json

# ‰æ‘œ“Ç‚İ‚İ
img_file_path = '----------.png'
img = open(img_file_path, 'rb')
img_byte = img.read()

ocr_url = '---------'
headers  = {'Ocp-Apim-Subscription-Key': '----------',"Content-Type": "application/octet-stream"}
params   = {'language': 'en', 'detectOrientation ': 'true'}

response = requests.post(ocr_url, headers=headers, params=params, data=img_byte)
response.raise_for_status()

ocr_data = response.json()


output = ""

for txt_lines in ocr_data['regions']:
    for txt_words in txt_lines['lines']:            
        for txt_word in txt_words['words']:
                output += txt_word['text']
                output += ' '
        output += '\n'
    output += '\n'
print('language:' + ocr_data['language'] + '\n')
print(output)

