def format_stylish(item):
    result = {}
    for k, v in item.items():
        if k[0] != '=' and k[0] != '!' or \
           k[0] == '=' and not isinstance(v, dict):
            result[k] = v
        elif k[0] == '!':
            result['- ' + k[2:]] = v[0]
            result['+ ' + k[2:]] = v[1]
        else:
            result[k] = func_re(v)
    return result


def func_re(item):
    result = {}
    for k, v in item.items():
        if k[0] == '!':
            result['- ' + k[2:]] = v[0]
            result['+ ' + k[2:]] = v[1]
        elif k[0] == '=' and isinstance(v, dict):
            result[k] = func_re(v)
        else:
            result[k] = v
    return result


def format_str(item, char=' ', count=2, depth=1):
    value = '{'
    if type(item) is dict:
        for k, v in item.items():
            if type(v) is dict:
                value = value + (f'\n{char * (depth * count)}{k}: '
                                 f'{format_str(v, char, count, depth+2)}')
            elif type(v) is not dict:
                value = value + f'\n{char * depth * count}{k}: {v}'
        return value + '\n' + char * ((depth * count) - count) + '}'
    else:
        return str(item)


def stylish(text):
    fstylish = format_stylish(text)
    dict_str = format_str(fstylish)
    result = (dict_str.replace('False', 'false').replace('None', 'null')
                      .replace('True', 'true').replace('=', ' '))
    return result
