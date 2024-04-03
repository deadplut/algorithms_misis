from generator import Generator


class ShellSort(Generator):
    """
    Сортировка Шелла
    """
    def sort_method(self, array):
        return self.shell_sort(array)


    @staticmethod
    def simple_insert_sort(arr, step):
        for i in range(step, len(arr)):
            c = arr[i]
            j = i - step
            while j >= 0 and arr[j] >= c:
                arr[j + step] = arr[j]
                j -= step
            arr[j + step] = c

    def shell_sort(self, arr):
        step = int(len(arr) / 2)

        while step >= 1:
            self.simple_insert_sort(arr, step)
            step = int(step / 2)

        return arr

class PyramidSort(Generator):
    def sort_method(self, array):
        return self.pyramid_sort(array)
    def check_branch(self, i, arr):
        index_child_l = 2 * i + 1
        index_child_r = 2 * i + 2
        the_biggest_element_index = index_child_l
        if index_child_l >= len(arr):  # существует ли левый дочерний элемент
            return arr
        elif index_child_r < len(arr) and arr[index_child_r] > arr[index_child_l]:
            the_biggest_element_index = index_child_r
        if arr[i] < arr[the_biggest_element_index]:
            arr[i], arr[the_biggest_element_index] = arr[the_biggest_element_index], arr[i]
            return self.check_branch(the_biggest_element_index, arr)
        return arr

    def pyramid_sort(self, arr):
        start_element = int((len(arr) - 2) / 2)
        for i in range(start_element, -1, -1):
            arr = self.check_branch(i, arr)

        for i in range(len(arr)):
            arr[0], arr[-i - 1] = arr[-i - 1], arr[0]
            sorted_list = arr[-i - 1:]
            arr = self.check_branch(0, arr[:-i - 1]) + sorted_list

        return arr


class TournamentSort(Generator):
    def sort_method(self, array):
        return self.tournament_sort(array)

    @staticmethod
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

