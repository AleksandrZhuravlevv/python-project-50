import json

TAB = '    '
ACTION_STATUS = {
    'added': '  + ',
    'removed': '  - ',
    'unchanged': '    '
}


def get_str(value):
    """
    Convert value from Python to json/yaml format
    """
    if value is None or isinstance(value, bool):
        return json.dumps(value)
    return str(value)


def stringify(data, depth):
    if isinstance(data, dict):
        result = ['{']
        for key, value in data.items():
            result.append(f'{TAB * depth}{key}: {stringify(value, depth + 1)}')
        result.append(f'{TAB * (depth - 1)}}}')
        return '\n'.join(result)
    return get_str(data)


def get_stylish(data, depth=1):
    result = ['{']
    for key, sub_dict in data.items():
        action = sub_dict.get('action')
        value = sub_dict.get('value')
        if action == 'nested':
            result.append(f'{TAB * depth}{key}: {get_stylish(value, depth+1)}')
        elif action == 'changed':
            old_value = stringify(value.get('old_value'), depth + 1)
            new_value = stringify(value.get('new_value'), depth + 1)
            result.append(f'{TAB * (depth-1)}'
                          f'{ACTION_STATUS["removed"]}{key}: {old_value}')
            result.append(f'{TAB * (depth-1)}'
                          f'{ACTION_STATUS["added"]}{key}: {new_value}')
        else:
            result.append(f'{TAB * (depth-1)}'
                          f'{ACTION_STATUS[action]}'
                          f'{key}: {stringify(value, depth + 1)}')
    result.append(f'{TAB * (depth - 1)}}}')
    return '\n'.join(result)
