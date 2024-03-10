def isInt(value):
    isInt = ""
    try:
        int(value)
        isInt=True
    except:
        isInt=False
    return isInt