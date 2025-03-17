# 6 x 6 2D array, maximum hourglass sum

def hourglassSum(arr):
    # max_sum is defined as a minimum value
    max_sum = float('-inf')
    # Loop through the 2D array
    # looping occurs from 1 to 4 centered values of the hourglass to prevent out of bound indices
    # looping occurs from row 1 to row 4 and column 1 to column 4
    for i in range(1,5):
        for j in range(1,5):
            # calculate the sum of the hourglass
            hg_sum = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            # update the max_sum if the current hourglass sum is greater
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