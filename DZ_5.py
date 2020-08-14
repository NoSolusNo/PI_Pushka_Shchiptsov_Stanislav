import string

################## 1. Дано целое число (int). Определить сколько нулей в этом числе.
my_int = 102030405060700000000000000000000
count_zero = str(my_int).count("0")
print(count_zero)

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
my_result = []
for value in my_list_1:
    if not value % 2:
        my_result.append(value)
for value in my_list_2:
    if value % 2:
        my_result.append(value)
print(my_result)

################## 4. Дан список my_list. Создать список new_list у которого первый элемент
# из my_list стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
my_list = [1, 2, 3, 4]
new_list = my_list.copy()
need = new_list.append(new_list.pop(0))
print(my_list, new_list)

################## 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя!
my_list = [1, 2, 3, 4]
my_list.append(my_list.pop(0))
print(my_list)

################## 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34, но меньше чем 56". Найти сумму ВСЕХ чисел в этой строке.
# Для данного примера 133.
my_str = "43 больше чем 34, но меньше чем 56."
my_sum = 0
dots = string.punctuation
for symbol in my_str:
    if symbol in dots:
        my_str = my_str.replace(symbol, "")
my_str_list = my_str.split()
for value in my_str_list:
    if value.isdigit():
        my_sum += int(value)
print(my_sum)

################## 7. Дана строка my_str. Разделите эту строку на
# пары из двух символов и поместите эти пары в список. Если строка
# содержит нечетное количество символов, пропущенный второй символ последней
# пары должен быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abc' -> ['ab', 'c_']
my_str = "qwer  tyu"
my_list = []
n = 2
for index in range(0, len(my_str), n):
    my_list.append(my_str[index:index + n])
if len(my_list[-1]) < n:
    last_elem = my_list.pop(-1)
    my_list.append(last_elem + "_" * (n - len(last_elem)))
print(my_list)

################## 8. Дана строка my_str в которой символы не повторяются и два символа
# l_limit, r_limit, которые точно находятся в этой строке.
# Причем l_limit левее чем r_limit. В переменную sub_str поместить часть
# строки между этими символами. my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"
my_str = "My_long st"
l_limit = "o"
r_limit = "t"
# sub_str = my_str[my_str.find(l_limit)+1: my_str.find(r_limit)] это я просто проверил =)
# но мне показалось так неудобно, по этому:
pos_l = my_str.find(l_limit)
pos_r = my_str.find(r_limit)
sub_str = my_str[pos_l + 1: pos_r]
print(sub_str)

################## 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа
# l_limit, r_limit, которые точно находятся в этой строке.
# Причем l_limit левее чем r_limit. В переменную sub_str поместить
# НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
my_str = "My long string"
l_limit = "o"
r_limit = "g"
pos_l = my_str.find(l_limit)
pos_r = my_str.rfind(r_limit)
sub_str = my_str[pos_l + 1: pos_r]
print(sub_str)

################## 10. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше двух своих соседей (слева и справа), и выведите количество
# таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них
# недостаточно соседей. Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
count = 0
for index in range(1, len(my_list) - 1):
    if my_list[index] > my_list[index - 1] + my_list[index + 1]:
        count += 1
print(count)