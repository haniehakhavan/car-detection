import csv
import os
import requests as rq
#
# with open('/home/hanieh/car/bama.csv', 'r') as f:
#     m = f.read()
# print(type(m))
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

links = []
for line in open('/home/hanieh/car/bama.csv'):
    csv_row = line.split()
    car = csv_row[0].split(',')
    links.append(car[1])
for index, l in enumerate(links):
    if index <= 7326:
        continue
    img = rq.get(l, headers=headers).content
    with open('/home/hanieh/car/images/'+str(index+1)+'.jpg', 'wb+') as f:
        f.write(img)


