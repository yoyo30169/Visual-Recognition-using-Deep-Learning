import json
import os

with open("result.json", "r+", encoding="utf-8") as f:
    data = json.load(f)


for i in range(0, len(data)):

    if data[i]['category_id'] == 10:
        data[i]['category_id'] = 0


with open('answer.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)
