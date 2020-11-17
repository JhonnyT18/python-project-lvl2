# -*- coding: utf-8 -*-
from gendiff.files_loader import get_data


added, deleted, changed, changeless = ('added', 'deleted', 'changed', 'changeless')  # noqa: E501


def make_diff(first_file, second_file):
    keys_from_first = first_file.keys()
    keys_from_second = second_file.keys()
    diff = {}
    for key in keys_from_first & keys_from_second:
        if first_file[key] == second_file[key]:
            diff[key] = (changeless, first_file[key])
        else:
            diff[key] = (changed, (first_file[key], second_file[key]))
    for key in keys_from_first ^ keys_from_second:
        if key in keys_from_first:
            diff[key] = (deleted, first_file[key])
        else:
            diff[key] = (added, second_file[key])
    return diff


def generate_diff(path_to_first, path_to_second):
    first_file, second_file = (get_data(path_to_first), get_data(path_to_second))  # noqa: E501
    diff = make_diff(first_file, second_file)
    keys = list(diff.keys())
    keys.sort()
    result = ''
    for i in keys:
        indent = '    '
        condition, value = diff[i]
        if condition == 'changeless':
            result += indent + '  ' + i + ': ' + str(value) + '\n'
        elif condition == 'changed':
            result += indent + '- ' + i + ': ' + str(value[0]) + '\n'
            result += indent + '+ ' + i + ': ' + str(value[1]) + '\n'
        elif condition == 'add':
            result += indent + '+ ' + i + ': ' + str(value) + '\n'
        elif condition == 'deleted':
            result += indent + '- ' + i + ': ' + str(value) + '\n'
    return '{}\n{}{}'.format('{', result, '}')
