
#
def simple_insert_sort(arr, step):
    for i in range(step, len(arr)):
        c = arr[i]
        j = i - step
        while j >= 0 and arr[j] >= c:
            arr[j + step] = arr[j]
            j -= step
        arr[j + step] = c
    return arr


def shell_sort(arr):
    step = int(len(arr) / 2)

    while step >= 1:
        simple_insert_sort(arr, step)
        step = int(step / 2)

    return arr



def quick_sort(arr):
    if len(arr) < 2:
        return arr

    supporter = int(len(arr) / 2)
    less = []
    greater = []
    equal = []
    for i in range(len(arr)):
        if arr[i] < arr[supporter]:
            less += [arr[i]]
        elif arr[i] == arr[supporter]:
            equal += [arr[i]]
        else:
            greater += [arr[i]]


    return quick_sort(less) + equal + quick_sort(greater)



def tournament_sort(arr):
    m = 0
    print(arr)

    while m < len(arr):
        stage = 1
        while stage < (len(arr) - m):
            stage = stage * 2
            distance = int(stage / 2)
            for i in range(m + distance, len(arr), stage):
                if arr[i] < arr[i - distance]:
                    arr[i], arr[i - distance] = arr[i - distance], arr[i]
        m += 1

    return arr



def check_branch(i, arr):
    index_child_l = 2 * i + 1
    index_child_r = 2 * i + 2
    the_biggest_element_index = index_child_l
    if index_child_l >= len(arr): # существует ли левый дочерний элемент
        return arr
    elif index_child_r < len(arr) and arr[index_child_r] > arr[index_child_l]:
        the_biggest_element_index = index_child_r
    if arr[i] < arr[the_biggest_element_index]:
        arr[i], arr[the_biggest_element_index] = arr[the_biggest_element_index], arr[i]
        return check_branch(the_biggest_element_index, arr)
    return arr


def pyramid_sort(arr):
    start_element = int((len(arr) - 2) / 2)
    for i in range(start_element, -1, -1):
        arr = check_branch(i, arr)

    for i in range(len(arr)):
        arr[0], arr[-i - 1] = arr[-i - 1], arr[0]
        sorted_list = arr[-i - 1:]
        arr = check_branch(0, arr[:-i - 1]) + sorted_list

    return arr


arr_1_1 = [-333, 12, 24124, -1, -12, 1, 2, -232323]
ans_1_1 = [-232323, -333, -12, -1, 1, 2, 12, 24124]
arr_1_2 = [3, -4, 1, -13, 11, -10]
ans_1_2 = [-13, -10, -4, 1, 3, 11]
arr_1_3 = [1, -2, -1, -2, 1]
ans_1_3 = [-2, -2, -1, 1, 1]
arr_1_4 = [-1000, -100000, -10, -13, 0]
ans_1_4 = [-100000, -1000, -13, -10, 0]
arr_1_5 = [9, 10, 11, 12 ,13, 14, 15, 16, 1 ,2 ,3 ,4 ,5 ,6 ,7 , 8]
ans_1_5 = [1 ,2 ,3 ,4 ,5 ,6 ,7 , 8, 9, 10, 11, 12 ,13, 14, 15, 16]


tests_arrs = [arr_1_1, arr_1_2, arr_1_3, arr_1_4, arr_1_5]
answers = [ans_1_1, ans_1_2, ans_1_3, ans_1_4, ans_1_5]

for i in range(len(tests_arrs)):
    print(f'Тест {i + 1}')
    print(pyramid_sort(tests_arrs[i]) == answers[i], '\n')

    # task_1(tests_arrs[i])/
print('-' * 20)
