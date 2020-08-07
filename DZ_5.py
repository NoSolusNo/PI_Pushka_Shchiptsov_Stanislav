################## 1. Дано целое число (int). Определить сколько нулей в этом числе.
my_int = 102030405060700000000000000000000
count = 0
for symbol in str(my_int):
    if int(symbol) == 0:
        count += 1
    else:
        pass
print(count)
################## 2. Дано целое число (int). Определить сколько нулей в конце этого числа.
count = 0
for symbol in str(my_int)[::-1]:
    if int(symbol) == 0:
        count += 1
    else:
        break
print(count)
################## 3. Даны списки my_list_1 и my_list_2. Создать список my_result в который вначале
# поместить четные элементы из my_list_1 и потом нечетные элементы из my_list_2.
my_list_1 = [1, 2, 3, 4, 5, 6]
my_list_2 = [1, 2, 3, 4, 5, 6]
my_result =[]
for index in my_list_1:
    if index % 2:
        my_result.append(my_list_1[index])
for index in my_list_2:
   if index % 2:
        my_result.append(my_list_2[index-1])
print(my_result)
################## 4. Дан список my_list. Создать список new_list у которого первый элемент
# из my_list стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
my_list = [1, 2, 3, 4]
new_list = my_list.copy()
new_list.append(my_list[0])
del new_list[0]
print(my_list, new_list)
################## 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя!
my_list = [1, 2, 3, 4]
my_list.append(my_list[0])
del my_list[0]
print(my_list)
################## 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34, но меньше чем 56". Найти сумму ВСЕХ чисел в этой строке.
# Для данного примера 133.
my_str = "43 больше чем 34 но меньше чем 56"
my_sum = 0
my_str_sp = my_str.split()
for value in my_str_sp:
    if value.isalnum():
        pass
    else:
        print(value.isalnum())
    try:
        if int(value):
            my_sum += int(value)
    except (ValueError):
        continue

print(my_str_sp)
print(my_sum)