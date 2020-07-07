a = 9


def f(a=3):
    print(globals())
    print(locals())
    print(a)
    b = 3
    print(b)


class A:
    a=8
    print(a)
    print(globals())
    print(locals())


#f()
