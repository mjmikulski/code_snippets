def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper

c = 0

@memoize
def fib(n):
    global c
    c += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(6))
c = 0
print(fib(4))

print('c: ', c)  # c:  0