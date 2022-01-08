def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    i = j = 0
    lst = []
    while (i<n and j <m):
        if arr[i] == brr[j]:
            lst.append(arr[i])
            i += 1
            j += 1
        elif arr[i]<brr[j]:
            i += 1
        else:
            j += 1
        return -1
    return lst

arr =[1,4,5]
brr =[3]
n =len(arr)
m = len(brr)
print(findArrayIntersection(arr,n,brr,m))