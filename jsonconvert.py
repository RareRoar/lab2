def to_json(obj):
    # dict
    if type(obj) == dict:
        result = "{"
        for key in obj:
            result += "{}: {}, ".format(to_json(key), to_json(obj[key]))
        return result[:-2] + "}"

    # list
    if type(obj) == list:
        result = "["
        for element in obj:
            result += "{}, ".format(to_json(element))
        return result[:-2] + "]"

    # primitive
    if type(obj) == int:
        return str(obj)
    if type(obj) == float:
        return str(obj)
    if type(obj) == str:
        return "\"{}\"".format(obj)
    if type(obj) == tuple:
        return to_json(list(obj))
    if obj is None:
        return "null"
    if obj:
        return "true"
    if not obj:
        return "false"


# split string by ',' considering quotes
def _to_list(string):
    result = []
    word = ""
    quot_flag = False
    for char in string:
        if char == ',' and not quot_flag:
            if not result:
                result.append(word)
            else:
                result.append(word[2:])
            word = ""
        word += char
        if char == '\"':
            quot_flag = not quot_flag
    if not result:
        result.append(word)
    else:
        result.append(word[2:])
    return result


# split key: value pair considering quotes
def _to_pair(string):
    result = []
    word = ""
    flag = False
    for char in string:
        if char == '\"':
            flag = not flag
        if char == ':' and not flag:
            result.append(word)
            word = ""
        word += char
    result.append(word[2:])
    return result


def from_json(string):
    if string[0] == '[' and string[-1] == ']':
        return [from_json(element) for element in _to_list(string[1:-1])]
    if string[0] == '{' and string[-1] == '}':
        temp = [_to_pair(element) for element in _to_list(string[1:-1])]
        result = {from_json(element[0]): from_json(element[1]) for element in temp}
        return result
    if string[0] == '\"':
        return string[1:-1]
    if string == "true":
        return True
    if string == "false":
        return False
    if string == "null":
        return None
    if string.find('.') != -1:
        return float(string)
    return int(string)
