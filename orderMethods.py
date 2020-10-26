def sequencial_search(arr, item):
    counter = 1
    for index, it in enumerate(arr):
        if index == 0:
            continue
        if compare(item, it):
            print('Item encontrado na posicao ', index, 'com ', counter, ' comparações ')
            print(it)
            return
        counter += 1
    print('Item não encontrado com', counter, 'comparações ')


def binary_search(arr, item, begin=1, end=0, counter=1):
    if end == 0:
        end = len(arr) - 1

    i = (begin + end) // 2

    if begin > end:
        print('Item não encontrado com', counter, 'comparações ')
        return
    if compare(arr[i], item):
        print('Item encontrado na posicao ', i, 'com ', counter, ' comparações ')
        print(arr[i])
    elif arr[i] < item:
        return binary_search(arr, item, i + 1, end, counter + 1)
    elif arr[i] > item:
        return binary_search(arr, item, begin, i - 1, counter + 1)


def compare(a, b):
    return a.split(',')[0] == b.split(',')[0]
