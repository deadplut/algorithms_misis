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




class QuickSort(Generator):
    def sort_method(self, array):
        return self.quick_sort(array)
    def quick_sort(self, arr):
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

        return self.quick_sort(less) + equal + self.quick_sort(greater)

