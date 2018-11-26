# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:30:35 2018

@author: KAZUKI
"""
import re
from collections import Counter

# 00 テキストの取得
target_text = """----------"""

# 01 文章を単語に分ける
# 複数の区切り文字を指定するため re.split を使う
words = re.split(r'\s|\,|\.|\(|\d+\)', target_text.lower())

# 02 集計する
counter = Counter(words)
print(len(counter))

# 03 表示する
# Counter#most_common を使って出現頻度の降順に csv 形式で表示する
for word, count in counter.most_common():
    if len(word) > 0:
        print("%s,%d" % (word, count))
        
        





