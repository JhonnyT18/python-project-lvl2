# -*- coding: utf-8 -*-
from gendiff.gendiff import generate_diff
import json
import pytest


path_to_fixtures = 'tests/fixtures/'


cases = [
    (
        path_to_fixtures + 'file1.json',
        path_to_fixtures + 'file2.json',
        'stylish',
        path_to_fixtures + 'expected.txt'
    ),
    (
        path_to_fixtures + 'file1.yaml',
        path_to_fixtures + 'file2.yaml',
        'stylish',
        path_to_fixtures + 'expected.txt'
    ),
    (
        path_to_fixtures + 'file_tree1.json',
        path_to_fixtures + 'file_tree2.json',
        'stylish',
        path_to_fixtures + 'expected_tree.txt'
    ),
    (
        path_to_fixtures + 'file_tree1.yaml',
        path_to_fixtures + 'file_tree2.yaml',
        'stylish',
        path_to_fixtures + 'expected_tree.txt'
    ),
    (
        path_to_fixtures + 'file_tree1.json',
        path_to_fixtures + 'file_tree2.json',
        'plain',
        path_to_fixtures + 'expected_extent_plain.txt'
    ),
    (
        path_to_fixtures + 'file_tree1.json',
        path_to_fixtures + 'file_tree2.json',
        'json',
        path_to_fixtures + 'expected_extent_json.json'
    )]


@pytest.mark.parametrize('path_to_first, path_to_second, form, expected', cases)
def test_generate_diff(path_to_first, path_to_second, form, expected):
    with open(expected, 'r') as file:
        if form == 'json':
            assert json.load(file) == json.loads(generate_diff(path_to_first, path_to_second, form))
        else:
            assert file.read() == generate_diff(path_to_first, path_to_second, form)
