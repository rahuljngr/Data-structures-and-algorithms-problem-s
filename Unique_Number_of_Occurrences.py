def uniqueOccurrences(arr,n):
    new_arr=[]
    set_arr=set(arr)
    print(set_arr)
    for i in set_arr:
        print(arr.count(i))
        new_arr.append(arr.count(i))
    #print(set_arr)
    #print(set(new_arr))
    #print(new_arr)
    return len(new_arr)==len(set(new_arr))

arr = [1,1,1,2,2,3,3]
n = len(arr)
print(uniqueOccurrences(arr,n))
            