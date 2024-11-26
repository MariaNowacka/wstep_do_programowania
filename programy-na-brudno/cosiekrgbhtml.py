def a(r):
    if len(r)<3:
        if len(r)==1:
            r='00'+r
        if len(r)==2:
            r='0'+r
    return r
