import m2

def f1():
    print('f1')
    getattr(m2, 'f2')()

def f3():
    print('f3')