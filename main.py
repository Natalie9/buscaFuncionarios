import argparse

from orderMethods import *


def read_csv(path):
    arr = []
    with open(path) as f:
        for line in f:
            arr.append(line)
    return arr


def search(file, item):
    data = read_csv(file)
    print('Busca sequencial')
    sequencial_search(data, item)
    print('Busca binária')
    binary_search(data, item)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, default='docs/1000/crescente.csv')
    parser.add_argument('-n', type=str, default='Abbey',
                        help="['Digite um nome para busca como: ','Abbey', 'Nonie', 'Zack', 'Torrie']")
    args = parser.parse_args()

    search(args.f, args.n)
