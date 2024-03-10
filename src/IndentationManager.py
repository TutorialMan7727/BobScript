from src.types import types

def GetAndRemoveIndents(line):
    indents = 0
    new_line = []

    for token in line:
        if token[0] == types.indent:
            indents+=1
        else:
            new_line.append(token)
    
    return indents, new_line