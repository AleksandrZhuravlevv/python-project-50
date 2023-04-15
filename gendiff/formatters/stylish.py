def format_stylish(item):
    result = {}
    for k, v in item.items():
        if k[0] != '=' and k[0]\
                != '!' or k[0] == '=' and not isinstance(v, dict):
            result[k] = v
        elif k[0] == '!':
            result['- ' + k[2:]] = v[0]
            result['+ ' + k[2:]] = v[1]
        else:
            result[k] = map_dict_value(v)
    return result


def map_dict_value(value):
    result = {}
    for k, v in value.items():
        if isinstance(v, dict):
            result[k] = map_dict_value(v)
        else:
            result[k] = v
    return result


def format_str(item, char=' ', count=2, depth=1):
    if isinstance(item, dict):
        result = '{\n'
        for k, v in item.items():
            if isinstance(v, dict):
                result += f"{char * (depth * count)}" \
                          f"{k}: {format_str(v, char, count, depth + 1)}\n"
            else:
                result += f"{char * (depth * count)}{k}: {v}\n"
        result += char * ((depth - 1) * count) + "}"
        return result
    else:
        return str(item)


def stylish(text):
    fstylish = format_stylish(text)
    dict_str = format_str(fstylish)
    result = dict_str.replace('False', 'false')\
        .replace('None', 'null').replace('True', 'true')
    return result
