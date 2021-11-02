import requests as rq
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--url', type=str, help='The url of the request', default='http://192.168.1.11:5347')
parser.add_argument('--test_set', type=str, help='path of testset', default='/home/hanieh/authena-test')
args = parser.parse_args()

embedding_url = args.url + '/embedding_file'
video_url = args.url + '/video'
for index in os.listdir(args.test_set):
    person = args.test_set + '/' + str(index)
    for p in os.listdir(person):
        tag = p.split('-')
        tag = tag[0].split('.')
        values = {'id': int(index), 'field': tag[0]}
        file_path = args.test_set + '/' + str(index) + '/' + p
        if tag[0] == "video":
            files = {'video': open(file_path, 'rb')}
            r = rq.post(video_url, files=files)
        else:
            files = {'image': open(file_path, 'rb')}
            r = rq.post(embedding_url, files=files, data=values)
        # print(r.__dict__)

verification_url = args.url + '/verification'
for index in os.listdir(args.test_set):
    req = rq.post(verification_url, json={"id": int(index)})
    print(req.__dict__)
    # print(index)








