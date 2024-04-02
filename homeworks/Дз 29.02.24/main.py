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
    have_mistakes = True
    while have_mistakes:
        have_mistakes = False
        i = 0
        j = 1
        while i + j < len(arr):
            if arr[i] <= 0 or arr[i] <= arr[i + j]:
                i += 1
                j = 1
                continue
            if arr[i + j] <= 0:
                j += 1
                continue

            if arr[i] > arr[i+j]:
                have_mistakes = True
                arr[i], arr[i+j] = arr[i+j], arr[i]
                j = 1
                i += 1
    print(f'Результат:       {" ".join(str(el) for el in arr)}', '\n')
    return arr



arr_1_1 = [0, 4, -1, 2, -1, 3]
ans_1_1 = [0, 2, -1, 3, -1, 4]
arr_1_2 = [3, -1, 1, 0, 2, -3, 1]
ans_1_2 = [1, -1, 1, 0, 2, -3, 3]
arr_1_3 = [0, 5, 3, 4, 2, 1, 0]
ans_1_3 = [0, 1, 2, 3, 4, 5, 0]
arr_1_4 = [5, 4, -1, 3]
ans_1_4 = [3, 4, -1, 5]
arr_1_5 = [4, 4, 3, -1, 1, -1]
ans_1_5 = [1, 3, 4, -1, 4, -1]


tests_arrs = [arr_1_1, arr_1_2,arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2,ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_1_1(tests_arrs[i]) == answers[i], '\n')
    # task_1_1(tests_arrs[i])
print('-'* 20)



def task_1_2(arr):
    # 5 4 -1 3
    print(f'Исходный список: {" ".join(str(el) for el in arr)}')
    i, j = 1, 1
    while i < len(arr):

        if arr[i] < 1:
            i += 1
            j = 1
            continue

        if i - j < 0:
            i += 1
            j = 1
            continue

        if arr[i - j] < 1:
            j += 1
            continue

        if arr[i - j] <= arr[i]:
            i += 1
            j = 1
            continue

        arr[i - j], arr[i] = arr[i], arr[i - j]
        i, j = (i - j), 1

    print(f'Результат:       {" ".join(str(el) for el in arr)}', '\n')
    return arr



arr_1_1 = [0, 4, -1, 2, -1, 3]
ans_1_1 = [0, 2, -1, 3, -1, 4]
arr_1_2 = [3, -1, 1, 0, 2, -3, 1]
ans_1_2 = [1, -1, 1, 0, 2, -3, 3]
arr_1_3 = [0, 5, 3, 4, 2, 1, 0]
ans_1_3 = [0, 1, 2, 3, 4, 5, 0]
arr_1_4 = [5, 4, -1, 3]
ans_1_4 = [3, 4, -1, 5]
arr_1_5 = [4, 4, 3, -1, 1, -1]
ans_1_5 = [1, 3, 4, -1, 4, -1]


tests_arrs = [arr_1_1, arr_1_2,arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2,ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_1_2(tests_arrs[i]) == answers[i], '\n')
    # task_1_1(tests_arrs[i])
print('-'* 20)



def task_1_3(arr):
    print(f'Исходный список: {" ".join(str(el) for el in arr)}')

    for i in range(1, len(arr)):
        if arr[i] < 1:
            continue

        c = arr[i]
        j = i - 1
        k = 1

        while j >= 0:
            if arr[j] < 1:
                j -= 1
                k += 1
                continue

            if arr[j] <= c:
                break

            arr[j + k] = arr[j]
            j -= 1
            k = 1

        arr[j + k] = c

    print(f'Результат:       {" ".join(str(el) for el in arr)}', '\n')
    return arr

arr_1_1 = [0, 4, -1, 2, -1, 3]
ans_1_1 = [0, 2, -1, 3, -1, 4]
arr_1_2 = [3, -1, 1, 0, 2, -3, 1]
ans_1_2 = [1, -1, 1, 0, 2, -3, 3]
arr_1_3 = [0, 5, 3, 4, 2, 1, 0]
ans_1_3 = [0, 1, 2, 3, 4, 5, 0]
arr_1_4 = [5, 4, -1, 3]
ans_1_4 = [3, 4, -1, 5]
arr_1_5 = [4, 4, 3, -1, 1, -1]
ans_1_5 = [1, 3, 4, -1, 4, -1]


tests_arrs = [arr_1_1, arr_1_2,arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2,ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_1_3(tests_arrs[i]) == answers[i], '\n')
    # task_1_3(tests_arrs[i])
print('-'* 20)

"""
Включить в упорядоченный по возрастанию массив заданное значение q в качестве элемента так,\
чтобы полученный массив остался упорядоченным.
"""

def task_2(q):
    arr = [-4, -2, -1, 1, 2, 4, 6, 7, 8, 9, 10]
    print(f'Исходный значение: {q}')
    print(f'Исходный список: {" ".join(str(el) for el in arr)}')
    arr += [q]
    for i in range(1, len(arr)):

        number = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > number:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = number

    print(f'Результат:       {" ".join(str(el) for el in arr)}', '\n')
    return arr

