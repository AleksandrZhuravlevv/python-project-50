def plain(diff_dict):
    def make_sub_string(sub_dict, path_name=""):
        result = []
        sorted_keys = sorted(sub_dict.keys())
        for key in sorted_keys:
            current_path = path_name + key
            current_value = sub_dict[key]
            if isinstance(current_value, dict):
                result.append(make_sub_string(
                    current_value, current_path + "."))
            elif isinstance(current_value, tuple):
                old_value, new_value = current_value
                if len(old_value) == 0:
                    result.append(f"Property '{current_path}"
                                  f"' was added with value:"
                                  f" {map_value(new_value['value'])}")
                elif len(new_value) == 0:
                    result.append(f"Property '{current_path}' was removed")
                elif old_value != new_value:
                    result.append(f"Property '{current_path}"
                                  f"' was updated. From"
                                  f" {map_value(old_value['value'])}"
                                  f" to {map_value(new_value['value'])}")
        return "\n".join(result)

    return make_sub_string(diff_dict)


def map_value(key_value):
    if isinstance(key_value, dict):
        return "[complex value]"
    elif key_value is True:
        return "true"
    elif key_value is False:
        return "false"
    elif key_value is None:
        return "null"
    elif isinstance(key_value, int):
        return str(key_value)
    else:
        return f"'{key_value}'"
