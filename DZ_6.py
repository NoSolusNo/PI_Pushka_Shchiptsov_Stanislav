############################# 1
my_list = ["qwe", "asd", "zxc", "fgh", "rty"]
my_new_list = []
for index, value in enumerate(my_list):
    if index % 2:
        my_new_list.append(value[::-1])
    else:
        my_new_list.append(value)
print(my_new_list)
############################# 2
my_list = ["qwe", "asd", "zxc", "fgh", "aty"]
my_new_list = []
for value in my_list:
    if value.startswith("a"):
        my_new_list.append(value)
print(my_new_list)
############################# 3
my_list = ["qwe", "asd", "zxc", "fagh", "aty"]
my_new_list = []
for value in my_list:
    if "a" in value:
        my_new_list.append(value)
print(my_new_list)
############################# 4
my_list = ["qwe", 11, "zxc", "fagh", 23]
my_new_list = []
for value in my_list:
    if type(value) == str:
        my_new_list.append(value)
print(my_new_list)
############################# 5
my_str = "qweqweqweqweqwer"
my_new_str = ""
my_set = set(my_str)
for value in my_set:
    if my_str.count(value) == 1:
        my_new_str += value
print(my_new_str)
############################# 6
my_str_1 = "qweqweqweqjweqwer"
my_str_2 = "qwejhgftyujknhgf"
my_set = set.intersection(set(my_str_1), set(my_str_2))
print(my_set)
############################# 7
my_str_1 = "qweqweqweqjweqwer"
my_str_2 = "qwejhgftyuknhgfr"
my_uni_str = ""
my_set = set.intersection(set(my_str_1), set(my_str_2))
for value in my_set:
    if my_str_1.count(value) == 1 and my_str_2.count(value) == 1:
        my_uni_str += value
print(my_uni_str)
############################# 8
my_dict = {
    "Фамилия": "Бубновый",
    "Имя": "Валет",
    "Возраст": 43,
    "Проживание": {
        "Страна": "Украина",
        "Город": "Днепр",
        "Улица": "Баумана"
    },
    "Работа": {
        "Наличие": 1,
        "Должность": "Козырь"
    }
}
############################# 9
my_dict = {
    "Составляющие": {
        "Коржи": {
            "Мука": 400,
            "Молоко": 150,
            "Масло": 200,
            "Яйцо": 3
        },
        "Крем": {
            "Сахар": 200,
            "Масло": 0,
            "Ваниль": 2,
            "Сметана": 250
        },
        "Глазурь": {
            "Какао": 250,
            "Сахар": 500,
            "Масло": 150
        }
    }
}