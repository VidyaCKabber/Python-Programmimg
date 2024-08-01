def head(n):
    
    if n==0:
        return
    
    head(n-1)
    print(n)
    
head(5)
