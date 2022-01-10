#get a pivot number
def getPivot(arr):
    s = 0
    e = len(arr)-1
    while s <e:
        mid = int(s + (e-s)/2)
        if arr[mid] >= arr[0]:
            s = mid +1
        else:
            e = mid
    return s
#use BS
def binarySearch(arr,s,e,k):
    start = s
    end = e
    while start <= end:
        mid = int(start+(end-start)/2)
        if arr[mid]> k : end = mid -1 #change end value 
        elif arr[mid] < k : start = mid + 1 # change start value
        else: return mid
    return -1

def findPosition(arr, n, k):
    pivot = getPivot(arr)

    if k >= arr[pivot] and k <= arr[n-1]:
        #BS on second line
        return binarySearch(arr,pivot,n-1,k)
    else:
        #BS on  first line
        return binarySearch(arr,0,pivot-1,k)

arr =[8,9,4,5]
k = 8
print(findPosition(arr,len(arr),k))