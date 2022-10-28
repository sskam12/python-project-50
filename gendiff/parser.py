"""Content parser"""


import json
import yaml
import os


def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension


def parse(file, file_extension):
    if file_extension == '.json':
        result = json.load(open(file))
    if file_extension == '.yml' or '.yaml':
        result = yaml.safe_load(open(file))
    return result
