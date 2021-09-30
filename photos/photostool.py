import json
from PIL import Image
import os


if __name__ == '__main__':
    result_json = []
    for item in os.listdir('./photoalbum'):
        if os.path.isdir('./photoalbum/'+item):
            dic = {'name': item, 'children': []}
            for x in os.listdir('./photoalbum/'+item):
                pic = Image.open('./photoalbum/'+item+'/'+x)
                height = pic.height
                width = pic.width
                dic['children'].append(f"{width}.{height} {x}")
            result_json.append(dic)
    with open('photoslist.json', 'w', encoding='utf-8') as f:
        json.dump(result_json, f, ensure_ascii=False, indent=4)


