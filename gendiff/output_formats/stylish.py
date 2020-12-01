# -*- coding: utf-8 -*-
indent_start = 2
indent_step = 4
conditions = {
    'added': '+ ',
    'deleted': '- ',
    'changeless': '  ',
    'changed': '- ',
    'children': '  '
}


def to_transform_value(value, indent):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        keys = list(value.keys())
        result = '{'
        for key in keys:
            result += '\n' + indent * ' ' + '  ' + str(key) + ': ' + to_transform_value(value[key], indent + indent_step)  # noqa: E501
        return result + '\n' + (indent - indent_start) * ' ' + '}'
    else:
        return str(value)


def make_first_part_stylish(built_diff, key, indent):
    condition, value = built_diff[key]
    if condition == 'changed':
        value, new_value = value
    result = indent * ' ' + conditions[condition] + str(key) + ': '
    if condition == 'children':
        return result
    result += to_transform_value(value, indent + indent_step) + '\n'
    if condition != 'changed':
        return result
    result += indent * ' ' + '+ ' + str(key) + ': ' + to_transform_value(new_value, indent + indent_step) + '\n'  # noqa: E501
    return result


def get_stylish(built_diff, indent):
    keys_from_diff = list(built_diff.keys())
    keys_from_diff.sort()
    result = ''
    for key in keys_from_diff:
        condition, value = built_diff[key]
        if condition == 'children':
            result += make_first_part_stylish(built_diff, key, indent) + '{\n'
            result += get_stylish(value, indent + indent_step)
            result += indent * ' ' + '  }\n'
        else:
            result += make_first_part_stylish(built_diff, key, indent)
    return result


def render(input_data):
    return '{\n' + get_stylish(input_data, indent_start) + '}\n'
