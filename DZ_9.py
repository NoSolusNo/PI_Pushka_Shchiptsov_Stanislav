import string
import random
import csv
import json
import re


def rand_flags():
    flags = ["integer_flag", "float_flag", "bool_flag"]
    rand_flag = random.choice(flags)
    return rand_flag


def txt_generator():
    size = random.choice(range(100, 1000))
    # chars = string.printable.replace("\n", "")
    # chars = chars.replace("\r", "")
    chars = re.sub("^\s+|\n|\r|\s$", '', string.printable)
    rand_str = ''
    rand_str = rand_str.join(random.choice(chars) for i in range(size))
    for unit in range(0, 9):
        switch = random.choice(range(1, size - 1))
        rand_str = f"{rand_str[0:switch]}\n{rand_str[switch + 1:size]}"
    return rand_str


def json_generator():
    rand_dict = {}
    chars = string.ascii_lowercase
    key_size = random.choice(range(5, 21))
    rand_flag = rand_flags()
    for unit in range(key_size):
        rand_key = "".join(random.choice(chars) for i in range(5))
        if rand_flag == "integer_flag":
            rand_value = random.choice(range(-100, 101))
        elif rand_flag == "float_flag":
            rand_value = random.random()
        elif rand_flag == "bool_flag":
            rand_value = bool(random.choice(range(0, 2)))
        else:
            rand_value = random.choice(range(-100, 101))
        rand_dict.update({f"{rand_key}": rand_value})
    return rand_dict


def csv_generator():
    rand_n = random.choice(range(1, 11))  # строк
    rand_m = random.choice(range(1, 11))  # столбц
    rows_for_csv = []
    for n in range(rand_n):
        rand_list = []
        for m in range(rand_m):
            rand_value = random.choice(range(0, 2))
            rand_list.append(rand_value)
        rows_for_csv.append(rand_list)
    return rows_for_csv


def write_txt(filename_with_path):
    with open(filename_with_path, 'w') as txt_file:
        data = txt_file.write(txt_generator())
    return "Ok"


def write_json(filename_with_path):
    with open(filename_with_path, 'w') as json_file:
        data = json_file.write(json.dumps(json_generator(), indent=4))
    return "Ok"


def write_csv(filename_with_path):
    with open(filename_with_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(csv_generator())
    return "Ok"


def file_writer(filename_with_path):
    ext = filename_with_path.rsplit(".", 1)[-1]
    if ext == "txt":
        write_txt(filename_with_path)
    elif ext == "json":
        write_json(filename_with_path)
    elif ext == "csv":
        write_csv(filename_with_path)
    else:
        raise Exception("Unsupported file format!")
    return "Ok"


file_writer("test_DZ_9.txt")
file_writer("test_DZ_9.json")
file_writer("test_DZ_9.csv")
