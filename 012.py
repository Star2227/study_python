#存储数据
import json

filename = 'num.json'
with open(filename) as file_object:
    num = json.load(file_object)

print(num)
