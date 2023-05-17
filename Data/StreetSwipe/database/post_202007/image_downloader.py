import requests
import os

file1 = open('./url.txt', 'r')
lines = file1.readlines()

for line in lines:
    obj = line.split("\n")[0]
    obj = obj.split(" ")
    id = obj[0]
    url = obj[1]

    response = requests.get(url)
    os.system("curl -o " + "./images/" + id + ".jpg " + url)

