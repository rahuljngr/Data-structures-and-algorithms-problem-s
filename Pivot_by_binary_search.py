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

arr = [2,3,4,5,67,1]
print(getPivot(arr))