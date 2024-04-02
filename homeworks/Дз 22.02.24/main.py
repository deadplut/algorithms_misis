import datetime


def decorator(func):
    def wrapper(*args, **kvargs):
        startTime = datetime.datetime.now()
        result = func(*args, **kvargs)
        print("Время исполнения:", datetime.datetime.now() - startTime)
        return result

    return wrapper


"""1. Бинарный поиск"""

def task_1(*args):
    arr = args[0]
    x = args[1]
    print(f'Исходный список: {" ".join(str(el) for el in arr)}')
    print(f'Исходный число: {x}')

    i1 = 0
    i2 = len(arr) - 1

    while i2 >= i1:
        i = (i1 + i2) // 2
        if x == arr[i]:
            break

        if x < arr[i]:
            i2 = i - 1
            continue
        i1 = i + 1
    else:
        i = None

    print(f'Результат: {i} (индекс)', '\n')



arr_1_1 = [[1, 2, 3, 4, 5, 6, 7, 8], 7]
ans_1_1 = 6
arr_1_2 = [[-10, -9, -8, -7, -6, -5], -10]
ans_1_2 = 0
arr_1_3 = [[1, 2, 3, 4, 5, 6, 7, 8], 8]
ans_1_3 = 7
arr_1_4 = [[1, 2, 3, 4, 5, 6, 7, 8], 120]
ans_1_4 = None
arr_1_5 = [[1, 2, 3, 4, 5, 6, 7, 8], 0]
ans_1_5 = None


tests_arrs = [arr_1_1, arr_1_2,arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2,ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_1(*tests_arrs[i]) == answers[i], '\n')
    task_1(*tests_arrs[i])
print('-'* 20)


"""2. Объединение двух массивов с чередованием элементов"""


def task_2(*args):
    result = [None] * (len(args[0]) + len(args[1]))
    arr1, arr2 = args[0], args[1]

    print(f'Исходный чётный список: {" ".join(str(el) for el in arr1)}')
    print(f'Исходный чётный список: {" ".join(str(el) for el in arr2)}')

    diff = len(arr1) - len(arr2)
    if diff >= 0:
        longest_arr = arr1
        length_shortest_arr = len(arr2)
    else:
        diff = diff * (-1)
        longest_arr = arr2
        length_shortest_arr = len(arr1)

    for i in range(1, diff + 1):
        result[-i] = longest_arr[-i]

    for i in range(length_shortest_arr):
        result[i * 2] = arr1[i]
        result[(i * 2) + 1] = arr2[i]

    print(f'Результат: {" ".join(str(el) for el in result)}', '\n')

    return result




arr_1_1 = [[1, 2, 3, 4], [-1, -2, -3, -4]]
ans_1_1 = [1, -1, 2, -2, 3, -3, 4, -4]
arr_1_2 = [[0, 0, 0], [1, 1, 1, 1, 10]]
ans_1_2 = [0, 1, 0, 1, 0, 1, 1, 10]
arr_1_3 = [[11, 1, 1, 1, 10], [0, 0, 0]]
ans_1_3 = [11, 0, 1, 0, 1, 0, 1, 10]
arr_1_4 = [[0], [-1]]
ans_1_4 = [0, -1]
arr_1_5 = [[], []]
ans_1_5 = []


tests_arrs = [arr_1_1, arr_1_2,arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2,ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_2(*tests_arrs[i]) == answers[i], '\n')
    task_2(*tests_arrs[i])
print('-'* 20)


def task_3(*args):
    result = [None] * (len(args[0]) + len(args[1]))
    arr1, arr2 = args[0], args[1]

    print(f'Исходный первый список: {" ".join(str(el) for el in arr1)}')
    print(f'Исходный второй список: {" ".join(str(el) for el in arr2)}')

    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):

        if arr1[i] >= arr2[j]:
            result[i + j] = arr1[i]
            i += 1
        else:
            result[i + j] = arr2[j]
            j += 1
    else:
        longest_arr = []
        start = 0
        sec_ind = 0

        if i < len(arr1):
            longest_arr = arr1
            start = i
            sec_ind = j
        if j < len(arr2):
            longest_arr = arr2
            start = j
            sec_ind = i

        for l in range(start, len(longest_arr)):
            result[l + sec_ind] = longest_arr[l]

    print(f'Результат: {" ".join(str(el) for el in result)}', '\n')

    return result


arr_1_1 = [[4, 3, 2, 1], [4, 3, -2, -4]]
ans_1_1 = [4, 4, 3, 3, 2, 1, -2, -4]
arr_1_2 = [[0, 0, 0], [10, 1, 1, 1, 1]]
ans_1_2 = [10, 1, 1, 1, 1, 0, 0, 0]
arr_1_3 = [[11, 9, 7, 5, 3, 1], [8, 6, 4, 2]]
ans_1_3 = [11, 9, 8, 7, 6, 5, 4, 3, 2, 1]
arr_1_4 = [[0], [-1]]
ans_1_4 = [0, -1]
arr_1_5 = [[], []]
ans_1_5 = []


