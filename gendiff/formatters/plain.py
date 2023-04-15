def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return f"'{str(value)}'"


def format_plain(item, path=''):
    result = []
    for key, value in item.items():
        full_path = f"{path}.{key[2:]}" if key[0] == '!' else f"{path}{key}"
        if key[0] == '-':
            result.append(f"Property '{full_path}' was removed")
        elif key[0] == '+':
            result.append(f"Property '{full_path}' was"
                          f" added with value: {format_value(value)}")
        elif key[0] == '!':
            old_value = format_value(value[0])
            new_value = format_value(value[1])
            result.append(f"Property '{full_path}' was"
                          f" updated. From {old_value} to {new_value}")
        elif key[0] == '=' and isinstance(value, dict):
            result.extend(format_plain(value, path=f"{full_path}."))
    return result


def plain(item):
    return "\n".join(format_plain(item))[1:]
