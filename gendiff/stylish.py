def build_diff(tree, depth=0):
    result = ""
    indent = build_indent(depth)

    if tree["type"] == "root":
        result += "{\n"
        for child in tree["children"]:
            result += build_diff(child, depth + 1)
        result += f"{indent}}}"
    else:
        name_of_property = tree["key"]
        type_of_property = tree["type"]
        value = map_value(tree["value"], depth)

        if type_of_property == "parent":
            result += f"{indent}{name_of_property}: {{\n"
            for child in tree["children"]:
                result += build_diff(child, depth + 1)
            result += f"{indent}}}\n"

        elif type_of_property == "added":
            result += f"{indent}+ {name_of_property}: {value}\n" # noqa

        elif type_of_property == "deleted":
            result += f"{indent}- {name_of_property}: {value}\n" # noqa

        elif type_of_property == "unchanged":
            result += f"{indent}  {name_of_property}: {value}\n" # noqa

        elif type_of_property == "updated":
            old_value = map_value(tree["value1"], depth)
            new_value = map_value(tree["value2"], depth)
            result += f"{indent}- {name_of_property}: {old_value}\n" # noqa
            result += f"{indent}+ {name_of_property}: {new_value}\n" # noqa

    return result


def map_value(key_value, depth):
    if isinstance(key_value, dict):
        return map_dict_value(key_value, depth + 1)
    elif key_value is True:
        return "true"
    elif key_value is False:
        return "false"
    elif key_value is None:
        return "null"
    else:
        return str(key_value)


def map_dict_value(value, depth):
    indent = build_indent(depth)
    sub_string = ""
    for key, val in value.items():
        if isinstance(val, dict):
            sub_string += f"{indent}    {key}: {{\n"
            sub_string += f"{map_dict_value(val, depth + 1)}"
            sub_string += f"{indent}    }}\n"
        else:
            val = map_value(val, depth)
            sub_string += f"{indent}    {key}: {val}\n"

    return sub_string


def build_indent(depth):
    return "    " * depth
