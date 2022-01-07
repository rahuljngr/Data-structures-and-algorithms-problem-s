def search(arr,n,key):
    for i in range(n):
        if int(arr[i]) == key:
            return True
    return False
        
arr = list(input().split())
n = len(arr)
key = int(input())
print(search(arr,n,key))

