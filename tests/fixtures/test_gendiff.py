from gendiff.gendiff import generate_diff
import pytest
import json

file = open('./tests/fixtures/expected.txt', 'r')
result = file.read()


def test_generate_diff():
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == result
