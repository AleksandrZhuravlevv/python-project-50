import json


def to_str(value):
    """
    Convert value from Python to plain format
    """
    if value is None or isinstance(value, bool):
        return json.dumps(value)
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, dict):
        return '[complex value]'
    return value


def get_plain(data, path=''):
    result = []
    for key, sub_dict in data.items():
        action = sub_dict.get('action')
        value = sub_dict.get('value')
        full_path = path + f'.{str(key)}' if path else str(key)
        if action == 'nested':
            result.append(get_plain(value, full_path))
        elif action == 'added':
            result.append(f'Property \'{full_path}\' '
                          f'was added with value: {to_str(value)}')
        elif action == 'removed':
            result.append(f'Property \'{full_path}\' was removed')
        elif action == 'changed':
            result.append(
                f'Property \'{full_path}\' was updated. '
                f'From {to_str(value.get("old_value"))} '
                f'to {to_str(value.get("new_value"))}')
    return '\n'.join(result)
