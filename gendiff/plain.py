def plain(diff_dict):
    return make_sub_string(diff_dict['children'], "")


def make_sub_string(sub_list, path_name):
    sub_string = ""
    for item_dict in sub_list:
        if item_dict['type'] == 'added':
            sub_string += make_added_string(
                item_dict['key'], item_dict['value'], path_name)
        elif item_dict['type'] == 'deleted':
            sub_string += make_deleted_string(item_dict['key'], path_name)
        elif item_dict['type'] == 'updated':
            sub_string += make_updated_string(
                item_dict['key'], item_dict['value1'],
                item_dict['value2'], path_name)
        elif 'children' in item_dict:
            sub_string += make_sub_string(
                item_dict['children'], path_name + item_dict['key'] + ".")
    return sub_string


def make_added_string(key, value, path_name):
    return f"Property '{path_name}{key}' " \
           f"was added with value: {map_value(value)}\n"


def make_deleted_string(key, path_name):
    return f"Property '{path_name}{key}' was removed\n"


def make_updated_string(key, value1, value2, path_name):
    return f"Property '{path_name}{key}'" \
           f" was updated. From {map_value(value1)} to {map_value(value2)}\n"


def map_value(key_value):
    if isinstance(key_value, dict):
        return "[complex value]"
    elif isinstance(key_value, bool):
        return str(key_value).lower()
    elif key_value is None:
        return "null"
    else:
        return str(key_value)
