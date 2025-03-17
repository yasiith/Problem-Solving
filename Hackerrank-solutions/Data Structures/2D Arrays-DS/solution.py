# 6 x 6 2D array, maximum hourglass sum

def hourglassSum(arr):
    max_sum = float('-inf')
    for i in range(1,5):
        for j in range(1,5):
            hg_sum = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            max_sum = max(max_sum, hg_sum)

    return max_sum

# Example Usage
arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

print(hourglassSum(arr))  # Output: 19