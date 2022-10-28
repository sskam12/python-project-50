from gendiff.gendiff import generate_diff
import pytest
import json

file_json = open('./tests/fixtures/expected_json.txt', 'r')
result_json = file_json.read()


def test_generate_diff():
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == result_json


file_yaml = open('./tests/fixtures/expected_yaml.txt', 'r')
result_yaml = file_yaml.read()


def test_generate_diff():
    assert generate_diff('./tests/fixtures/file1.yml', './tests/fixtures/file2.yml') == result_yaml
