############################################ пример 1
my_indexes = [0, 1, 2, 3, 4]
my_string = "abcde"
for index in my_indexes:
    print(my_string[index])

############################################ 1
my_list = [1, 3, 6, 3, 4, 7, 8, 4]
my_indexes = [0, 1, 2, 3, 4, 5, 6, 7]
for index in my_indexes:
    print(my_list[index])

############################################ 2
my_list_1 = [1, 3, 6, 3, 4, 7, 8, 4]
my_list_2 = [4, 8, 7, 4, 3, 6, 3, 1]
my_indexes = [0, 1, 2, 3, 4, 5, 6, 7]
for index in my_indexes:
    print(f"({my_list_1[index]}, {my_list_2[index]})")

############################################ пример 2
my_string_1 = "12"
my_string_2 = "34"

for symb_1 in my_string_1:
	for symb_2 in my_string_2:
		print(symb_1 + symb_2)

############################################ 3
my_string = "0123456789"
for symb_1 in my_string:
    for symb_2 in my_string:
        print(int(symb_1 + symb_2))