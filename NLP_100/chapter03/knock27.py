import re
from knock26 import dic_rm

def remove_il(text):
    pattern = r'\[\[(?:[^:\]]+?\|)?([^:]+?)\]\]'  # r"\[\[……\]\]" : 内部リンクと一致, (?:[^:\[]+?\|)? : 削除して良い文字列, 
    text = re.sub(pattern, r'\1', text)
    return text

#26
for k, v in dic_rm.items():
    print(k + ': ' + v)

print()
print('---------------')
print()

#27
dic_rm_il = {k: remove_il(v) for k, v in dic_rm.items()}
for k, v in dic_rm_il.items():
    print(k + ': ' + v)