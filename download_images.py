import csv
import os
import requests as rq
import argparse

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def main():
    links = []
    for line in open(args.images_link):
        csv_row = line.split()
        car = csv_row[0]
        links.append(car)
        for index, l in enumerate(links):
            img = rq.get(l, headers=headers).content
            with open(args.data_set + str(index + 1) + '.jpg', 'wb+') as f:
                f.write(img)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_set', type=str, help='path of dataset', default='/home/hanieh/car/images/')
    parser.add_argument('--images_link', type=str, help='path of images download link', default='/home/hanieh/car/bama2.csv')

    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = parse_arguments()
    main()
