import datetime


def decorator(func):
    def wrapper(*args, **kvargs):
        startTime = datetime.datetime.now()
        result = func(*args, **kvargs)
        print("Время исполнения:", datetime.datetime.now() - startTime)
        return result

    return wrapper


"""1. Задан одномерный массив. Сформировать другой одномерный массив из отрицательных элементов, 
      расположенных между максимальным и минимальным элементами исходного массива"""

def task_1(arr):

    index_min = 0
    index_max = 0

    for i in range(len(arr)):
        if arr[i] < arr[index_min]:
            index_min = i
        if arr[i] > arr[index_max]:
            index_max = i

    if index_min > index_max:

        first, last = index_max, index_min
    elif index_min < index_max:

        first, last = index_min, index_max
    else:
        len_new_arr = 0
        first, last = 0, 0

    answer = [None] * len(arr)
    count = 0
    for i in range(index_min+1, index_max ):
        if arr[i] < 0:
            answer[count] = arr[i]
            count += 1
    print(answer)
    return answer


arr_1_1 = [-10, -2, -3, 4]
ans_1_1 = [-2, -3]
arr_1_2 = [1, -3, -2, 4]
ans_1_2 = [-2]
arr_1_3 = [-1, -3, -2, -40, -12]
ans_1_3 = [-3, -2]
arr_1_4 = []
ans_1_4 = []
arr_1_5 = [0]
ans_1_5 = []


