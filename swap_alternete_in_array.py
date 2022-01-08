def swapAlternate(arr,n):
    for i in range(0,n,2):
        if i+1 <n:
            arr[i], arr[i+1] = arr[i+1],arr[i]
    return arr



even = [2,5,9,6,8,12,]

odd = [6,54,34,23,98]
n = len(odd)
m = len(even)

print(swapAlternate(odd,n))
print(swapAlternate(even,m))