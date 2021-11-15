from bs4 import *
import requests as rq
from csv import writer
import argparse

def main():
    pages = []
    cars = []
    models = []
    brands = []
    years = []
    page_name = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/50.0.2661.102 Safari/537.36'}

    # get ads' links of first n  page of bama
    for n in range(args.nop, 830, -1):
        url = 'https://bama.ir/car/all-brands/all-models/all-trims?pic=true&page=' + str(n)
        print(url)
        r = rq.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.select('div.title a')
        for l in links:
            pages.append(l['href'])

    # get info from each ad
    for p in pages:
        print(p)
        name = p.split('-')
        r2 = rq.get(p, headers=headers)
        soup2 = BeautifulSoup(r2.text, "html.parser")
        with open(args.path + str(name[1]) + '.html', 'w') as f:
            f.write(r2.text)
        tag = soup2.select('h1.addetail-title span')
        images = soup2.select("div.hidden-xs a img")
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

    # write images' link, name, brand of an ad to csv file
    with open(args.output_path, 'a') as f:
        wr = writer(f)
        for i in range(len(cars)):
            wr.writerow([page_name[i], cars[i], brands[i], models[i], years[i]])



def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nop', type=int, help='number of pages', default=850)
    parser.add_argument('--path', type=str, default='/home/hanieh/car/pages/',
                        help='path of a directory to save html pages')
    parser.add_argument('--output_path', type=str, default='/home/hanieh/car/carslist.csv',
                        help='path of the directory to save output')
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = parse_arguments()
    main()