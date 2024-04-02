import datetime


def decorator(func):
    def wrapper(*args, **kvargs):
        startTime = datetime.datetime.now()
        result = func(*args, **kvargs)
        print("Время исполнения:", datetime.datetime.now() - startTime)
        return result

    return wrapper


"""1. Определить значение и номер последнего отрицательного элемента массива"""


@decorator
def task_1(array):
    print(f'Исходный список: {" ".join(str(el) for el in array)}')
    for i in range(len(array) - 1, -1, -1):
        if array[i] < 0:
            print(f'Результат: "{array[i]}" - значение, "{i}" - номер(индекс)')
            break


task_1_array_1 = [1, -1, -3, -4, 5, 6, -6]
task_1_array_2 = [-1, 5, 6, 5]
task_1_array_3 = [-100, 0, 0, 5, 6, 5]
task_1_array_4 = [-1]
task_1_array_5 = [1]
task_1_array_6 = [-1, -1, -1, -2, -3, -4, -5]

task_1(task_1_array_1)
task_1(task_1_array_2)
task_1(task_1_array_3)
task_1(task_1_array_4)
task_1(task_1_array_5)
task_1(task_1_array_6)

"""2. Из элементов заданного массива сформировать два новых массива, включая в первый массив
элементы исходного массива с четными индексами, во второй - с нечетными."""


