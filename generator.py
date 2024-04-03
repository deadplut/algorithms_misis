import random
import time

class Generator:

    def __init__(self, output_file):
        self.output_file = output_file

    def write_to_file(self, text):
        with open(self.output_file, 'a') as file:
            file.write(text + '\n')


    def run_tests(self):

        #########################
        # ТЕСТЫ СЛУЧАЙНЫХ МАССИВОВ (Первая группа)
        ##########################
        sample_size = 0

        print(1)
        self.write_to_file('Тест 1.1: Массивы случайных чисел 10')
        array = self.generate_random_array(10, sample_size,)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 1.2: Массивы случайных чисел 1000')
        array = self.generate_random_array(1000, sample_size)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 1.3: Массивы случайных чисел 100000')
        array = self.generate_random_array(100000, sample_size)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 1.4: Массивы случайных чисел 1000000')
        array = self.generate_random_array(1000000, sample_size)
        self.sort_test(array, 20, sample_size)
        self.write_to_file('~' * 100)

        #########################
        # ТЕСТЫ массивы, включающие несколько отсортированных последовательностей (вторая группа
        ##########################
        print(2)

        sample_size = 10
        self.write_to_file('Тест 2.1: Массивы случайных чисел 10')
        array = self.generate_random_array(10, sample_size,)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 2.2: Массивы случайных чисел 1000')
        array = self.generate_random_array(1000, sample_size)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 2.3: Массивы случайных чисел 100000')
        array = self.generate_random_array(100000, sample_size)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 2.4: Массивы случайных чисел 1000000')
        array = self.generate_random_array(1000000, sample_size)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('~' * 100)

        #########################
        # ТЕСТЫ массивы, включающие несколько отсортированных последовательностей (третья группа)
        ##########################
        print(3)

        sample_size = 10
        self.write_to_file('Тест 3.1: Массивы случайных чисел 10')
        array = self.generate_array_3_group(10)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 3.2: Массивы случайных чисел 1000')
        array = self.generate_array_3_group(1000)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 3.3: Массивы случайных чисел 100000')
        array = self.generate_array_3_group(100000)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 3.4: Массивы случайных чисел 1000000')
        array = self.generate_array_3_group(1000000)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('~' * 100)
        #########################
        # ТЕСТЫ 4 отсортированные в прямом и обратном порядке
        ##########################
        print(4)

        sample_size = 10
        self.write_to_file('Тест 4.1: Массивы случайных чисел 10')
        self.write_to_file('ASC')
        array = self.generate_random_array(10, 100)
        self.sort_test(array, 20, sample_size)
        self.write_to_file('Desc')
        array = sorted(array, reverse=True)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 4.1: Массивы случайных чисел 10')
        self.write_to_file('ASC')
        array = self.generate_random_array(10, 100)
        self.sort_test(array, 20, sample_size)
        self.write_to_file('Desc')
        array = sorted(array, reverse=True)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 4.2: Массивы случайных чисел 1000')
        self.write_to_file('ASC')
        array = self.generate_random_array(1000, 100)
        self.sort_test(array, 20, sample_size)
        self.write_to_file('Desc')
        array = sorted(array, reverse=True)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 4.3: Массивы случайных чисел 100000')
        self.write_to_file('ASC')
        array = self.generate_random_array(100000, 100)
        self.sort_test(array, 20, sample_size)
        self.write_to_file('Desc')
        array = sorted(array, reverse=True)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 4.4: Массивы случайных чисел 1000000')
        self.write_to_file('ASC')
        array = self.generate_random_array(1000000, 100)
        self.sort_test(array, 20, sample_size)
        self.write_to_file('Desc')
        array = sorted(array, reverse=True)
        self.sort_test(array, 20, sample_size)

        #########################
        # ТЕСТЫ массивы и тесты с большим количеством повторений одного элемента (10%, 25%, 50%, 75% и 90%).
        ##########################
        print(5)
        sample_size = 10
        percent_of_repeated_numbers = 10

        self.write_to_file(f'Тест 5.1.1: Массивы случайных чисел 10, процент повторения одного элемента {percent_of_repeated_numbers}')
        array = self.generate_array_repeated_numbers(10, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 5.2.1: Массивы случайных чисел 1000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(1000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 5.3.1: Массивы случайных чисел 100000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(100000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 5.4.1: Массивы случайных чисел 1000000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(1000000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('~' * 100)


        percent_of_repeated_numbers = 25

        self.write_to_file(f'Тест 5.1.2: Массивы случайных чисел 10, процент повторения одного элемента {percent_of_repeated_numbers}')
        array = self.generate_array_repeated_numbers(10, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 5.2.2: Массивы случайных чисел 1000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(1000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 5.3.2: Массивы случайных чисел 100000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(100000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 5.4.2: Массивы случайных чисел 1000000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(1000000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('~' * 100)
        percent_of_repeated_numbers = 50

        self.write_to_file(f'Тест 5.1.3: Массивы случайных чисел 10, процент повторения одного элемента {percent_of_repeated_numbers}')
        array = self.generate_array_repeated_numbers(10, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 5.2.3: Массивы случайных чисел 1000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(1000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 5.3.3: Массивы случайных чисел 100000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(100000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('Тест 5.4.3: Массивы случайных чисел 1000000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(1000000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('~' * 100)

        percent_of_repeated_numbers = 75

        self.write_to_file(
            f'Тест 5.1.4: Массивы случайных чисел 10, процент повторения одного элемента {percent_of_repeated_numbers}')
        array = self.generate_array_repeated_numbers(10, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file(
            'Тест 5.2.4: Массивы случайных чисел 1000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(1000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file(
            'Тест 5.3.4: Массивы случайных чисел 100000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(100000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file(
            'Тест 5.4.4: Массивы случайных чисел 1000000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(1000000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('~' * 100)

        percent_of_repeated_numbers = 90

        self.write_to_file(
            f'Тест 5.1.5: Массивы случайных чисел 10, процент повторения одного элемента {percent_of_repeated_numbers}')
        array = self.generate_array_repeated_numbers(10, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file(
            'Тест 5.2.5: Массивы случайных чисел 1000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(1000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file(
            'Тест 5.3.5: Массивы случайных чисел 100000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(100000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file(
            'Тест 5.4.5: Массивы случайных чисел 1000000, процент повторения одного элемента {percent_of_repeated_numbers')
        array = self.generate_array_repeated_numbers(1000000, percent_of_repeated_numbers)
        self.sort_test(array, 20, sample_size)

        self.write_to_file('~' * 100)




    def sort_method(self, array):
        return []


    def sort_test(self, array, times, sample_size):
        total_time = 0
        for i in range(times):
            start_time = time.time()
            result = self.sort_method(array)
            end_time = time.time()
            loop_time = end_time - start_time
            total_time += loop_time


        avg_time = total_time / times
        self.write_to_file(f"Average time per loop: {avg_time} seconds")
        # return result


    @staticmethod
    def generate_random_array(length, size_of_sorted_sample:int=0):
        """
        Метод для генерации массива заданной длины и размером сортированных сэмплов
        """

        random_array = [random.randint(-100, 1000) for _ in range(length)]
        if size_of_sorted_sample==0:
            return random_array

        sorted_array = sorted(random_array)
        if size_of_sorted_sample==100:
            return sorted_array

        sample_length = int(size_of_sorted_sample * length / 100)


        array = [sorted_array[i * sample_length : (i + 1) * sample_length] for i in range(int(100/size_of_sorted_sample) + 1)]
        random.shuffle(array)
        result = []
        for i in array:
            result += i

        return result

    @staticmethod
    def generate_array_3_group(length, size_of_sorted_sample: int = 10, number_of_diff_repeated_numbers=2):
        """
        Метод для генерации массива для третьей группы:
        третья группа – изначально почти отсортированные массивы случайных чисел с
        некоторым числом перестановок двух случайных элементов;
        """
        count_of_random_numbers = int(length / 5)
        random_array = [random.randint(-100, 1000) for _ in range(length - count_of_random_numbers)]
        repeated_numbers = [[random.randint(100, 100 + number_of_diff_repeated_numbers)] for _ in range(count_of_random_numbers)]
        sorted_array = sorted(random_array)



        sample_length = int(size_of_sorted_sample * length / 100)

        array = [sorted_array[i * sample_length: (i + 1) * sample_length] for i in
                 range(int(100 / size_of_sorted_sample) + 1)] + repeated_numbers
        random.shuffle(array)
        result = []

        for i in array:
            result += i

        return result


    @staticmethod
    def generate_array_repeated_numbers(length, percent_of_repeated_numbers=50):
        """
        Метод для генерации массива для третьей группы:
        третья группа – изначально почти отсортированные массивы случайных чисел с
        некоторым числом перестановок двух случайных элементов;
        """
        repeated_numbers = int(length * percent_of_repeated_numbers / 100)
        random_array = [random.randint(-100, 1000) for _ in range(length - repeated_numbers)]

        repeated_arr = [100 for _ in range(repeated_numbers)]
        random_array = random_array + repeated_arr
        random.shuffle(random_array)
        return random_array


#
# a = Generator()
# print(a.generate_array_repeated_numbers(200))
