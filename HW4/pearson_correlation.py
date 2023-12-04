from math import sqrt
def pearson_correlation(array1, array2):
    avg_array1 = sum(array1) / len(array1)
    avg_array2 = sum(array2) / len(array2)

    res1 = sum((x - avg_array1) * (y - avg_array2) for x, y in zip(array1, array2))

    res2 = sqrt(sum(pow((x - avg_array1), 2) * pow((y - avg_array2), 2) for x, y in zip(array1, array2)))

    return res1/res2


if __name__ == "__main__":
    arr1 = [2, 1, 3]
    arr2 = [12, 4, 5]
    print(pearson_correlation(arr1, arr2))



