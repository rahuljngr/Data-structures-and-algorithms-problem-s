def findUnique(arr, n) :
    ans = 0
    for i in range(n):
        #use XOR a^a = 0 and 0^a = a
        ans = ans^arr[i]
    return ans

arr = [2,3,4,2,3,4,5]
n = len(arr)
print(findUnique(arr,n))