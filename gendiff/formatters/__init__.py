from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json_f


def get_formatter(formater):
    if formater == 'stylish':
        return stylish
    if formater == 'plain':
        return plain
    if formater == 'json':
        return json_f
    raise ValueError(f"Unrecognized formater: {formater}")
