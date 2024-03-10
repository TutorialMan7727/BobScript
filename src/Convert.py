from src.types import types
from src.IndentationManager import GetAndRemoveIndents

def Convert(code):
    new_code = ""

    for line in code:
        indents, line = GetAndRemoveIndents(line)
        # print(line)

        if line == []:
            continue
        elif line[0][0] != types.keyword:
            continue
        elif line[0][1][0] == "/" and line[0][1][1] == "/":
            continue

        code_line = ""
        brackets_opened = False
        
        if line[0][0] == types.keyword and line[0][1] == "if":
            if line[1][0] == types.boolean:
                code_line = "if " + str(line[1][1]) + ":"
            else:
                code_line = "if "
                if line[1][0] != types.string:
                    code_line += str(line[1][1])
                else:
                    code_line += "'"+str(line[1][1])+"'"
                code_line += " == "
                if line[2][0] != types.string:
                    code_line += str(line[2][1])
                else:
                    code_line += "'"+str(line[2][1])+"'"
                code_line += ":"
        elif line[0][0] == types.keyword and line[1][0] == types.operation and line[1][1] == "=":
            for token in line:
                if token[0] != types.string:
                    code_line += str(token[1])
                else:
                    code_line += "'"+str(token[1])+"'"
        elif line[0][0] == types.keyword and line[0][1] == "def":
            code_line = "def " + str(line[1][1]) +  "("
            if len(line) != 2:
                for parm in line[2:]:
                    code_line += str(parm[1])+","
                code_line = code_line[:-1] + "):"
            else:
                code_line += "):"
        else:
            for token in line:
                if token[0] == types.keyword and token[1][0] != "-":
                    if not brackets_opened:
                        code_line += token[1]+"."
                elif token[0] == types.keyword:
                    if not brackets_opened:
                        code_line = code_line[:-1] + "(" + str(token[1][1:])+","
                        brackets_opened = True
                else:
                    if not brackets_opened:
                        code_line = code_line[:-1] + "("
                        brackets_opened = True

                    if token[0] == types.string:
                        code_line += "'"+token[1]+"',"
                    else:
                        code_line += str(token[1])+","
                
            code_line = code_line[:-1] + ")"
        
        for i in range(indents):
            code_line = "   " + code_line

        new_code += code_line+"\n"
    
    return new_code