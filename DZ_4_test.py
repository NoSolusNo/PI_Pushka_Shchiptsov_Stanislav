################################################ 1
values = [1, 2, 3, 4, 5]
print(type(values))
################################################ 2
values = (1, 2, 3, 4, 5)
print(type(values))
################################################ 3
values = (1, 2, 3, 4, 5)
values = list(values)
print(type(values))
################################################ 4
values = [1, 2, 3, 4, 5]
values = tuple(values)
print(type(values))
################################################ 5
values = [1, 2, 3, 4, 5]
result = []
for value in values:
    result.append(value)
print(result)
################################################ 6
values = [1, 2, 3, 4, 5]
result = []
for value in values[::-1]:
    result.append(value)
print(result)
################################################ 7
values = [1, 2, 3, 4, 5]

print(len(values))
################################################ 8
values = [1, 2, 3, 4, 5]
new_value = values + values[::-1]
print(new_value)
################################################ 9
values = [1, 2, 3, 4, 5]
new_value = values
new_value.append(6)
print(values)
################################################ 10
values = [1, 2, 3, 4, 5]
new_value = values.copy()
new_value.append(6)
print(values)
################################################ 11
values = [0] * 6
values[0] = 1
print(values)
################################################ 12
value = 0
values = [value] * 6
value = 1
print(values)
################################################ 13
my_list = [0]
values = [my_list] * 3
print(values)
################################################ 14
my_list = [0]
values = [my_list] * 3
my_list.append(1)
print(values)
################################################ 15
my_list = [0]
values = [my_list.copy()] * 3
my_list.append(1)
print(values)
################################################ 16
count = 10
while count > 0:
    print("Test")
################################################ 17
count = 10
while count > 0:
    print("Test")
    count -= 1
################################################ 18
count = 10
exit_flag = True
while exit_flag:
    count -= 1
    if count > 0:
        exit_flag = False
    print("Test")