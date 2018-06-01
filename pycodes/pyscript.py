def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


for idx, fn in enumerate(fib()):
    print('{i:3}:  {f:5}'.format(i=idx, f=fn))
    if(idx == 20):
        break
