arr = [1, 2, 3, 4, 6, 7, 9, 15, 33, 67, 290]


def sequencial_search(arr, item):
    counter = 0
    for index, it in enumerate(arr):
        counter += 1
        if item is it:
            print('item na posicao ', index, 'comparacoes ', counter)
            return


def binary_search(arr, begin, end, item, counter=1):
    i = (begin + end) // 2

    if begin > end:
        print('item nao encontrado' 'comparacoes ', counter)
        return
    if arr[i] is item:
        print('item encontrado na posicao', i, 'comparacoes ', counter)
    elif arr[i] < item:
        return binary_search(arr, i + 1, end, item, counter + 1)
    elif arr[i] > item:
        return binary_search(arr, begin, i - 1, item, counter + 1)


if __name__ == '__main__':
    item = 3
    sequencial_search(arr, item)
    binary_search(arr, 0, len(arr), item)
