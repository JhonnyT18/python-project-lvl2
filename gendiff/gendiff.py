# -*- coding: utf-8 -*-


import json


def generate_diff(path_to_file1, path_to_file2):
    first_file = json.load(open(path_to_file1))
    second_file = json.load(open(path_to_file2))
    keys_from_first = first_file.keys()
    keys_from_second = second_file.keys()
    common_keys = keys_from_first & keys_from_second
    common_keys_list = []
    deleted = '- '
    added = '+ '
    no_changed = '  '
    for i in common_keys:
        if first_file[i] == second_file[i]:
            common_keys_list.append((no_changed + i, str(first_file[i])))
        else:
            common_keys_list.append((deleted + i, str(first_file[i])))
            common_keys_list.append((added + i, str(second_file[i])))
    only_first_keys = keys_from_first - keys_from_second
    first_keys_list = [(deleted + i, str(first_file[i])) for i in only_first_keys]  # noqa: E501
    only_second_keys = keys_from_second - keys_from_first
    second_keys_list = [(added + i, str(second_file[i])) for i in only_second_keys]  # noqa: E501
    tuples_with_diff = common_keys_list + first_keys_list + second_keys_list
    sorted_diff = sorted(tuples_with_diff, key=lambda i: i[0][2])
    str_dif = ''
    for i in sorted_diff:
        str_dif += ('   ' + i[0] + ': ' + i[1] + '\n')
    diff = '{}\n{}{}'.format('{', str_dif, '}')
    return diff
