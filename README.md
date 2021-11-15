# car-detection


<h3>bama</h3>
the code was written by python.
<br/>
the code crawls an ad website for cars.(bama.ir)
<br/>
it saves name of brand and model of cars, link of images, year that each car produced in.
<br/>

<h3>Table of Contents</h3>

- [Requirement](#requirement)
- [Usage](#usage)

## requerments

Python 3.8.5

## usage

after installing python you can run the script in terminal
<h3>bama</h3>
#### command:
```sh
python main.py --nop 'number of pages you want to crawl' --path 'path of directory you want to save html files of ads' --output_path 'path of file you want to save informtions'
```
#### example of command:
<code>python bama.py --nop 100 --path /home/hanieh/car/bama_pages/ --output_path /home/hanieh/car/bama.csv</code>

<h3>bama_crawler</h3>
#### command:
```sh
python main.py --nop 'number of pages you want to crawl' --output_path 'path of file you want to save informtions'
```
#### example of command:
<code>python bama.py --nop 100  --output_path /home/hanieh/car/bama.csv</code>


