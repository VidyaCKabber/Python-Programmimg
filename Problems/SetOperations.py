Task
# You have a non-empty set , and you have to execute  commands given in  lines.

# The commands will be pop, remove and discard.

# Input Format

# The first line contains integer , the number of elements in the set .
# The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer , the number of commands.
# The next  lines contains either pop, remove and/or discard commands followed by their associated value.

# Constraints



# Output Format

# Print the sum of the elements of set  on a single line.

# Sample Input

# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5
# Sample Output

# 4

# ============================================
n = int(input())
elements = set(map(int, input().split()))

N = int(input())
cmds = []
if all(x>=0 and x<=9 for x in elements):
    for i in range(N):
        cmds.append(input())
    for cmd in cmds:
        if(len(elements) > 1):
            if 'pop' in cmd:
                if elements:
                    elements.pop()
            elif 'remove' in cmd:
                elements.discard(int(cmd[-1]))
            elif 'discard' in cmd:
                elements.discard(int(cmd[-1]))
    print(sum(elements))
        
# ============================================
# Read the number of elements as an integer
n = int(input())

elements = set(map(int, input().split()))

num_commands = int(input())

for _ in range(num_commands):
    command = input().split()
    if command[0] == "pop":
        if elements:
            elements.pop()
    elif command[0] == "remove":
        value = int(command[1])
        elements.discard(value)
    elif command[0] == "discard":
        value = int(command[1])
        elements.discard(value)
print(sum(elements))

    
