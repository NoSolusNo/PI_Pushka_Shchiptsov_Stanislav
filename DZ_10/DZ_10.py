import json
import re


def read_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data


def sort_dict_by_key_name(value_dict):
    name_key = "name"
    name_dict = value_dict[name_key]
    my_dict_list = name_dict.split()
    name_for_sotr = my_dict_list[-1]
    return name_for_sotr


def sort_dict_by_die_date_in_key_years(value_dict):
    name_key = "years"
    name_dict = value_dict[name_key]
    find_BC = re.findall(r'[0-9]{1,4} BC', name_dict)
    if len(find_BC):
        find_DY = int(re.findall(r'[0-9]{1,4}', find_BC[-1])[0]) * -1
    else:
        find_DY = int(re.findall(r'[0-9]{1,4}', name_dict)[-1])
    return find_DY


def sort_dict_by_count_word_in_key_text(value_dict):
    name_key = "text"
    name_dict = value_dict[name_key]
    format_str = re.sub("[^A-Za-z0-9 ]+", '', name_dict).split()
    return len(format_str)


sort_name_dict = sorted(read_json("data.json"), key=sort_dict_by_key_name)
# print(json.dumps(sort_name_dict, indent=2))
#######################
sort_die_date_dict = sorted(read_json("data.json"), key=sort_dict_by_die_date_in_key_years)
# print(json.dumps(sort_die_date_dict, indent=2))
#######################
sort_len_word_dict = sorted(read_json("data.json"), key=sort_dict_by_count_word_in_key_text)
# print(json.dumps(sort_len_word_dict, indent=2))
