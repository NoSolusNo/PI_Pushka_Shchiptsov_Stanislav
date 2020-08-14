from random import randint
import string

######################## 1.1
my_list = []
my_i = 0
while my_i < 20:
    my_rand = randint(1, 100)
    my_list.append(my_rand)
    my_i += 1
print(my_list)
######################## 1.2
my_list = []
for i in range(0, 20):
    my_rand = randint(1, 100)
    my_list.append(my_rand)
print(my_list)
######################## 2
my_dict = {}
my_points = list(string.ascii_uppercase[0:3])
for value in my_points:
    my_dict[value] = (randint(1, 100), randint(1, 100))
print(my_dict)
######################## 3
my_str = "I'm the string"


def side_stars(text_need):
    print(f"***{text_need}***")


side_stars(my_str)


######################## 4
def up_under_stars(text_need):
    len_stars = str("*" * len(text_need))
    print(f"{len_stars}\n{text_need}\n{len_stars}")


up_under_stars(my_str)


######################## 5
def multi_stars(text_need):
    md_text = f"***{text_need}***"
    len_stars = str("*" * len(md_text))
    print(f"{len_stars}\n{md_text}\n{len_stars}")


multi_stars(my_str)