arr_1_1 = -3
ans_1_1 = [-4, -3, -2, -1, 1, 2, 4, 6, 7, 8, 9, 10]
arr_1_2 = -1
ans_1_2 = [-4, -2, -1, -1, 1, 2, 4, 6, 7, 8, 9, 10]
arr_1_3 = 3
ans_1_3 = [-4, -2, -1, 1, 2, 3, 4, 6, 7, 8, 9, 10]
arr_1_4 = -8
ans_1_4 = [-4, -2, -1, 1, 2, 4, 6, 7, 8, 8, 9, 10]
arr_1_5 = 100
ans_1_5 = [-4, -2, -1, 1, 2, 4, 6, 7, 8, 9, 10, 100]


tests_arrs = [arr_1_1, arr_1_2,arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2,ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_2(tests_arrs[i]) == answers[i], '\n')
    # task_2(tests_arrs[i])
print('-'* 20)



"""
Включить в упорядоченный по возрастанию массив заданное значение q в качестве элемента так,\
чтобы полученный массив остался упорядоченным.
"""

def task_3(p, q):
    arr = [-4, -2, -1, 1, 2, 4, 6, 7, 8, 9, 10]
    print(f'Исходный значение: {p, q}')
    print(f'Исходный список: {" ".join(str(el) for el in arr)}')
    arr += [q, p]
    for i in range(1, len(arr)):
        number = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < number:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = number

    print(f'Результат:       {" ".join(str(el) for el in arr)}', '\n')
    return arr

arr_1_1 = [-3, 100]
ans_1_1 = [-4, -3, -2, -1, 1, 2, 4, 6, 7, 8, 9, 10, 100]
arr_1_2 = [-1, -100]
ans_1_2 = [-100, -4, -2, -1, -1, 1, 2, 4, 6, 7, 8, 9, 10]
arr_1_3 = [3, 1]
ans_1_3 = [-4, -2, -1, 1, 2, 3, 4, 6, 7, 8, 9, 10]
arr_1_4 = [8, 3]
ans_1_4 = [-4, -2, -1, 1, 2, 4, 6, 7, 8, 8, 9, 10]
arr_1_5 = [100, 120]
ans_1_5 = [-4, -2, -1, 1, 2, 4, 6, 7, 8, 9, 10, 100]


tests_arrs = [arr_1_1, arr_1_2,arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2,ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_3(*tests_arrs[i]) == answers[i], '\n')
    task_3(*tests_arrs[i])
print('-'* 20)

'''
Заданы упорядоченный по возрастанию массив а из n элементов и упорядоченный по убыванию массив b из m элементов.
 Сформировать новый упорядоченный по убыванию массив с, включив в него все элементы из a и b,  
 не используя алгоритмы сортировки и инвертирования.
'''

# ф-ция вставки значения в список
def insert_value_in_arr(arr, index, value):
    arr = arr + [None]
    for i in range(len(arr) - 1, index - 1, -1):
        arr[i] = arr[i - 1]
    arr[index] = value
    return arr

def task_4(arr_asc, arr_desc):
    n = len(arr_asc)
    print(f'Исходный список: {" ".join(str(el) for el in arr_asc)}')
    print(f'Исходный список: {" ".join(str(el) for el in arr_desc)}')

    for i in range(len(arr_asc)):
        if arr_asc[i] >= arr_desc[0]:
            arr_desc = insert_value_in_arr(arr_desc, 0, arr_asc[i])
            continue

        if arr_asc[i] <= arr_desc[-1]:
            continue

        mid = (len(arr_desc) + i) // 2
        start = 0
        end = (len(arr_desc) + i) - 1

        while arr_desc[mid] != arr_asc[i] and start <= end:

            if arr_asc[i] > arr_desc[mid]:
                end = mid - 1
            else:
                start = mid + 1

            mid = (start + end) // 2

        if start > end:
            arr_desc = insert_value_in_arr(arr_desc, start, arr_asc[i])
        else:
            arr_desc = insert_value_in_arr(arr_desc, mid, arr_asc[i])

    print(f'Результат:       {" ".join(str(el) for el in arr_desc)}', '\n')
    return arr_desc

arr_1_1 = [[-10, 2, 3, 11110], [10,3, 2, 1, 0, -1, -2, -3, -4]]
ans_1_1 = [3, 3, 2, 2, 1, 1]
arr_1_2 = [[ 2, 3], [6, 5, 3, 2]]
ans_1_2 = [6, 5, 3, 3, 2, 2, 1, 0, -1]
arr_1_3 = [[0, 2, 4], [5, 3, 1, -1]]
ans_1_3 = [5, 4, 3, 2, 1, 0, -1]
arr_1_4 = [[-10, -9, 8], [9, -3, -11]]
ans_1_4 = [-11, -10, -9, -3, 8, 9]
arr_1_5 = [[3, 6, 9], [10, 4, 1]]
ans_1_5 = [1, 3, 4, 6, 9, 10]


tests_arrs = [arr_1_1, arr_1_2,arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2,ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    # print(task_4(*tests_arrs[i]) == answers[i], '\n')
    task_4(*tests_arrs[i])
print('-'* 20)