@decorator
def task_2(array):
    print(f'Исходный список: {" ".join(str(el) for el in array)}')
    length = len(array)
    if length % 2 == 0:
        first_array = [None] * (length // 2)
    else:
        first_array = [None] * (length // 2 + 1)
    sec_array = [None] * (length // 2)

    for i in range(len(array)):
        index = i // 2
        if i % 2 == 0:
            first_array[index] = array[i]
        else:
            sec_array[index] = array[i]

    print(f'Результат: \n{first_array} - массив со значениями четных индексов')
    print(f'{sec_array} - массив со значениями нечетными индексов')


task_2_array_1 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
task_2_array_2 = [1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20]
task_2_array_3 = [-1, -20, -1, -20, -1, -20, -1, -20, -1, -20]
task_2_array_4 = [-1]

task_2(task_2_array_1)
task_2(task_2_array_2)
task_2(task_2_array_3)
task_2(task_2_array_4)

"""3. Найти сумму квадратов элементов, расположенных до первого отрицательного элемента
массива."""


@decorator
def task_3(array):
    print(f'Исходный список: {" ".join(str(el) for el in array)}')
    i = 0
    sum_array = 0
    while array[i] >= 0:
        sum_array += array[i] ** 2
        i += 1
    print(f'Результат: {sum_array}')


task_3_array_1 = [1, 1, 3, 4, 5, 6, -6]
task_3_array_2 = [1, 3, -3, -4, 5, 6, 5]
task_3_array_3 = [-100, 0, 0, 5, 6, 5]

task_3(task_3_array_1)
task_3(task_3_array_2)
task_3(task_3_array_3)

"""4. Определить индексы элементов массива, меньших среднего. Результат получить в виде
массива."""


@decorator
def task_4(array):
    print(f'Исходный список: {" ".join(str(el) for el in array)}')

    avg = sum(array) / len(array)
    result = [i for i in range(len(array)) if array[i] < avg]
    print(f'Результат: {result}')


task_4_array_1 = [1, 1, 3, 4, 5, 6, -6]
task_4_array_2 = [1, 3, -3, -4, 5, 6, 5]
task_4_array_3 = [-100, 0, 0, 5, 6, 5]
task_4_array_4 = [-1, -1, -2, -2, -1]

task_4(task_4_array_1)
task_4(task_4_array_2)
task_4(task_4_array_3)
task_4(task_4_array_4)

"""5. В одномерном массиве поменять местами соседние элементы (1-й со 2-м, 3-й с 4-м и т.д.),
распложенные в первой половине массива.."""


@decorator
def task_5(array):
    print(f'Исходный список: {" ".join(str(el) for el in array)}')
    mid = len(array) / 2 - 2
    i = 0
    while i <= mid:
        if i % 2 == 0:
            array[i], array[i + 1] = array[i + 1], array[i]
        i += 1
    print(f'Результат: {array}')


task_5_array_1 = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 8]
task_5_array_2 = [-100, 0, 1, 5, 6]
task_5_array_3 = [-100, 0, 1, 5, 6, 5, 7, 8]
task_5_array_4 = [1]
task_5_array_5 = []

task_5(task_5_array_1)
task_5(task_5_array_2)
task_5(task_5_array_3)
task_5(task_5_array_4)
task_5(task_5_array_5)

"""6. В массиве А найти максимальное количество следующих подряд упорядоченных по убыванию
элементов."""


@decorator
def task_6(array):
    print(f'Исходный список: {" ".join(str(el) for el in array)}')
    count = 1
    if len(array) == 0:
        count = 0
    a = 0
    b = 0
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            count += 1
            b = i
        else:
            if count < b - a:
                count = b - a
            a = i
            b = i

    print(f'Результат: {count}')


task_6_array_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
task_6_array_2 = [-100, 1, 1, 5, 6]
task_6_array_3 = [-100, 0, 1, 5, 6, 5, 7, 8]
task_6_array_4 = [-100, -101, -103, -104]
task_6_array_5 = [1]
task_6_array_6 = []

task_6(task_6_array_1)
task_6(task_6_array_2)
task_6(task_6_array_3)
task_6(task_6_array_4)
task_6(task_6_array_5)
task_6(task_6_array_6)

"""1.*В массиве находятся целые числа от (в произвольном порядке), одно – один раз, остальные -  по 2 раза. 
Найти число, встречающееся 1 раз.
"""


@decorator
def task_1_star(array):
    print(f'Исходный список: {" ".join(str(el) for el in array)}')
    length = len(array)
    sum = 0
    sub_array = [None] * length
    for i in range(len(array)):
        if array[i] in sub_array:
            sum -= array[i]
        else:
            sub_array[i] = array[i]
            sum += array[i]
    print(f'Результат: {sum}')


task_1_star_array_1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
task_1_star_array_2 = [2, 2, 4, 3, 3, 4, 6, 5, 6, 5, 1, 7, 7]
task_1_star_array_3 = [1, 1, 2, 2, 3, 7, 3, 4, 4, 5, 5]
task_1_star_array_4 = [10, 2, 2]
task_1_star_array_5 = [21, 21, 10]



task_1_star(task_1_star_array_1)
task_1_star(task_1_star_array_2)
task_1_star(task_1_star_array_3)
task_1_star(task_1_star_array_4)
task_1_star(task_1_star_array_5)


"""2.**В массиве находятся целые числа, больше половины из которых равны Х. Найти Х."""

@decorator
def task_2_star(array):
    print(f'Исходный список: {" ".join(str(el) for el in array)}')
    answer = array[0]
    max_count = 1
    count_in_row = 1
    for i in range(len(array)):
        if array[i] == array[i - 1]:
            count_in_row += 1
            if count_in_row > max_count:
                max_count = count_in_row
                answer = array[i]
        else:
            count_in_row = 1

    print(f'Результат: {answer}')
    return answer


print('Тест 1')
print(task_2_star([3, 3, 1, 3, 1, 3, 1]) == 3)
print('Тест 2')
print(task_2_star([0, 0, 0, 0, 0, 0, 0]) == 0)
print('Тест 3')
print(task_2_star([1, 3, 1, 3, 3, 2, 3]) == 3)
print('Тест 4')
print(task_2_star([1]) == 1)
print('Тест 5')
print(task_2_star([-3, -1, -1, -1, -2, -1]) == -1)
print('Тест 6')
print(task_2_star([3, 1, 1, 3, 3, 1, 3]) == 3)
print(task_2_star([3, 3, 1, 1, 3, 1, 3]) == 3)

"""3.** В массиве находятся целые числа, одно – один или 2 раза, остальные -  по 3 раза. 
Найти это число и сколько раз оно встречается."""

@decorator
def task_3_star(arr):
    print(f'Исходный список: {" ".join(str(el) for el in arr)}')
    anwer_count = len(arr) % 3
    first_array = [None] * len(arr)
    first_sum = 0
    sec_array = [None] * len(arr)
    sec_sum = 0
    for i in range(len(arr)):
        if arr[i] not in first_array:
            first_array[i] = arr[i]
            first_sum += arr[i]
        elif arr[i] not in sec_array:
            sec_array[i] = arr[i]
        else:
            sec_sum += arr[i]
    print(f'Результат: "{first_sum - sec_sum}" - число встречается {anwer_count} раз(а)')
    return [first_sum - sec_sum, anwer_count]


print('Тест 1')
print(task_3_star([3, 3, 2, 2, 2, 1, 1, 1]) == [3, 2]),
print('Тест 2')
print(task_3_star([1, 2, 1, 2, 1, 2, 0, 0]) == [0, 2])
print('Тест 2.1')
print(task_3_star([1, 2, 1, 2, 1, 2, 0]) == [0, 1])

print('Тест 3')
print(task_3_star([1, 0, 0, 2, 3, 3, 1, 2, 1, 2, 0]) == [3, 2])
print('Тест 4')
print(task_3_star([-2, -3, -1, -1, -1, -2, -2, -3]) == [-3, 2])
print('Тест 4')
print(task_3_star([-2, 3, -1, -1, -1, -2, -2, 3]) == [3, 2])
