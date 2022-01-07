arr = list(input().split())
size_of_arr = len(arr)


def sumOfArray(arr,n):
    sum = 0
    for i in range(n):
        sum += int(arr[i])
        
    return sum

print(sumOfArray(arr,size_of_arr))
