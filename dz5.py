# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

user_number = int(input("Укажите число: "))
my_list = [7, 5, 3, 3, 2]
a = my_list.count(user_number)
for element in my_list:
    if a > 0:
        b = my_list.index(user_number)
        my_list.insert(b+a, user_number)
        break
    else:
        if user_number > element:
            c = my_list.index(element)
            my_list.insert(c, user_number)
            break
        elif user_number < my_list[len(my_list) - 1]:
            my_list.append(user_number)
print(my_list)

