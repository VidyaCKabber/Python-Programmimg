def find_Fibonacci(n):
    fib_sequence = [0, 1]
    
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence
    
n = 5

res = find_Fibonacci(n)
print(res)