tests_arrs = [arr_1_1, arr_1_2,arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2,ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    print(task_1(tests_arrs[i]) == answers[i], '\n')
print('-'* 20)




def task_2(arr):
    if not arr:
        return arr
    answer = [None] * (len(arr) + 1)
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    avg = sum / len(arr)
    print(avg)

    indx_value = 0
    min_diff = avg - arr[indx_value] if avg > arr[indx_value] else arr[indx_value] - avg

    for i in range(len(arr)):
        diff = avg - arr[i] if avg > arr[i] else arr[i] - avg
        answer[i] = arr[i]
        if min_diff > diff:
            min_diff = diff
            indx_value = i
    print(min_diff)
    print(indx_value)
    for i in range(len(arr), indx_value+1, -1):
        answer[i] = answer[i - 1]

    answer[indx_value+1] = 1000
    print(answer)





arr_2_1 = [-10, -2, -3, 4]
ans_2_1 = [-2, -3]
arr_2_2 = [1, -3, -2, 4]
ans_2_2 = [-2]
arr_2_3 = [-1, -3, -2, -40, -12]
ans_2_3 = [-3, -2]
arr_2_4 = []
ans_2_4 = []
arr_2_5 = [0]
ans_2_5 = []


tests_arrs = [arr_2_1, arr_2_2,arr_2_3, arr_2_4, arr_2_5]
answers = [ans_2_1, ans_2_2,ans_2_3, ans_2_4, ans_2_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    print(task_2(tests_arrs[i]) == answers[i], '\n')
print('-'* 20)

def task_3(arr):
    if len(arr) < 2:
        return []
    index_max = None
    index_min = None
    for i in range(len(arr)):

        if index_max is None or arr[i] > arr[index_max]:
            index_max = i
            index_min = None
            if (i + 1) < len(arr):
                index_min = i + 1
                print(index_min)
        elif index_min and arr[i] < arr[index_min]:
            index_min = i

    anwer = arr
    if (index_min is not None) and (index_max is not None):
        anwer[index_min], anwer[index_max] =  anwer[index_max], anwer[index_min]
    print(anwer)
    # return


arr_3_1 = [10, -2, -3, 4]
ans_3_1 = [-2, -3]
arr_3_2 = [1, 30, -2, 4, -5]
ans_3_2 = [-2]
arr_3_3 = [-1000, 300, -2, -40, -122]
ans_3_3 = [-3, -2]
arr_3_4 = []
ans_3_4 = []
arr_3_5 = [0]
ans_3_5 = []


tests_arrs = [arr_3_1, arr_3_2,arr_3_3, arr_3_4, arr_3_5]
answers = [ans_3_1, ans_3_2,ans_3_3, ans_3_4, ans_3_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    print(task_3(tests_arrs[i]) == answers[i], '\n')
print('-'* 20)

def task_4(arr):
    i_min = None
    for i in range(len(arr)):
        if arr[i] <= 0:
            continue

        if i_min is None or arr[i_min] > arr[i]:
            i_min = i

    if i_min is None:
        return arr

    for i in range(i_min, len(arr) -1):
        print(i)
        arr[i] = arr[i + 1]

    del arr[-1]
    print(arr)
    return arr


arr_4_1 = [10, -2, -3, 4]
ans_4_1 = [10, -2, -3]
arr_4_2 = [1, 30, -2, 4, -5]
ans_4_2 = [30, -2, 4, -5]
arr_4_3 = [-1000, 300, -2, -40, -122]
ans_4_3 = [-1000, -2, -40, -122]
arr_4_4 = [-1]
ans_4_4 = [-1]
arr_4_5 = [0]
ans_4_5 = [0]


tests_arrs = [arr_4_1, arr_4_2,arr_4_3, arr_4_4, arr_4_5]
answers = [ans_4_1, ans_4_2,ans_4_3, ans_4_4, ans_4_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    print(task_4(tests_arrs[i]) == answers[i], '\n')
print('-'* 20)

def task_5(arr):
    if len(arr) < 1:
        return arr
    i_last = None
    for i in range(len(arr)):
        if arr[i] > 0:
           i_last = i

    if i_last is None:
        return arr

    arr.append(None)
    for i in range(len(arr) - 1, i_last+1, -1):
        arr[i] = arr[i -1]

    arr[i_last + 1] = 100

    print(arr)
    return arr


arr_5_1 = [10, -2, -3, 4]
ans_5_1 = [10, -2, -3, 4, 100]
arr_5_2 = [1, 30, -2, 4, -5]
ans_5_2 = [1, 30, -2, 4, 100, -5]
arr_5_3 = [1000, -300, -2, -40, -122]
ans_5_3 = [1000, 100, -300, -2, -40, -122]
arr_5_4 = []
ans_5_4 = []
arr_5_5 = [-1]
ans_5_5 = [-1]


tests_arrs = [arr_5_1, arr_5_2,arr_5_3, arr_5_4, arr_5_5]
answers = [ans_5_1, ans_5_2,ans_5_3, ans_5_4, ans_5_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    print(task_5(tests_arrs[i]) == answers[i], '\n')
print('-'* 20)



def task_6(arr):
    if len(arr) < 1:
        return arr
    i_max = 1
    for i in range(3, len(arr), 2):
        if arr[i] > arr[i_max]:
            i_max = i
    arr[i_max] = i_max

    print(arr)
    return arr


arr_6_1 = [10, -2, -3, 4]
ans_6_1 = [10, -2, -3, 3]
arr_6_2 = [1, 30, -2, 4, -5]
ans_6_2 = [1, 1, -2, 4, -5]
arr_6_3 = [1000, -300, -2, -40, -122]
ans_6_3 = [1000, -300, -2, 3, -122]
arr_6_4 = []
ans_6_4 = []
arr_6_5 = [-1]
ans_6_5 = [-1]


# tests_arrs = [arr_6_1, arr_6_2,arr_6_3, arr_6_4, arr_6_5]
# answers = [ans_6_1, ans_6_2,ans_6_3, ans_6_4, ans_6_5]
#
# for i in range(len(tests_arrs)):
#     print(f'Тест {i + 1}')
#     print(task_6(tests_arrs[i]) == answers[i], '\n')
# print('-'* 20)


def task_7(k):

    arr_1 = [1, 2, 3, 4, 5]
    arr_2 = [-1, -2, -3, -4, -5, -6]
    new_arr = [None] * (len(arr_1) + len(arr_2))

    for i in range(len(arr_1)):
        new_arr[i] = arr_1[i]

    index_first = k - len(arr_1) + 1
    if index_first > len(arr_1):
        index_first = len(arr_1)
    if index_first < 0:
        index_first = 0

    for i in range(len(new_arr), index_first, -1):
        print(i)
        new_arr[i - 1] = new_arr[i - len(arr_2) - 1]
        print(new_arr)


    for i in range(len(arr_2)):
        print(index_first)
        indexxx = index_first + i
        new_arr[indexxx] = arr_2[i]

    print(new_arr)
    return new_arr



arr_7_1 = 0
ans_7_1 = [-1, -2, -3, -4, -5, -6, 1, 2, 3, 4, 5]
arr_7_2 = 9
ans_7_2 = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6]
arr_7_3 = 7
ans_7_3 = [1, 2, 3, -1, -2, -3, -4, -5, -6, 4, 5]
arr_7_4 = 12
ans_7_4 = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6]
arr_7_5 = 3
ans_7_5 = [-1, -2, -3, -4, -5, -6, 1, 2, 3, 4, 5]


tests_arrs = [arr_7_1, arr_7_2,arr_7_3, arr_7_4, arr_7_5]
answers = [ans_7_1, ans_7_2,ans_7_3, ans_7_4, ans_7_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    print(task_7(tests_arrs[i]) == answers[i], '\n')
print('-'* 20)



def task_8(arr):
    for i in range(len(arr)):
        if arr[i] >= 0:
            continue

        index_max_value = i
        for j in range(i + 1, len(arr)):
            if arr[j] >= 0:
                continue
            if arr[j] > arr[index_max_value]:
                index_max_value = j

            # print(i, index_max_value)

        arr[i], arr[index_max_value] = arr[index_max_value], arr[i]
            # print(arr)
            # break



    print(arr)
    return arr


arr_8_1 = [10, -2, -3, -1, -10, 4]
ans_8_1 = [10, -1, -2, -3, -10, 4]
arr_8_2 = [-10, 30, -5, 4, -3]
ans_8_2 = [-3, 30, -5, 4, -10]
arr_8_3 = [1, 2, 3, 4]
ans_8_3 = [1, 2, 3, 4]
arr_8_4 = []
ans_8_4 = []
arr_8_5 = [0]
ans_8_5 = [0]


tests_arrs = [arr_8_1, arr_8_2,arr_8_3, arr_8_4, arr_8_5]
answers = [ans_8_1, ans_8_2,ans_8_3, ans_8_4, ans_8_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    print(task_8(tests_arrs[i]) == answers[i], '\n')
print('-'* 20)


def task_1_star(arr):
    print(f'Исходный список: {" ".join(str(el) for el in arr)}')

    answer = [None] * len(arr)
    count = 0
    answer[count] = 0
    for i in range(1, len(arr)):
        if arr[answer[0]] < arr[i]:
            count = 0
            answer[count] = i
        elif arr[answer[0]] == arr[i]:
            count += 1
            answer[count] = i

    print(f'Результат: {" ".join(str(el) for el in answer if el is not None)}')
    return answer


arr_1s_1 = [0, 0, 1, 1, 1, 2, 0, 2, -1, 2]
ans_1s_1 = [1, 3, 5]
arr_1s_2 = [2, 1, 2, 2, 1, 1]
ans_1s_2 = [0, 2, 3]
arr_1s_3 = [-1, -1, -3, -4, -1]
ans_1s_3 = [0, 1, 4]
arr_1s_4 = [1]
ans_1s_4 = [0]



tests_arrs = [arr_1s_1, arr_1s_2,arr_1s_3, arr_1s_4]
answers = [ans_1s_1, ans_1s_2,ans_1s_3, ans_1s_4]

for i in range(len(tests_arrs)):
    # print(f'Тест {i + 1}')
    task_1_star(tests_arrs[i])
    print('\n')
    # print(task_1_star(tests_arrs[i]) == answers[i], '\n')
print('-'* 20)


def task_2_star(arr):
    print(f'Исходный список: {" ".join(str(el) for el in arr)}')

    count = 0
    i = 0
    while (i + count) < len(arr):
        if arr[i + count] < 0:
            count += 1
            continue

        arr[i] = arr[i + count]
        i += 1

    print(f'Результат: {" ".join(str(el) for el in arr[:len(arr)-count])}')

    return arr[:len(arr)-count]


arr_2s_1 = [-1, 0, -1, -1, 10, -2, -3, 20, -3]
ans_2s_1 = [0, 10 , 20]
arr_2s_2 = [2, 1, 2, 2, 1, 1, -1, -2, -3, -4]
ans_2s_2 = [2, 1, 2, 2, 1, 1]
arr_2s_3 = [-1]
ans_2s_3 = []
arr_2s_4 = [1]
ans_2s_4 = [1]
arr_2s_5 = []
ans_2s_5 = []


tests_arrs = [arr_2s_1, arr_2s_2,arr_2s_3, arr_2s_4, arr_2s_5]
answers = [ans_2s_1, ans_2s_2,ans_2s_3, ans_2s_4, ans_2s_5]

for i in range(len(tests_arrs)):
    # print(f'Тест {i + 1}')
    # print(task_2_star(tests_arrs[i]) == answers[i], '\n')
    task_2_star(tests_arrs[i])
    print('\n')

print('-'* 20)


def task_3_star(arr):
    print(f'Исходный список: {" ".join(str(el) for el in arr)}')

    max_count = 0
    for i in range(len(arr)):
        count = 0
        for j in range(i + 1, (len(arr) - max_count)):
            if arr[j] == arr[i]:
                count += 1
            arr[j - count] = arr[j]
        max_count += count

    print(f'Результат: {" ".join(str(el) for el in arr[:len(arr)-max_count])}')

    return arr[:(len(arr)-max_count)]


arr_3s_1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
ans_3s_1 = [1, 2, 3, 4, 5]
arr_3s_2 = [1, 1, 1, 1, 1, 1, 1, 2 ]
ans_3s_2 = [1, 2]
arr_3s_3 = [1, 2]
ans_3s_3 = [1, 2]
arr_3s_4 = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]
ans_3s_4 = [3]
arr_3s_5 = [-1, -2, -3, -4, 0, 0, 0]
ans_3s_5 = [-1, -2, -3, -4, 0,]


tests_arrs = [arr_3s_1, arr_3s_2,arr_3s_3, arr_3s_4, arr_3s_5]
answers = [ans_3s_1, ans_3s_2,ans_3s_3, ans_3s_4, ans_3s_5]

for i in range(len(tests_arrs)):
    # print(f'Тест {i + 1}')
    # print(task_3_star(tests_arrs[i]) == answers[i], '\n')
    task_3_star(tests_arrs[i])
    print('\n')
print('-'* 20)