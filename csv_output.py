# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 12:23:51 2018

@author: KAZUKI
"""
import re
from collections import Counter
import requests, uuid, json

target_text = """
-------------------------------------
"""

base_url = '----------------------'
path = '-------------------------------'
params = "&to=ja"
constructed_url = base_url + path + params

headers = {
    'Ocp-Apim-Subscription-Key': '----------------------------------',
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# 01 文章を単語に分ける
# 複数の区切り文字を指定するため re.split を使う
words = re.split(r'\s|\,|[^a-zA-Z]|\.|\)', target_text.lower())

# 出てきた単語の中で最も長い単語とその数を測る
max_len_element = max(words, key=len)
max_len_element_len = len(max_len_element)

# 02 集計する
counter = Counter(words)
counter_len = len(counter) - 1
print(  '単語数:%d' % len(counter))

# csv出力             
with open('output.csv', 'w') as f:             
 f.write("英単語")
 # csvなのでカンマで列を区切る
 f.write(',')
 f.write("意味")
 f.write(',')
 f.write("出た回数")
 f.write(',')
 f.write(str(counter_len))
 # 行の最後には改行を忘れないこと
 f.write('\n')
 for word, count in counter.most_common():
    if len(word) > 0:
                
        body = [{'text' : word}]
        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()
        result_ja = response[0]['translations'][0]['text']
        print(word)
        f.write(str(word))
        f.write(',')  
        f.write(str(result_ja))
        f.write(',')  
        f.write(str(count))
        f.write('\n')
# ファイルクローズ''''
f.close()
