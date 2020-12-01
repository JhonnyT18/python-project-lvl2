# -*- coding: utf-8 -*-
import os
import json
import yaml


def get_type(path_to_file):
    return os.path.splitext(path_to_file)[1]


def get_data(path_to_file):
    with open(path_to_file) as file:
        return to_load(file, get_type(path_to_file))


def to_load(opened_file, files_type):
    if files_type == '.json':
        return json.load(opened_file)
    else:
        return yaml.safe_load(opened_file)
