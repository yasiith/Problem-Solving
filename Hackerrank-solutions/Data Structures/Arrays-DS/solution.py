def reverseArray(a):
    return a[::-1]

n = int ( input() )

arr = list(map(int, input().split()))

reversed_arr = reversedArray(arr)
print(*reversed_arr)