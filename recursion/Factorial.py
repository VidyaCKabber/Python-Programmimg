def factorial_head(n):
    
    if n == 0:
        return 1
    
    res = factorial_head(n-1)
    out = n * res
    return out
    
print(factorial_head(5))


def factorial_tail(n, accumulator=1):
    
    if n==0:
        return accumulator
        
    return factorial_tail(n-1, n * accumulator)
    
    
print(factorial_tail(5))
