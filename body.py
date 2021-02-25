def finder(num, words, args, bdwords=None):
    if bdwords is None:
        bdwords = []
    arr = []
    for j in words:
        swtch = True
        for k in args:
            if not (args[k] in j[int(k) - 1:int(k) - 1 + len(args[k]):]):
                swtch = False
        if len(j) == num and swtch:
            arr.append(j)
    return arr


def last_check(lst, bdwords):
    swtch = True
    arr = []
    for j in lst:
        swtch = True
        for i in bdwords:
            if i in j:
                swtch = False
        if swtch:
            arr.append(j)
    return arr


