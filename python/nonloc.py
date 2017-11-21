k = 100
m = 10
n = 1

def show():
    print(n)

def show_g():
    global n
    print(n)

def modify():
    n = 8

def modify_g():
    global n
    n = 9


def big_foo():
    p = 'serious'
    q = 'error'
    r = 'number'

    k = 200
    global m
    m += 1  # has effect
    n = 2

    def foo():
        print(p, q, r, sep=' ', end=' ')
        print(k, m, n, sep='.')

    def bar():
        nonlocal p, q, r
        global k, m, n
        print(p, q, r, sep=' ', end=' ')
        print(k, m, n, sep='.')

    def modify():
        global p
        nonlocal q
        p = 'funny'     # no effect, p is nonlocal, not global
        q = 'warning'   # changes nonlocal q
        r = 'NUMBER'    # no effect, r is local

        global k
        k = 101         # changes global k
        # nonlocal m    # SyntaxError: no binding for nonlocal 'm' found
        m = 20          # no effect, just new local variable
        nonlocal n
        n = 3           # changes nonlocal n from big_foo that shadows the global

    foo()
    bar()

    modify()

    foo()
    bar()




# eg_1 = [show(), show_g(), modify(), show(), show_g(), modify_g(), show(), show_g()]
# shows 7 7 7 7 9 9


big_foo()
# shows:
# serious error number 200.11.2
# serious error number 100.11.1
# serious warning number 200.11.3
# serious warning number 101.11.1