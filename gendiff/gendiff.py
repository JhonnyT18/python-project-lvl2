# -*- coding: utf-8 -*-
from gendiff.files_loader import get_data


added = 'added'
deleted = 'deleted'
changed = 'changed'
changeless = 'changeless'


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
    diff = make_diff(get_data(path_to_first), get_data(path_to_second))
    indent = '   '
    keys = list(diff.keys())
    keys.sort()
    result = ''
    for key in keys:
        condition, value = diff[key]
        if condition == 'changeless':
            result += indent + '  ' + key + ': ' + str(value) + '\n'
        elif condition == 'changed':
            result += indent + '- ' + key + ': ' + str(value[0]) + '\n'
            result += indent + '+ ' + key + ': ' + str(value[1]) + '\n'
        elif condition == 'added':
            result += indent + '+ ' + key + ': ' + str(value) + '\n'
        elif condition == 'deleted':
            result += indent + '- ' + key + ': ' + str(value) + '\n'
    return '{}\n{}{}'.format('{', result, '}')
