import requests as rq
from csv import writer
import argparse


def main():
    cars_image = []
    models = []
    brands = []
    years = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/50.0.2661.102 Safari/537.36'}
    # get ads' links of first n  page of bama
    for n in range(args.nop, 760, -1):
        url = 'https://bama.ir/car/search?pageIndex=' + str(n) + '&image=1'
        print(url)
        r = rq.get(url, headers=headers)
        print(r.json()['data'])
        cars = r.json()['data']['car_ads']
        for car in cars:
            title = car['detail']['title'].split('،')
            model = title[1]
            brand = title[0]
            images = car['detail']['images']
            year = car['detail']['year']
            for i in images:
                cars_image.append(i['large'])
                years.append(year)
                brands.append(brand)
                models.append(model)
    # #write images, name, brand of an ad to csv file
    with open(args.output_path, 'a') as f:
        wr = writer(f)
        for i in range(len(cars_image)):
            wr.writerow([cars_image[i], brands[i], models[i], years[i]])


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nop', type=int, help='number of pages', default=765)
    parser.add_argument('--output_path', type=str, default='/home/hanieh/car/carslist.csv',
                        help='path of the directory to save output')

    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = parse_arguments()
    main()
