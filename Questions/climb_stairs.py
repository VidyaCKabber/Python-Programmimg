# Problem: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example:
# Input: n = 3
# Output: 3 (1 step + 1 step + 1 step, 1 step + 2 steps, 2 steps + 1 step)

def climb_stairs(n):
    if n <= 1:
        return 1
        
    prev_2 , prev_1 = 1, 1
    
    for i in range(2, n+1):
        current = prev_2 + prev_1
        prev_2 = prev_1
        prev_1 = current
        
    return prev_1
    
print(climb_stairs(4))
