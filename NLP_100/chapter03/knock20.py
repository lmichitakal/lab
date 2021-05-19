import json
import sys
json_open = open("jawiki-country.json", "r").readlines()
for line in json_open:
    now = json.loads(line)
    if now['title'] == 'イギリス':
        text = now['text']
        #print(text)
        #sys.exit()