tests_arrs = [arr_1_1, arr_1_2,arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2,ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_3(*tests_arrs[i]) == answers[i], '\n')
    task_3(*tests_arrs[i])
print('-'* 20)


# 4 Инвертирование массива

def task_4(arr1):
    print(f'Исходный первый список: {" ".join(str(el) for el in arr1)}')


    i = 0
    while i < (len(arr1) / 2):
        arr1[i], arr1[(-1) * (i + 1)] = arr1[ (-1) * (i + 1)], arr1[i]
        i += 1

    print(f'Результат: {" ".join(str(el) for el in arr1)}', '\n')

    return arr1


arr_1_1 = [1,2,3,4,5,6,7]
ans_1_1 = [7,6,5,4,3,2,1]
arr_1_2 = [1, 2, 3, 4]
ans_1_2 = [4, 3, 2, 1]
arr_1_3 = [0]
ans_1_3 = [0]
arr_1_4 = [-1, -2]
ans_1_4 = [-2, -1]
arr_1_5 = []
ans_1_5 = []


tests_arrs = [arr_1_1, arr_1_2,arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2,ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_4(tests_arrs[i]) == answers[i], '\n')
    task_4(tests_arrs[i])
print('-'* 20)



# 5 Циклический сдвиг(1-й вариант)
def task_5_1(*args):
    arr = args[0]
    m = args[1]

    print(f'Исходный первый список: {" ".join(str(el) for el in arr)}')
    print(f'Количество позиций вправо: {m}')

    help_arr = arr[-m:]

    for i in range(len(arr) - 1, m - 1, -1):
        arr[i] = arr[i - m]

    for i in range(len(help_arr)):
        arr[i] = help_arr[i]

    print(f'Результат: {" ".join(str(el) for el in arr)}', '\n')
    return arr


arr_1_1 = [[1,2,3,4,5,6,7], 3]
ans_1_1 = [5,6,7,1,2,3,4]
arr_1_2 = [[1,2,3,4,5,6,7], 0]
ans_1_2 = [1,2,3,4,5,6,7]
arr_1_3 = [[1,2,3,4,5,6,7], 1]
ans_1_3 = [7,1,2,3,4,5,6]
arr_1_4 = [[0], 1]
ans_1_4 = [0]
arr_1_5 = [[], 0]
ans_1_5 = []


tests_arrs = [arr_1_1, arr_1_2,arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2,ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_4(*tests_arrs[i]) == answers[i], '\n')
    task_5_1(*tests_arrs[i])
print('-'* 20)


# 4 Циклический сдвиг(2-й вариант)
def task_5_2(*args):
    arr = args[0]
    m = args[1]

    print(f'Исходный первый список: {" ".join(str(el) for el in arr)}')
    print(f'Количество позиций вправо: {m}')

    help = arr[-m:]
    for j in range(m):
        help_var = arr[-1]

        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]

        arr[0] = help_var

    print(f'Результат: {" ".join(str(el) for el in arr)}', '\n')
    return arr


arr_1_1 = [[1,2,3,4,5,6,7], 3]
ans_1_1 = [5,6,7,1,2,3,4]
arr_1_2 = [[1,2,3,4,5,6,7], 0]
ans_1_2 = [1,2,3,4,5,6,7]
arr_1_3 = [[1,2,3,4,5,6,7], 1]
ans_1_3 = [7,1,2,3,4,5,6]
arr_1_4 = [[0], 1]
ans_1_4 = [0]
arr_1_5 = [[], 0]
ans_1_5 = []


tests_arrs = [arr_1_1, arr_1_2,arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2,ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_4(*tests_arrs[i]) == answers[i], '\n')
    task_5_2(*tests_arrs[i])
print('-'* 20)

# 6 Вариант 3
def task_6(arr):

    max_val = arr[0]
    pre_max_val = arr[1]

    print(f'Исходный список: {" ".join(str(el) for el in arr)}')

    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val, pre_max_val = arr[i], max_val
        elif arr[i] == max_val:
            continue
        elif arr[i] > pre_max_val:
            pre_max_val = arr[i]

    print(f'Результат: {pre_max_val}', '\n')
    return pre_max_val


arr_1_1 = [1, 8, 2,3,100, 4,5,6,7]
ans_1_1 = 8
arr_1_2 = [1, 2, 3, 4, 4]
ans_1_2 = 3
arr_1_3 = [0, 1]
ans_1_3 = 0
arr_1_4 = [-1, -20, -20, -1, -9]
ans_1_4 = -9
arr_1_5 = [8, 2, 3, 4, 10]
ans_1_5 = 8



tests_arrs = [arr_1_1, arr_1_2,arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2,ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_4(tests_arrs[i]) == answers[i], '\n')
    task_6(tests_arrs[i])
print('-'* 20)