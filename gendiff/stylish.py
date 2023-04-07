def stylish(diff_dict):
    def make_sub_string(sub_dict, sub_string, depth):
        indent = "    " * depth
        sub_string += indent + "{\n"
        for key, value in sorted(sub_dict.items()):
            if isinstance(value, dict):
                sub_string += indent + "  " + key + ": "
                sub_string = make_sub_string(value, sub_string, depth + 1)
            elif isinstance(value, tuple):
                sub_string += indent
                if len(value[0]) == 0:
                    sub_string += "+ " + key + ": " + map_value(
                        value[1]["value"]) + "\n"
                elif len(value[1]) == 0:
                    sub_string += "- " + key + ": " + map_value(
                        value[0]["value"]) + "\n"
                elif value[0]["value"] == value[1]["value"]:
                    sub_string += "  " + key + ": " + map_value(
                        value[0]["value"]) + "\n"
                else:
                    sub_string += "- " + key + ": " + map_value(
                        value[0]["value"]) + "\n"
                    sub_string += indent + "+ " + key + ": " + map_value(
                        value[1]["value"]) + "\n"
        sub_string += indent + "}\n"
        return sub_string

    result = make_sub_string(diff_dict, "", 0)
    return result


def map_value(key_value):
    if isinstance(key_value, dict):
        return "{\n" + map_dict_value(key_value, "    ", 1) + "    " + "}"
    elif str(key_value) == 'True':
        return "true"
    elif str(key_value) == 'False':
        return "false"
    elif str(key_value) == 'None':
        return "null"
    else:
        return "'" + str(key_value) + "'"


def map_dict_value(value, indent, depth):
    result = ""
    for key, val in value.items():
        if isinstance(val, dict):
            result += indent * depth + key + ": {\n" + map_dict_value(
                val, indent, depth + 1) + indent * depth + "}\n"
        else:
            result += indent * depth + key + ": " + map_value(val) + "\n"
    return result
