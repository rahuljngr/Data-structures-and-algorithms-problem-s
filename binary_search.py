def binarySearch(arr,n,k):
    start = 0
    end = n-1
    while start <= end:
        mid = int(start+(end-start)/2)
        if arr[mid]> k : end = mid -1 #change end value 
        elif arr[mid] < k : start = mid + 1 # change start value
        else: return mid
    return -1
    
arr =[2,3,4,98]
print(len(arr))
k = 2
print(binarySearch(arr,len(arr),k))
