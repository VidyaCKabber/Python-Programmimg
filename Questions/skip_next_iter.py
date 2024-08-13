# A software development company is working to create several shared computing systems throughout an office.

# For computers to be on the same network, there are the following constraints:

# 1. They must be adjacent to one another.
# 2. There must be a minimum number of computers.
# 3. The total processing speed of the network (the sum of each computer's processing speed) must be at least a certain threshold.
# 4. A computer can only belong to one network.

# Example

# n = 6

# speed = 15,7, 9, 12, 10, 131

# minComps = 2

# speedThreshold = 15

# There are n = 6 computers. Each network needs to have a

# minimum of minComps = 2 computers and a total

# processing speed of at least speedThreshold = 15.

# - The first network includes the second, third, and fourth computers, which results in a total processing speed of
# 7+9+12 = 28. This is above the threshold of 15.
# - The second network includes the fifth and sixth computers,
# with a total processing speed of 10+13 = 23.

# The maximum number of networks that can be formed is 2.

n = 6
speed = [5,7, 9, 12, 10, 13, 3, 1, 1, 10]
minComps = 2
speedThreshold = 15
add = speed[0]
count = 0
i = 1

while i < len(speed):
    add += int(speed[i])
    if add >= speedThreshold:
        count +=1
        add = 0
        add = speed[i+1]
        i+=2
    else:
        i+=1
        
print(count)
        
    
