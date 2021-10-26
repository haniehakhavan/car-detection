from bs4 import *
import requests as rq
import csv

pages = []
cars = []
models = []
brands = []
years = []
page_name = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

for n in range (100,0,-1):
    url = 'https://bama.ir/car/all-brands/all-models/all-trims?pic=true&page='+str(n)
    print(url)
    r = rq.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.select('div.title a')
    for l in links:
        pages.append(l['href'])

for p in pages:
    print(p)
    name = p.split('-')
    r2 = rq.get(p, headers=headers)
    soup2 = BeautifulSoup(r2.text, "html.parser")
    with open('/home/hanieh/car/bama_pages/'+str(name[1])+'.html', 'w') as f:
        f.write(r2.text)
    tag = soup2.select('h1.addetail-title span')
    images= soup2.select("div.hidden-xs a img")
    if len(tag[0].find_all()) != 0:
        brand = tag[1].text
        model = tag[2].text
        year = tag[3].text
    else:
        brand = tag[0].text
        model = tag[1].text
        year = tag[2].text
    for img in images:
        if img['src'] not in cars:
            cars.append(img['src'])
            brands.append(brand)
            models.append(model)
            years.append(year)
            page_name.append(name[1])

with open('/home/hanieh/car/bama.csv', 'w') as f:
    writer = csv.writer(f)
    for i in range(len(cars)):
        writer.writerow([page_name[i], cars[i], brands[i], models[i], years[i]])
