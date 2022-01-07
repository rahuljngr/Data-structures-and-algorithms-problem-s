def reverseArray(arr,n):
    # create a new array
    rarr = []
    for i in range(n+1):
        #add arr in reverse to new array
        rarr.append(int(arr[-i]))
    # return narr start with indexing 1
    return rarr[1:]

def ReverseArray(arr,n):
    # create 2 variable
    start = 0
    end = n-1
    while start <= end :
        #swap array
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr
        

        

arr = [1]
n = len(arr)

print(ReverseArray(arr,n))