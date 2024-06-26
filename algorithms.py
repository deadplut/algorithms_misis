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

class LSDSort(Generator):
    def sort_method(self, array):
        return self.lsd_sort(array)


    def lsd_sort(self, arr):
        if not arr:
            return []
        m = []

        max_length = len(str(abs(max(arr, key=abs))))
        arr_s = self.fill_array_with_zeros(arr, max_length)

        for r in range(1, max_length + 1):
            for i in range(-9, 10):
                d = self.spread_numbers_into_bins(arr_s, i, r)
                m += d
                d.clear()

            arr_s = m.copy()
            m.clear()

        return [int(x) for x in arr_s]

    @staticmethod
    def fill_array_with_zeros(arr, max_length):
        result_arr = []
        for num in arr:
            if num >= 0:
                processed_num = str(num).zfill(max_length)
            else:
                processed_num = '-' + str(abs(num)).zfill(max_length)
            result_arr.append(processed_num)
        return result_arr

    @staticmethod
    def spread_numbers_into_bins(arr, bin, rank):
        result_arr = []
        for x in arr:
            coef = '-'
            if int(x) >= 0 or bin == 0:
                coef = ''
            if (coef + x[-rank]) == str(bin):
                result_arr.append(x)
        return result_arr


class MSDSort(Generator):
    def sort_method(self, array):
        return self.radix(array)

    def radix(self, array, size=None, index=None):
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
            bins[9 + coef * dest_i] += [e]

        result = []
        for b in bins:
            if b:
                result.append(self.radix(b, size, index - 1))

        flattened_result = self.flatten(result)
        return flattened_result

    @staticmethod
    def flatten(array):
        new_array = []
        for sub_array in array:
            new_array += sub_array
        return new_array

