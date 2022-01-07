size_of_arr = int(input())
arr = list(input().split())

def maxArray(arr,n):
    max = arr[0]
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    return max
    
def minArray(arr,n):
    min = arr[0]
    for i in range(1,n):
        if min > arr[i]:
            min = arr[i]
    return min

print(maxArray(arr,size_of_arr))
print(minArray(arr,size_of_arr))
