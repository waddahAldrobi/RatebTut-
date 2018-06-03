
def fib(n):
    if n<=1:
        return(n,0)
    else:
        (a,b)=fib(n-1)
        return(a+b,a)

Nfib= 2
print ( fib(Nfib)[0] + fib(Nfib)[1]  )