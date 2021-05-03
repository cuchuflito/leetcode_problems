def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib = memoize(fib)

# print(recursive_fibo(70))
print(fib(40))

# complexity:
# recursive: TIME = O[N^2] SPACE = O[n] (stack)
# MEMOIZE:   TIME = O[N] SPACE = O[N] 
