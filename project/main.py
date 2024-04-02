import datetime


def decorator(func):
    def wrapper(*args, **kvargs):
        startTime = datetime.datetime.now()
        result = func(*args, **kvargs)
        print("Время исполнения:", datetime.datetime.now() - startTime)
        return result

    return wrapper


"""1. Отсортировать каждым из рассмотренных в лекции методом только положительные элементы массива, 
 оставив остальные элементы на своих местах. (не использовать дополнительный массив!)"""


def task_1_1(arr):
    print(f'Исходный список: {" ".join(str(el) for el in arr)}')
    result = lsd_sort(arr)

    print(f'Результат:       {" ".join(str(el) for el in [int(x) for x in result])}', '\n')
    return result

def lsd_sort(arr):
    if not arr:
        return []
    d = []
    m = []

    max_length = len(str(abs(max(arr, key=abs))))
    arr_s = fill_array_with_zeros(arr, max_length)

    for r in range(1, max_length + 1):
        for i in range(-9, 10):
            d = spread_numbers_into_bins(arr_s, i, r)
            m += d
            d.clear()

        arr_s = m.copy()
        m.clear()

    return [int(x) for x in arr_s]


def fill_array_with_zeros(arr, max_length):
    result_arr = []
    for num in arr:
        if num >= 0:
            processed_num = str(num).zfill(max_length)
        else:
            processed_num = '-' + str(abs(num)).zfill(max_length)
        result_arr.append(processed_num)
    return result_arr


def spread_numbers_into_bins(arr, bin, rank):
    result_arr = []
    for x in arr:
        coef = '-'
        if int(x) >= 0 or bin == 0:
            coef = ''
        if (coef + x[-rank]) == str(bin):
            result_arr.append(x)
    return result_arr


arr_1_1 = [ -333, 12, 24124, -1, -12, -232323,]
ans_1_1 = [-333, -12, -1, 12, 24124, 232323]
arr_1_2 = [3, -4, 1, -13, 11, -10]
ans_1_2 = [-13, -10, -4, 1, 3, 11]
arr_1_3 = [1, -2, -1, -2, 1]
ans_1_3 = [-2, -2, -1, 1, 1]
arr_1_4 = [-1000, -100000, -10, -13, 0]
ans_1_4 = [-100000, -1000, -13, -10, 0]
arr_1_5 = [0]
ans_1_5 = [0]

tests_arrs = [arr_1_1, arr_1_2, arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2, ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_1_1(tests_arrs[i]) == answers[i], '\n')
    task_1_1(tests_arrs[i])
print('-' * 20)

"""1. Отсортировать каждым из рассмотренных в лекции методом только положительные элементы массива,
 оставив остальные элементы на своих местах. (не использовать дополнительный массив!)"""


def task_1_2(arr):
    print(f'Исходный список: {" ".join(str(el) for el in arr)}')
    result = radix(arr)
    print(f'Результат:       {" ".join(str(el) for el in result)}', '\n')
    return [int(x) for x in result]

def radix(array, size=None, index=None):
    if not array:
        return array
    if size is None:
        size = len(str(abs(max(array, key=abs))))
    if index is None:
        index = size
    if index <= 0:
        return array

    bins = [[] for _ in range(19)]

    for e in array:
        coef = 1
        if e < 0:
            coef = -1

        num_with_zeros = str(abs(e)).zfill(size)
        dest_c = num_with_zeros[size - index]
        dest_i = int(dest_c)
        bins[9 + coef * dest_i ] += [e]

    result = []
    for b in bins:
        if b:
            result.append(radix(b, size, index - 1))

    flattened_result = flatten(result)
    return flattened_result


def flatten(array):
    new_array = []
    for sub_array in array:
        new_array += sub_array
    return new_array



arr_1_1 = [-333, 12, 24124, -1, -12, -232323]
ans_1_1 = [-232323, -333, -12, -1, 12, 24124]
arr_1_2 = [3, -4, 1, -13, 11, -10]
ans_1_2 = [-13, -10, -4, 1, 3, 11]
arr_1_3 = [1, -2, -1, -2, 1]
ans_1_3 = [-2, -2, -1, 1, 1]
arr_1_4 = [-1000, -100000, -10, -13, 0]
ans_1_4 = [-100000, -1000, -13, -10, 0]
arr_1_5 = [0]
ans_1_5 = [0]


tests_arrs = [arr_1_1, arr_1_2, arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2, ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_1_2(tests_arrs[i]) == answers[i], '\n')
    task_1_2(tests_arrs[i])
print('-' * 20)
