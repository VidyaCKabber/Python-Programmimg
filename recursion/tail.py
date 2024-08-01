def tail(n):
    if n == 0:
        return
    print(n)
    tail(n-1)
    
tail(5)
