def max_apples_within_range(K, N, apple_sizes):
    apple_sizes.sort()  # Sort the apple sizes in ascending order
    max_apples = 0

    for i in range(N):
        for j in range(i, N):
            if apple_sizes[j] - apple_sizes[i] <= K:
                max_apples = max(max_apples, j - i + 1)

    return max_apples

# Read input
K = int(input())
N = int(input())
apple_sizes = [int(input()) for _ in range(N)]

# Calculate and print the maximum number of apples that can be selected
result = max_apples_within_range(K, N, apple_sizes)
print(result)
