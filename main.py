def merge_sort(array):
    if len(array) < 2:
        return array
    middle = int(len(array) / 2)
    left_array = merge_sort(array[:middle])
    right_array = merge_sort(array[middle:])
    return merge_arrays(left_array, right_array)


def merge_arrays(*args):
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


# task_3([1, 2, 3, 4, 5, 6,], [3, 3, 3, 4,4 ,5])
print(merge_sort([3, 2, 1,5, 5, 50, -1, -2, -1]))