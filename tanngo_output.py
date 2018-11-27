# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:30:35 2018

@author: KAZUKI
"""

import re
from collections import Counter
import requests, uuid, json
# 00 テキストの取得
target_text = """
-------------------------
"""

base_url = '------------------------------------'
path = '------------------------------'
params = "&to=ja"
constructed_url = base_url + path + params

headers = {
    'Ocp-Apim-Subscription-Key': '-------------------------------',
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# 01 文章を単語に分ける
# 複数の区切り文字を指定するため re.split を使う
words = re.split(r'\s|\,|\.|\(|\d+\)', target_text.lower())

# 出てきた単語の中で最も長い単語とその数を測る
max_len_element = max(words, key=len)
max_len_element_len = len(max_len_element)
#print(max_len_element)
#print(max_len_element_len)

# 02 集計する
counter = Counter(words)
counter_len = len(counter)
print(  '単語数:%d' % len(counter))

"""for i in words:
   if len(i) > 0:
      i_len = len(i)
      gap   = max_len_element_len - i_len
      print(i,end="")
      
      for k in range(gap):
          print(end=" ")
      print("|")
"""

# 03 表示する
# Counter#most_common を使って出現頻度の降順に csv 形式で表示する

for word, count in counter.most_common():
    if len(word) > 0:
                
        body = [{'text' : word}]
        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()
        result_ja = response[0]['translations'][0]['text']
        
        #for i in word:
        i_len = len(word)
        gap   = max_len_element_len - i_len
        print(word,end="")
                 
        for k in range(gap):
                    print(end=" ")
                    
        print("|", end="")
        
        w_len = len(result_ja)
        #print(w_len,end="")
        w_gap   = max_len_element_len - w_len
        print(result_ja,end="")
        
        for k in range(w_gap):
                    print(" ",end="")
                    
        print("|", end="")         
        
        print(" %d回"   %  count)
                 
                 
                 

        















