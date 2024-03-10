from src.ScriptToCode import MLSTC
from src.Convert import Convert

f = open("test.bs", "r")
code = f.read()
f.close()

code = MLSTC(code)
code = Convert(code)
exec(code)
