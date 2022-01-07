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
        

        

arr = [1,2,3,4,5,6]
n = len(arr)

print(ReverseArray(arr,n))