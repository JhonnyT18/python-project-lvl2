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


def to_str(value, indent):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        keys = list(value.keys())
        result = '{'
        for key in keys:
            result += '\n' + (indent+indent_step) * ' ' + '  ' + str(key) + ': ' + to_str(value[key], indent + indent_step)  # noqa: E501
        return result + '\n' + (indent + indent_start) * ' ' + '}'
    else:
        return str(value)


def get_stylish(built_diff, indent):
    keys_from_diff = sorted(list(built_diff.keys()))
    print(keys_from_diff)
    result = ''
    for key in keys_from_diff:
        condition, value = built_diff[key]
        result += indent * ' ' + conditions[condition] + str(key) + ': '
        if condition == 'changed':
            value, new_value = value
            result += to_str(value, indent) + '\n'
            result += indent * ' ' + '+ ' + str(key) + ': ' + to_str(new_value, indent + indent_step) + '\n'  # noqa: E501
        elif condition == 'changeless' or condition == 'added' or condition == 'deleted':  # noqa: E501
            result += to_str(value, indent) + '\n'
        else:
            result += '{\n' + get_stylish(value, indent + indent_step) + (indent + indent_start) * ' ' + '}\n'  # noqa: E501
    return result


def render(input_data):
    return '{\n' + get_stylish(input_data, indent_start) + '}\n'
