from generator import Generator


class BubleSort(Generator):
    """
    Сортировка Шелла
    """
    def sort_method(self, array):
        return self.bubble_sort(array)

    @staticmethod
    def bubble_sort(arr):
        have_mistakes = True
        while have_mistakes:
            have_mistakes = False
            i = 0

            while i < len(arr) - 1:
                if arr[i] <= arr[i + 1]:
                    i += 1
                    continue

                if arr[i] > arr[i + 1]:
                    have_mistakes = True
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]

                    i += 1
        return arr


class SimpleInsertsSort(Generator):
    def sort_method(self, array):
        return self.simple_insert_sort(array)

    @staticmethod
    def simple_insert_sort(arr, step=1):
        for i in range(step, len(arr)):
            c = arr[i]
            j = i - step
            while j >= 0 and arr[j] >= c:
                arr[j + step] = arr[j]
                j -= step
            arr[j + step] = c
        return arr

class SimpleSelectSort(Generator):
    def sort_method(self, array):
        return self.selection_sort(array)

    @staticmethod
    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            index = i
            for j in range(i + 1, n):
                if arr[j] < arr[index]:
                    index = j
            arr[i], arr[index] = arr[index], arr[i]
        return arr

class DwarfSort(Generator):

    def sort_method(self, array):
        return self.dwarf_sort(array)


    @staticmethod
    def dwarf_sort(arr):
        i, j = 1, 1
        while i < len(arr):

            if i - j < 0:
                i += 1
                j = 1
                continue

            if arr[i - j] <= arr[i]:
                i += 1
                j = 1
                continue

            arr[i - j], arr[i] = arr[i], arr[i - j]
            i, j = (i - j), 1

        return arr






