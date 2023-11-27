# Таблица умноженеия от 1 до числа n
# Применен процедурный подход, поскольку удобно использовать процедуру multiplication_table
# для мнократного вызова с разными числами n.

n = int(input("Введите число: "))

def multiplication_table(number):
    for i in range(1, number+1):
        for j in range(1, number+1):
            # print(str(i) + '*' + str(j) + '=' + str(i*j))
            print(f"{i} * {j} = {i*j}")

multiplication_table(n)