import pandas as pd
import argparse

def main():
    df = pd.read_csv('/home/hanieh/car/bama.csv')
    m = df.value_counts(["brand", "model"])
    print(type(m))
    m.to_csv('/home/hanieh/car/counter.csv')


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_path', type=str, help='path of csv file ', default='/home/hanieh/car/bama.csv')
    parser.add_argument('--result', type=str, help='path of result file', default='/home/hanieh/car/counter.csv')

    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = parse_arguments()
    main()