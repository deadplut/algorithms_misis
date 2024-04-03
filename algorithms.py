from generator import Generator


class MergeSort(Generator):
    """
    Сортировка слиянием
    """
    def sort_method(self, array):
        return self.merge_sort(array)

    def merge_sort(self, array):
        """
        Сортировка слиянием
        """

        if len(array) < 2:
            return array
        middle = int(len(array) / 2)
        left_array = self.merge_sort(array[:middle])
        right_array = self.merge_sort(array[middle:])
        return self.merge_arrays(left_array, right_array)


    @staticmethod
    def merge_arrays(*args):
        """
        Вспомогательный метод для сортировки слиянием
        """
        result = [None] * (len(args[0]) + len(args[1]))
        arr1, arr2 = args[0], args[1]

        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):

            if arr1[i] <= arr2[j]:
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
        return result



class ShellSort(Generator):
    """
    Сортировка слиянием
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

