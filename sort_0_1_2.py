#Sort an array of 0s, 1s and 2
def sort012(arr, n) :
    lst_0=[]
    lst_1=[]
    lst_2=[]
    for i in range(n):
        if arr[i]==0:
            lst_0.append(0)
        elif arr[i]==1:
            lst_1.append(1) 
        elif arr[i]==2:
            lst_2.append(2)
    
    i=0        
    for x in lst_0:
        arr[i]=x
        i+=1
                
    for x in lst_1:
        arr[i]=x
        i+=1
    for x in lst_2:
        arr[i]=x
        i+=1
    
    return arr
