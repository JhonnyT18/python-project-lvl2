# -*- coding: utf-8 -*-


from gendiff.gendiff import generate_diff


file = open('tests/fixtures/expected.txt', 'r')
result = file.read()


def test_gendiff_json():
    assert result == generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')  # noqa: E501


def test_gendiff_yaml():
    assert result == generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')  # noqa: E501
