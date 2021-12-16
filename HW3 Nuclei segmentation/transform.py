import json
import os

with open("answer.json", "r+", encoding="utf-8") as f:
    data = json.load(f)
print(data[0]["image_id"])

for i in range(0, len(data)):

    if data[i]["image_id"] == 1:
        data[i]["image_id"] = 3
    elif data[i]["image_id"] == 2:
        data[i]["image_id"] = 6
    elif data[i]["image_id"] == 3:
        data[i]["image_id"] = 1
    elif data[i]["image_id"] == 4:
        data[i]["image_id"] = 4
    elif data[i]["image_id"] == 5:
        data[i]["image_id"] = 2
    elif data[i]["image_id"] == 6:
        data[i]["image_id"] = 5
            


with open('answer.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)