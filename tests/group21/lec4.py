def is_even_with_return(i):
    print("with return")
    return i % 2 == 0

def is_even_without_return(i):
    print("without return")
    i % 2  # 沒有 return，回傳 None

def bisection_cuberoot_approx(x, epsilon):
    low = 0.0
    high = x
    guess = (high + low)/2.0
    while abs(guess**3 - x) >= epsilon:
        if guess**3 < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
    return guess

def add_returning_function():
    def x(a, b):
        return a + b
    return x

def f_scope(x):
    x = x + 1
    print('in f(x): x =', x)
    return x

def g_scope(x):
    def h(x):
        x = x+1
        print("in h(x): x =", x)
    x = x + 1
    print("in g(x): x =", x)
    h(x)
    return x

