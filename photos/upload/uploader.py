import os
import json

with open('uploadlist.json', 'r', encoding='utf-8') as f:
    d = json.loads(f.read())

for x, y in d.items():
    for item in y:
        name = item.split('/')[-1]
        upload_path = x + name
        os.system(f'b2 upload-file photosalbum  {item} {upload_path} > logs.txt')
# os.system(f'b2 upload-file photosalbum {item} {name} > logs.txt')
