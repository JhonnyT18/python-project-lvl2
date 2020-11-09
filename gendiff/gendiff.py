# -*- coding: utf-8 -*-


import json


def get_data(path_to_file1, path_to_file2):
    first_file = json.load(open(path_to_file1))
    second_file = json.load(open(path_to_file2))
    return first_file, second_file


deleted, added, no_changed = ('- ', '+ ', '  ')


def make_diff(first_file, second_file):
    keys_from_first = first_file.keys()
    keys_from_second = second_file.keys()
    diff = []
    for key in keys_from_first & keys_from_second:
        if first_file[key] == second_file[key]:
            diff.append((no_changed + key, str(first_file[key])))
        else:
            diff.append((deleted + key, str(first_file[key])))
            diff.append((added + key, str(second_file[key])))

    for key in keys_from_first ^ keys_from_second:
        if key in keys_from_first:
            diff.append((deleted + key, str(first_file[key])))
        else:
            diff.append((added + key, str(second_file[key])))
    sorted_diff = sorted(diff, key=lambda i: i[0][2])
    return sorted_diff


def generate_diff(path_to_file1, path_to_file2):
    first_file, second_file = get_data(path_to_file1, path_to_file2)
    sorted_diff = make_diff(first_file, second_file)
    str_dif = ''
    for i in sorted_diff:
        str_dif += ('   ' + i[0] + ': ' + i[1] + '\n')
    result = '{}\n{}{}'.format('{', str_dif, '}')
    return result
