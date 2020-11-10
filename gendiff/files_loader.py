# -*- coding: utf-8 -*-
import os
import json
import yaml


def get_type(file_path):
    return os.path.splitext(file_path)[1]


def to_load(file_path):
    _type = get_type(file_path)
    if _type == '.json':
        return json.load(open(file_path))
    else:
        return yaml.safe_load(open(file_path))
