def check_value(value):
    if type(value) is dict:
        return '[complex value]'
    elif type(value) is int:
        return value
    else:
        return "'" + str(value) + "'"


def res_plain(item, depth=''):
    result = ''
    for key, value in item.items():
        if key[0] == '-':
            result += f"Property '{depth}{key[2:]}' was removed\n"
        if key[0] == '+':
            result += (f"Property '{depth}{key[2:]}' "
                       f"was added with value: {check_value(value)}\n")
        if key[0] == '!':
            result += (f"Property '{depth}{key[2:]}' was updated."
                       f" From {check_value(value[0])}"
                       f" to {check_value(value[1])}\n")
        if key[0] == '=' and type(value) is dict:
            result += depth_plain(key, value)
    return result


def depth_plain(key, value):
    result = ''
    for k1, v1 in value.items():
        if k1[0] != '=':
            result += res_plain({k1: v1}, depth=key[2:] + '.')
        if k1[0] == '=' and type(v1) is dict:
            result += depth_plain(key + "." + k1[2:], v1)
    return result


def replace_char(text):
    result = (text.replace("'False'", 'false').replace("'None'", 'null')
                  .replace("'True'", 'true'))
    final = result.rstrip('\n')
    return final


def plain(item):
    res1 = res_plain(item)
    rep_char = replace_char(res1)
    return rep_char
