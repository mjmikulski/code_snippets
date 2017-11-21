from time import sleep

def fib():
    a, b = 0, 1
    while True:
        yield b
        (a, b) = (b, a+b)


for n in fib():
    print(n)
    sleep(0.5)