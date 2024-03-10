from src.types import types
from src.Is import isInt

def STC(line):
    chars = list(line)
    obj = []

    current_text = ''
    is_string_itteration = False

    ammount_of_tab_spaces = 0

    for i, char in enumerate(chars):
        if is_string_itteration:
            if char == '"':
                is_string_itteration = False
                obj.append((types.string, current_text))
                current_text = ''
            else:
                current_text += char
        elif char == '"':
            is_string_itteration = True
        elif char == ' ' or i == len(chars)-1:
            if char != ' ':
                current_text += char

            if current_text == "":
                can_indent = True
                for i in obj:
                    if i[0] != types.indent:
                        can_indent = False

                if can_indent:
                    ammount_of_tab_spaces+=1
                    if ammount_of_tab_spaces == 4:
                        obj.append((types.indent, types.null))
                        ammount_of_tab_spaces = 0
            elif current_text == "true" or current_text == "True":
                obj.append((types.boolean, True))
            elif current_text == "false" or current_text == "False":
                obj.append((types.boolean, False))
            elif current_text in ["+", "-", "*", "/", "="]:
                obj.append((types.operation, current_text))
            elif current_text == "null":
                obj.append((types.null, types.null))
            elif isInt(current_text):
                obj.append((types.integer, int(current_text)))
            else:
                obj.append((types.keyword, current_text))
            current_text = ''
        else:
            current_text += char

    return obj

def MLSTC(code):
    obj = []
    for line in code.split('\n'):
        obj.append(STC(line))
    return obj