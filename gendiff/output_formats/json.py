# -*- coding: utf-8 -*-
import json


def render(input_data):
    return json.dumps(input_data, sort_keys=True, indent=4) + '\n'
