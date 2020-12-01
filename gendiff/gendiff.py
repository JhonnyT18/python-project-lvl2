# -*- coding: utf-8 -*-
from gendiff.files_loader import get_data
from gendiff.output_formats import stylish, plain, json


ADDED = 'added'
DELETED = 'deleted'
CHANGED = 'changed'
CHANGELESS = 'changeless'
CHILDREN = 'children'


def make_diff(first_file, second_file):
    keys_from_first = first_file.keys()
    keys_from_second = second_file.keys()
    diff = {}
    common_keys = keys_from_first & keys_from_second
    keys_from_only_one = keys_from_first ^ keys_from_second
    for key in common_keys:
        if first_file[key] == second_file[key]:
            diff[key] = (CHANGELESS, first_file[key])
        elif isinstance(first_file[key], dict) and isinstance(second_file[key], dict):  # noqa: E501
            diff[key] = (CHILDREN, make_diff(first_file[key], second_file[key]))  # noqa: E501
        else:
            diff[key] = (CHANGED, (first_file[key], second_file[key]))
    for key in keys_from_only_one:
        if key in keys_from_first:
            diff[key] = (DELETED, first_file[key])
        else:
            diff[key] = (ADDED, second_file[key])
    return diff


def generate_diff(path_to_first, path_to_second, output_format='stylish'):
    first_file = get_data(path_to_first)
    second_file = get_data(path_to_second)
    if output_format == 'plain':
        return plain.render(make_diff(first_file, second_file))
    elif output_format == 'json':
        return json.render(make_diff(first_file, second_file))
    else:
        return stylish.render(make_diff(first_file, second_file))
