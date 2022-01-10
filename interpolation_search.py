def interpolationSearch(arr,k):
    low = 0
    high = len(arr)-1
    if arr[low] == k: # if arr has only one element
        return low

    while arr[low]<= k and arr[high] >= k:
        mid = int(low+((k-arr[low])/(arr[high]-arr[low]))*(high-low))
        
        if arr[mid]<k:
            low = mid + 1
        elif arr[mid]> k:
            high = mid - 1
        else:
            return mid

    return -1 # if k in not in arr
arr = [1,3,5,11,17,18,19,21]
k = 18
print(interpolationSearch(arr,k))