# -*- coding: utf-8 -*-
ADDED = "Property '{}' was added with value: {}"
REMOVED = "Property '{}' was removed"
UPDATE = "Property '{}' was updated. From {} to {}"


def get_plain(diff, before_keys=''):
    result = ''
    for key in sorted(list(diff.keys())):
        condition, value = diff[key]
        if condition == 'added':
            result += ADDED.format(str(before_keys) + str(key), to_transform_value(value)) + '\n'  # noqa: E501
        elif condition == 'deleted':
            result += (REMOVED.format(str(before_keys) + key)) + '\n'
        elif condition == 'changed':
            value, new_value = value
            result += UPDATE.format(str(before_keys) + str(key), to_transform_value(value), to_transform_value(new_value)) + '\n'  # noqa: E501
        elif condition == 'children':
            result += get_plain(value, before_keys + key + '.')
    return result


def to_transform_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return "'" + str(value) + "'"


def render(diff):
    return get_plain(diff)
