def binary_seash(list, num):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((high + low)/ 2)
        res = list[mid]
        if res == num:
            return mid
        if res > num:
            high = mid - 1
        else:
            low = mid + 1
    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_seash(my_list, 1))
