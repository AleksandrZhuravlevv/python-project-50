def children(item1, item2):
    return isinstance(item1, dict) and isinstance(item2, dict)


def check_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return str(value)


def diff_equals(item1, item2):
    result = {}
    for key1, value1 in item1.items():
        match key1:
            case key1 if key1 in item2 and value1 == item2[key1]:
                result[key1] = check_value(value1)
            case key1 if key1 in item2 and not children(value1, item2[key1]):
                result[key1] = [check_value(value1), check_value(item2[key1])]
            case key1 if key1 not in item2:
                result[key1] = check_value(value1)
            case key1 if key1 in item2 and children(value1, item2[key1]):
                result[key1] = diff_equals(value1, item2[key1])

    for key2, value2 in item2.items():
        if key2 not in item1:
            result[key2] = check_value(value2)

    return result


def item_equals(item):
    result = {}
    for key, value in item.items():
        if isinstance(value, dict) and key[0]:
            result[key] = item_equals(value)
        elif not isinstance(value, dict):
            result[key] = value
        else:
            result[key] = item_equals(value)
    return result


def diff_lvl1(item1, item2):
    result = {}
    for key1, value1 in item1.items():
        if key1 in item2:
            result[key1] = diff_equals(value1, item2[key1])
        else:
            result[key1] = item_equals(value1)

    for key2, value2 in item2.items():
        if key2 not in item1:
            result[key2] = item_equals(value2)

    return result


def formatter(item):
    result = {}
    if isinstance(item, dict):
        result_sort = sorted(item.items(), key=lambda x: x[0])
        for key, value in dict(result_sort).items():
            if not isinstance(value, dict):
                result[key] = value
            else:
                result[key] = formatter(value)
    else:
        return item
    return result


def format_keys(item):
    res = {}
    for key, value in item.items():
        res[key] = formatter(value)
    return dict(sorted(res.items()))


def data_from_gendiff(item1, item2):
    if not isinstance(item1, dict) or not isinstance(item2, dict):
        raise ValueError('Input should be dictionaries')
    diff_dict = diff_lvl1(item1, item2)
    return format_keys(diff_dict)
