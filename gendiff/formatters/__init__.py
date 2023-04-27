from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


def get_formatter(formater):
    if formater == 'stylish':
        return get_stylish
    if formater == 'plain':
        return get_plain
    if formater == 'json':
        return get_json
    raise ValueError(f"Unrecognized formater: {formater}")
