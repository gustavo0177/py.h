def inverte_string_recursiva(s):
    if s == "":
        return ""
    else:
        return inverte_string_recursiva(s[1:])
    