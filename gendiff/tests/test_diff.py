# -*- coding: utf-8 -*-


from gendiff.gendiff import generate_diff


file = open('gendiff/tests/fixtures/expected.txt', 'r')
result = file.read()


def test_gendiff():
    assert result == generate_diff('gendiff/tests/fixtures/file1.json', 'gendiff/tests/fixtures/file2.json')  # noqa: E501
