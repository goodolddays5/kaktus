def func1(arg1, arg2):
    var7 = func2(arg2, arg1)
    var12 = func3(arg1, arg2)
    var35 = var15(var7, var12)
    var39 = func10(var35, var12)
    var40 = (935 ^ -272686304 ^ (var7 | var12 + 1080169513 + 376) + 388 + (arg2 ^ ((arg2 - var35 | arg1 | -185195187) ^ var35) & arg1)) - arg2
    var41 = var12 | (arg2 - arg1)
    var42 = (var39 ^ (arg1 - var35 + arg2 - (arg2 - var40) ^ var40)) - -100
    result = var39 ^ ((-12721589 | var7) ^ arg2 | var40 + arg2 - -872 + arg1) ^ var12
    return result
def func6(arg16, arg17):
    var18 = func9()
    var19 = (var18 | -250) ^ 495204341 - var18
    var20 = 659 ^ (182336422 + var19)
    var21 = var20 | (arg16 | 9) + var18
    if var19 < var21:
        var22 = arg16 - ((1067836880 ^ 95) - var21)
    else:
        var22 = var21 + (var19 - var20) + arg16
    var23 = arg17 & var20
    var24 = var18 ^ var23 | var18
    if var24 < var20:
        var25 = (arg16 ^ var21 - var19) - var19
    else:
        var25 = arg16 + var24
    if var19 < var20:
        var26 = -1488067460 ^ arg16
    else:
        var26 = var21 | (var21 - var20) + var21
    var27 = 295 | (-665 & var18 + var24)
    var28 = (var24 | var20) + var18 | var27
    var29 = (var28 & var19) & var24 | var21
    var30 = var29 & var24 + var21 | var20
    var31 = ((var24 & var19) ^ var23) - var29
    var32 = var19 | -471
    if var30 < var28:
        var33 = (var24 + (var29 & var29)) | var27
    else:
        var33 = var30 | ((arg16 | arg16) & var24)
    var34 = (11 - var18) - -297
    result = var24 & (var27 + -445162005 + ((var27 - (540 & var27) - var21 | var27 + var24 | var34) ^ var29)) - var29
    return result
def func9():
    func7()
    result = len(xrange(13))
    func8()
    return result
def func8():
    global len
    del len
def func7():
    global len
    len = lambda x : 5
def func5():
    closure = [-2]
    def func4(arg13, arg14):
        closure[0] += func6(arg13, arg14)
        return closure[0]
    func = func4
    return func
var15 = func5()
def func3(arg8, arg9):
    var10 = 0
    for var11 in xrange(11):
        var10 += var11 ^ -6 | var11
    return var10
def func2(arg3, arg4):
    var5 = 0
    for var6 in range(5):
        var5 += -2 | (var5 | var5)
    return var5
def func10(arg36, arg37):
    def func11(acc, rest):
        var38 = (0 - 8) & 8
        if acc == 0:
            return var38
        else:
            result = func11(acc - 1, var38)
            return result
    result = func11(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 43'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
