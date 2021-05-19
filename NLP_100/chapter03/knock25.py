import re
import json
import gzip
from knock20 import text
# テンプレートの抽出
pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
template = re.findall(pattern, text, re.MULTILINE + re.DOTALL)
#print(template)

# フィールド名と値を辞書オブジェクトに格納
pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
dic = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))
#for k, v in dic.items():
#  print(k + ': ' + v)