my_list = [9, 7, 5, 3, 3, 1]
n = int(input('Введите количество: '))
for it in range(n):
    number = int(input('Введите число: '))
    i = 0
    for val in my_list:
        if number > val:
            break
        i += 1
    my_list.insert(i, (number))
    print(my_list)