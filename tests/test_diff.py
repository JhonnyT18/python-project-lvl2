# -*- coding: utf-8 -*-


from gendiff.gendiff import generate_diff


def test_gendiff_json():
    with open('tests/fixtures/expected.txt', 'r') as result:
        assert result.read() == generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')  # noqa: E50


def test_gendiff_yaml():
    with open('tests/fixtures/expected.txt', 'r') as result:
        assert result.read() == generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')  # noqa: E501


def test_gendiff_tree_json():
    with open('tests/fixtures/expected_tree.txt', 'r') as result:
        assert result.read() == generate_diff('tests/fixtures/file_tree1.json', 'tests/fixtures/file_tree2.json')


def test_gendiff_tree_yaml():
    with open('tests/fixtures/expected_tree.txt', 'r') as result:
        assert result.read() == generate_diff('tests/fixtures/file_tree1.yaml', 'tests/fixtures/file_tree2.yaml')


def test_gendiff_plain():
    with open('tests/fixtures/expected_for_plain.txt', 'r') as result:
        assert result.read() == generate_diff('tests/fixtures/file_tree1.json', 'tests/fixtures/file_tree2.yaml', 'plain')
