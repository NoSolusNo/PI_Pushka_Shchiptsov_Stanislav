my_list = [101, 209, 3, 7, 4000]
###################################### 1
for index in my_list:
    if index > 100:
        print(index)
    else:
        pass
###################################### 2
my_result = []
for index in my_list:
    if index > 100:
        my_result.append(index)
    else:
        pass
print(my_result)
###################################### 3
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[len(my_list) - 1] + my_list[len(my_list) - 2])
print(my_list)
###################################### 4
val_ch = True
while val_ch:
    try:
        value = input("Введите число: ")
        value = value.replace(",", ".")
        value = float(value)
        print(value ** -1)
        break
    except (ValueError):
        print(f"Введите целое число или число с \".\" или с \",\"")

