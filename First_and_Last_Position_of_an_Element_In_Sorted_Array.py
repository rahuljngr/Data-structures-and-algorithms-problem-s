def firstOcc(arr,n,k):
    start = 0
    end = n-1
    ans = -1
    while start <= end:
        mid = int(start+(end-start)/2)
        if k == arr[mid]:
            ans = mid
            end = mid-1
        elif arr[mid]> k : end = mid -1 #change end value 
        elif arr[mid] < k : start = mid + 1 # change start value
            
        #return ans
    return ans

def lastOcc(arr,n,k):
    start = 0
    end = n-1
    ans = -1
    while start <= end:
        mid = int(start+(end-start)/2)
        if k == arr[mid]:
            ans = mid
            start = mid+1
        elif arr[mid]> k : end = mid -1 #change end value 
        elif arr[mid] < k : start = mid + 1 # change start value
            
        #return ans
    return ans
    


def firstAndLastPosition(arr, n, k):
    first =firstOcc(arr,len(arr),k)
    last =  lastOcc(arr,len(arr),k)
    total_number_of_occ = (last-first)+1
    return first , last
    #return total_number_of_occ
arr = [0,0,0,0]
k = 0
print(firstAndLastPosition(arr,len(arr),k))