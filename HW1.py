# Сортировка списка выбором по убыванию

num = [1, 10, 3, 5, -1]

# Императивный способ
def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        maximum = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[maximum]:
                maximum = j
        numbers[maximum], numbers[i] = numbers[i], numbers[maximum]
    return numbers


print(sort_list_imperative(num))


# Декларативный способ
def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers


print(sort_list_declarative(num))
