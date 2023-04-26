def data_from_gendiff(data_1, data_2):
    diff = dict()
    for key in sorted(data_1.keys() | data_2.keys()):
        if key not in data_1:
            diff[key] = {
                'action': 'added',
                'value': data_2[key]
            }
        elif key not in data_2:
            diff[key] = {
                'action': 'removed',
                'value': data_1[key]
            }
        elif data_1[key] == data_2[key]:
            diff[key] = {
                'action': 'unchanged',
                'value': data_1[key]
            }
        elif isinstance(data_1[key], dict) and isinstance(data_2[key], dict):
            diff[key] = {
                'action': 'nested',
                'value': data_from_gendiff(data_1[key], data_2[key])
            }
        else:
            diff[key] = {
                'action': 'changed',
                'value': {
                    'old_value': data_1[key],
                    'new_value': data_2[key]
                }
            }
    return diff
