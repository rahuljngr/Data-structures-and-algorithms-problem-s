def peakIndexInMountainArray( arr: list[int]) -> int:
    start = 0
    end = len(arr)-1
    while start <end:
        mid = int(start+(end-start)/2)
        if arr[mid]<arr[mid+1]:
            start = mid+1
        else:
            end = mid
                
    return start

arr = [1,2,3,4,5,8,9,5,4,3,2]
print(peakIndexInMountainArray(arr))