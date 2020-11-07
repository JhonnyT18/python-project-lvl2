# -*- coding: utf-8 -*-


from gendiff.gendiff import generate_diff


file = open('tests/fixtures/expected.txt', 'r')
result = file.read()


def test_gendiff():
    assert result == generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')  # noqa: E501
