import re
from knock20 import text
#print(text)
texts = text.split('\n')
pattern = re.compile('\|(.+?)\s=\s*(.+)')
dic = {}
for line in texts:
    r = re.search(pattern, line)
    if r:
        dic[r[1]] = r[2]
print(dic)
