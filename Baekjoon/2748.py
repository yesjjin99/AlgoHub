fib = [-1]*100

def fibo(n):
    global fib
    if fib[n] != -1:
        return fib[n]
    if n < 2:
        fib[n] = n
        return fib[n]
    fib[n] = fibo(n-1) + fibo(n-2)
    return fib[n]

n = int(input())
print(fibo(n))
