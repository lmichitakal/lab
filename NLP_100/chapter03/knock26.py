#import re
#from knock25 import dic
import re
import json
import gzip
from knock25 import dic

def remove_markup(text):
  # 強調マークアップの除去
  pattern = r'\'{2,5}'
  text = re.sub(pattern, '', text)

  return text

dic_rm = {k: remove_markup(v) for k, v in dic.items()}
#for k, v in dic_rm.items():
#    print(k + ': ' + v)