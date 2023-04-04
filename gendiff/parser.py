import json
import yaml


def definition_form(file_path):
    if file_path[-4:] == "json":
        return dict(sorted((json.load(open(file_path))).items()))
    elif file_path[-4:] == "yaml" or file_path[-3:] == "yml":
        return dict(sorted((yaml.safe_load(open(file_path))).items()))
    else:
        raise ValueError('Unsupported format. '
                         'Next formats are supported: .json .yaml .yml{}')