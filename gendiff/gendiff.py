#!usr/bin/env python3

import json


def generate_diff(file_path1, file_path2):

    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    dict1 = {y: x for x, y in file1.items()}
    dict2 = {y: x for x, y in file2.items()}

    dict_temp = dict()
    dict_temp.update(dict1)
    dict_temp.update(dict2)

    dict_temp_sorted = sorted(dict_temp, key=dict_temp.get)

    dict_result = {}

    for w in dict_temp_sorted:
        dict_result[w] = dict_temp[w]

    result_str = '{\n'
    for k, v in dict_result.items():
        result_str += '  '

        if dict1.get(k) and not dict2.get(k):
            result_str += '- '
        if dict1.get(k) and dict2.get(k):
            result_str += '  '
        if dict2.get(k) and not dict1.get(k):
            result_str += '+ '
        result_str += f'{v}: {k}\n'
    result_str += '}'
    print(result_str.lower())
    return result_str.lower()
