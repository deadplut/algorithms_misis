def some_func(x, max_length):
    print(max_length)
    return x **2

max_length = 123
arr = [1, 2, 3]
arr_s = list(map(lambda x, max_length=max_length: some_func(x, max_length), arr))

print(
    arr_s
)
