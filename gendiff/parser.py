import json
import yaml


def parsing(file):
    if file[-4:] == 'json':
        return json.load(open(file))
    if file[-4:] == 'yaml' or file[-3:] == 'yml':
        return yaml.safe_load(open(file))
    else:
        return 'wrong format'
