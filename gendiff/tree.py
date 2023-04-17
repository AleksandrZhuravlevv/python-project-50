def children(string1, string2):
    if isinstance(string1, dict) and isinstance(string2, dict):
        return True
    elif type(string1) == type(string2):
        return False
    else:
        return False


def check_value(string):
    if isinstance(string, dict):
        for k, v in string.items():
            return {'= ' + k: v}
    else:
        return string


def diff_equals(ikey1, ikey2):
    result = {}
    for k1, v1 in ikey1.items():
        if k1 in ikey2 and v1 == ikey2[k1]:
            result['= ' + k1] = check_value(v1)
        if k1 in ikey2 and v1 != ikey2[k1] and not children(v1, ikey2[k1]):
            result['! ' + k1] = [check_value(v1), check_value(ikey2[k1])]
        if k1 not in ikey2:
            result['- ' + k1] = check_value(v1)
        if k1 in ikey2 and v1 != ikey2[k1] and children(v1, ikey2[k1]):
            result['= ' + k1] = diff_equals(v1, ikey2[k1])
    for k2, v2 in ikey2.items():
        if k2 not in ikey1:
            result['+ ' + k2] = check_value(v2)
    return result


def item_equals(item):
    result = {}
    for key, value in item.items():
        if type(value) is dict and key[0] == '=':
            result[key] = item_equals(value)
        elif type(value) is not dict:
            result['= ' + key] = value
        else:
            result['= ' + key] = item_equals(value)
    return result


def diff_lvl1(item1, item2):
    result = {}
    for k1, v1 in item1.items():
        if k1 in item2:
            result['= ' + k1] = diff_equals(v1, item2[k1])
        else:
            result['- ' + k1] = item_equals(v1)
    for k2, v2 in item2.items():
        if k2 not in item1:
            result['+ ' + k2] = item_equals(v2)
    return result


def formater(item):
    result = {}
    if type(item) is dict:
        result_sort = sorted(item.items(), key=lambda x: x[0][2:])
        for k, v in dict(result_sort).items():
            if type(v) is not dict:
                result[k] = v
            elif type(v) is dict:
                result[k] = formater(v)
    else:
        return item
    return result


def format_keys(item):
    res = {}
    for k, v in item.items():
        res[k] = formater(v)
    return dict(sorted(res.items(), key=lambda x: x[0][2:]))


def data_from_gendiff(item1, item2):
    for k, v in item1.items():
        if type(k) is not dict and type(v) is not dict:
            res_dict = diff_equals(item1, item2)
            return format_keys(res_dict)
        else:
            res_dict = diff_lvl1(item1, item2)
        return format_keys(res_dict)
