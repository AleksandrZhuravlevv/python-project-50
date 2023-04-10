def stylish(diff_dict):
    sub_string = make_sub_string(diff_dict["children"], "", 1)
    return "{\n" + sub_string + "}"


def make_sub_string(sub_list, sub_string, depth):  # noqa: C901
    for item_dict in sub_list:
        if "children" in item_dict:
            sub_string += " " * (4 * depth) + item_dict["key"] + ": {\n"
            sub_string = make_sub_string(
                item_dict["children"], sub_string, depth + 1)
            sub_string += " " * (4 * depth) + "}\n"
        elif item_dict["type"] == "added":
            sub_string += " " * (4 * depth) + "+ " + item_dict["key"] + ": "
            sub_string += map_value(item_dict["value"]) + "\n"
        elif item_dict["type"] == "deleted":
            sub_string += " " * (4 * depth) + "- " + item_dict["key"] + ": "
            sub_string += map_value(item_dict["value"]) + "\n"
        elif item_dict["type"] == "unchanged":
            sub_string += " " * (4 * depth) + item_dict["key"] + ": "
            sub_string += map_value(item_dict["value"]) + "\n"
        elif item_dict["type"] == "updated":
            sub_string += " " * (4 * depth) + "- " + item_dict["key"] + ": "
            sub_string += map_value(item_dict["value1"]) + "\n"
            sub_string += " " * (4 * depth) + "+ " + item_dict["key"] + ": "
            sub_string += map_value(item_dict["value2"]) + "\n"
    return sub_string


def map_value(key_value):
    if isinstance(key_value, dict):
        return "{\n" + make_sub_string(key_value.items(), "", 1) + " " * 4 + "}"
    elif key_value is True:
        return "true"
    elif key_value is False:
        return "false"
    elif key_value is None:
        return "null"
    else:
        return str(key_value)
