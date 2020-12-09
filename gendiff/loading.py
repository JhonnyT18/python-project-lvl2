# -*- coding: utf-8 -*-
import os
import json
import yaml


def get_extant(path_to_file):
    return os.path.splitext(path_to_file)[1]


def get_data(path_to_file):
    with open(path_to_file) as file:
        return load(file, get_extant(path_to_file))


def load(opened_file, files_extent):
    if files_extent == '.json':
        return json.load(opened_file)
    else:
        return yaml.safe_load(opened_file)
