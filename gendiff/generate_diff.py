from gendiff.parser import definition_form


def stulish(result, lvl=2):
    final = "{"
    for str_result in result:
        if result[str_result] is True or result[str_result] is False:
            result[str_result] = str(result[str_result]).lower()
        elif result[str_result] is None:
            result[str_result] = "null"
        else:
            result[str_result] = str(result[str_result])
        final = final + "\n" + str(str_result) + ': ' + result[str_result]
    final = final + "\n" + (" " * lvl) + "}"
    return final


def generate_key_lists(file1, file2,):
    common = list()
    n_common = list()
    for key1 in file1:
        if key1 in file2:
            common.append(key1)
        else:
            n_common.append(key1)
    for key2 in file2:
        if key2 in file1:
            continue
        else:
            n_common.append(key2)
    return common, n_common


def generate(file1, file2, lvl=2):
    result = dict()
    common, not_common = generate_key_lists(file1, file2)[0], generate_key_lists(file1, file2)[1]
    for key_common in common:
        new_key1 = (" " * lvl) + "- " + key_common
        new_key2 = (" " * lvl) + "+ " + key_common
        new_key_all = (" " * lvl) + "  " + key_common
        if type(file1[key_common]) is dict and type(file2[key_common]) is dict:
            result[new_key_all] = stulish(generate(file1[key_common], file2[key_common], lvl + 4), lvl + 2)
        elif type(file1[key_common]) is dict and type(file2[key_common]) is not dict:
            result[new_key1] = stulish(generate(file1[key_common], file1[key_common], lvl + 4), lvl + 2)
            result[new_key2] = file2[key_common]
        elif type(file1[key_common]) is not dict and type(file2[key_common]) is dict:
            result[new_key1] = file1[key_common]
            result[new_key2] = stulish(generate(file2[key_common], file2[key_common], lvl + 4), lvl + 2)
        elif file1[key_common] != file2[key_common]:
            result[new_key1] = file1[key_common]
            result[new_key2] = file2[key_common]
        else:
            result[new_key_all] = file1[key_common]
    for key_not_common in not_common:
        if key_not_common in file1:
            new_key1 = (" " * lvl) + "- " + key_not_common
            if type(file1[key_not_common]) is dict:
                result[new_key1] = stulish(generate(file1[key_not_common], file1[key_not_common], lvl + 4), lvl + 2)
            else:
                result[new_key1] = file1[key_not_common]
        elif key_not_common in file2:
            new_key2 = (" " * lvl) + "+ " + key_not_common
            if type(file2[key_not_common]) is dict:
                result[new_key2] = stulish(generate(file2[key_not_common], file2[key_not_common], lvl + 4), lvl + 2)
            else:
                result[new_key2] = file2[key_not_common]
    return result


def return_result(file_path1, file_path2, formater="stylish"):
    file1 = definition_form(file_path1)
    file2 = definition_form(file_path2)
    if formater == "stylish":
        return stulish(generate(file1, file2))



